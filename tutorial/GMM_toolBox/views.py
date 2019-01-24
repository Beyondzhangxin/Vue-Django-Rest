import datetime

import random
import time

from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import render

from .gmmTools import getDistribution
from .models import GmmConfig
from .serializer import GmmConfigSerializer
import matlab.engine
import matlab
import json
import functools
import matlab.engine
from rest_framework import status
# Create your views here.
import numpy as np

# 错误wapper
from .models import GmmConfig


def dealException(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        result = 0
        try:
            result = func(*args, **kw)
        except Exception as e:
            return {'exception': type(e)}
        return 0

    return wrapper


def matlabEngineEnv():
    # 开始运行matlab engine
    engine = matlab.engine.start_matlab()
    return engine


# 返回当前所有的distribution配置
def getAllDistributionConfigs(request):
    response = {}
    configList = []
    try:
        configs = GmmConfig.objects.all()
        if not configs is None:
            for x in configs:
                configList.append({"id": x.id, "name": x.name})
        response['data'] = configList
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


class Distribution(generics.ListCreateAPIView):
    queryset = GmmConfig.objects.all()
    serializer_class = GmmConfigSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DistributionList(generics.ListAPIView):
    serializer_class = GmmConfigSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    """
        通过名称得到config.
    """

    def get_queryset(self, name):
        queryset = GmmConfig.objects
        if name is not None:
            queryset = queryset.get(name=name)
        return queryset

    """
        List a queryset.
    """

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=False)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=False)
        return Response(serializer.data)

    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     print(queryset)
    #
    #     # print(Response(serializer.data).content)
    #     return Response(json.loads(queryset))
    # def get(self, request, format=None):
    #         # print(request.data)
    #         print(dict(request.query_params))
    #         # print(request.parsers)
    #         print(getSamples(dict(request.query_params)))
    #         return Response(123)


# 根据name得到config过滤的矩阵
# GMM_Distribution函数
# 输入单维训练集Y，vector(向量)
# 输入GMM阶数J，int
# 输入option = 'marginal'
# 输入算法选项 method，str
class Marginal:
    def model(self, data):
        engine = matlabEngineEnv()
        y = data.get('vector')
        j = data.get('j')
        option = 'marginal'
        # 纵向量
        # 将数据封装成matlab格式
        # row_vec = np.array(y)
        # col_vec = np.array([row_vec]).T
        # array = matlab.double(col_vec.tolist())
        array = matlab.double(y)
        J = matlab.int8([j])
        print(array)
        return engine.GMM_Distribution(array, J, 'EM', 'marginal')


# GMM_Distribution函数
# 输入多维训练集Y，matrix(矩阵)
# 输入GMM阶数J，int
# 输入option = 'marginal'
# 输入算法选项 method，str


class Joint:
    def model(self, data):
        engine = matlabEngineEnv()
        y = data.get('matrix')
        j = data.get('j')
        option = 'joint'
        # row_vec = np.array(y)
        # col_vec = np.array([row_vec]).T
        array = matlab.double(y)
        j = matlab.int8([j])
        return engine.GMM_Distribution(array, j, 'EM', option)


# GMM_Distribution函数
# 输入多维训练集 Y，matrix
# 输入GMM阶数 J，int
# 输入option=‘conditional’
# 输入算法选项 method，str
# 输入给定条件值 y，vector


class Conditional:
    def model(self, data):
        engine = matlabEngineEnv()
        y1 = data.get('matrix')
        y2 = data.get('y')
        j = data.get('j')
        method = data.get('method')
        option = 'conditional'
        array = matlab.double([y1])
        vector = matlab.double([y2])
        j = matlab.int8([j])
        return engine.GMM_Distribution(array, j, 'EM', option, vector)


class GetMatrix(APIView):
    # dao操作得到config数据
    def get_queryset(self, name):
        queryset = GmmConfig.objects
        if name is not None:
            queryset = queryset.get(name=name)
            print(queryset)
        return queryset

    # 变形成列向量和矩阵
    def formatData(self, data={}, y=[]):
        if data['options'] == 'marginal':
            data['vector'] = [[int(z) for z in x] for x in y]
        if data['options'] == 'joint':
            print([[int(z) for z in x] for x in y])
            data['matrix'] = [[int(z) for z in x] for x in y]
        # conditional 未测试
        if data['options'] == 'conditional':
            data['matrix'] = [list(int(z) for z in x) for x in y]
            list = []
            for var in json.loads(data['y']):
                list.push(var)
            data['y'] = list
        return data

    # 建模和画图
    def modelData(self, data):
        if data['options'] == 'marginal':
            config = self.formatData(data, getSamples(data))
            model = Marginal.model(self, config)
            # 建模后绘制图形
            self.GMM_plot(distribution=model, options='singlePDF')
        if data['options'] == 'joint':
            data = self.formatData(data, getSamples(data))
            model = Joint.model(self, data)
            # 建模后绘制图形
            self.GMM_plot(distribution=model, options='multiPDF')
        if data['options'] == 'conditional':
            data = self.formatData(data, getSamples(data))
            model = Conditional.model(data)

    """
        计算
    """

    def calculate(self, request, distributionlist=None):
        op = request.data.options
        engine = matlabEngineEnv()
        if op == 'PDF':
            if distributionlist and len(distributionlist) == 2:
                self.result = engine.GMM_calculation(distributionlist[0], 'pdf', distributionlist[1])
        if op == 'CDF':
            if distributionlist and len(distributionlist) == 2:
                self.result = engine.GMM_calculation(distributionlist[0], 'cdf', distributionlist[1])
        if op == 'quantile':
            if distributionlist and len(distributionlist) == 2:
                self.result = engine.GMM_calculation(distributionlist[0], 'quantile', distributionlist[1])
        if op == 'KL':
            if distributionlist and len(distributionlist) == 2:
                self.result = engine.GMM_calculation(distributionlist[0], 'KL', distributionlist[1])
        if op == 'RMSE':
            if request.data.x:
                x = matlab.double(request.data.x)
            self.result = engine.GMM_calculation(distributionlist[0], 'RMSE', distributionlist[1], x)
        if op == 'linear':
            if request.data.A and request.data.b:
                a = matlab.double(request.data.A)
                b = matlab.double(request.data.b)
                self.result = engine.GMM_calculation(distributionlist[0], 'linear', a, b)

    # POST请求要走的流程
    def post(self, request, format=None):
        try:
            # 得到config数据
            # 必须POST reuest.data中要有config name1 name2
            serializer = GmmConfigSerializer()
            if request.data['name1'] and request.data['name2']:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            cofNameList = [request.data['name1'], request.data['name2']]
            # 根据名称得到config配置
            configList = [self.get_queryset(name) for name in cofNameList]
            # 根据config配置得到数据
            return Response(123134)
            dataList = [getSamples(config) for config in configList]
            # 将数据加载到config配置中 （要重新做）
            formatDateList = [self.formatDateList(self, data) for data in dataList]
            # 通过数据得到distribution
            distributionlist = [self.modelData(x) for x in dataList]
            # 通过distribution得到Configuration
            self.calculate(request, distributionlist)
        except Exception as e:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            print(e)
        # 返回函数生成的图像和distributionlist和calculate的计算结果》》
        return Response(1231231312)


@require_http_methods(['POST'])
def calculate(request):
    # engine = matlabEngineEnv()
    data = json.loads(request.body)
    config_id = data.get('id1')
    gmm_config = GmmConfig.objects.get(pk=config_id)
    distribution1 = getDistribution(gmm_config)
    options = gmm_config.options  # gmm分布输出选择，maginal，joint和conditional
    option = data.get('option')
    A = data.get('A')
    b = data.get('b')
    id2 = data.get('id2')
    n_max = float(0 if data.get('n_max')=='' else  data.get('n_min'))
    n_min = float(0 if data.get('n_min')=='' else  data.get('n_min'))
    x = matlab.double([[x * 10 // 1 / 10] for x in np.arange(0, 30, 0.1)])
    y = data.get('y')
    y_list = []
    x1 = matlab.double([[x * 10 // 1 / 10] for x in np.arange(-4, 12, 0.1)])
    y1 = matlab.double([[x * 10 // 1 / 10] for x in np.arange(-8, 24, 0.2)])
    if len(y) > 0:
        for x in y:
            y_list.append(float(x.get('val')))
    response = {}
    if option == 'pdf':
        # pdf = engine.GMM_calculation(distribution1, 'pdf', matlab.double(y_list))
        if options == "joint":
            timestamp = time.time()
            picName = "/gmm/" + str(timestamp) + '.png'
            # engine.GMM_plot(distribution1, 'multiPDF', x1, picName, y1, nargout=0)
            # response['data'] = {'result': pdf, 'pictureName': [str(timestamp)]}
        else:
            timestamp = time.time()
            picName = "/gmm/" + str(timestamp) + '.png'
            # engine.GMM_plot(distribution1, 'singlePDF', x1, picName, nargout=0)
            # response['data'] = {'result': pdf, 'pictureName': [str(timestamp)]}
    if option == 'cdf':
        # cdf = engine.GMM_calculation(distribution1, 'cdf', matlab.double(y_list))
        if options == 'joint':
            timestamp = time.time()
            picName = "/gmm/" + str(timestamp) + '.png'
            # engine.GMM_plot(distribution1, 'multiCDF', x1, picName, y1, nargout=0)
            # response['data'] = {'result': cdf, 'pictureName': [str(timestamp)]}
        else:
            timestamp = time.time()
            picName = "/gmm/" + str(timestamp) + '.png'
            # engine.GMM_plot(distribution1, 'singleCDF', x1, picName, nargout=0)
            # response['data'] = {'result': cdf, 'pictureName': [str(timestamp)]}
    if option == 'quantile':
        timestamp1 = time.time()
        picName = "/gmm/" + str(timestamp1) + '.png'
        # quantile = engine.GMM_calculation(distribution1, 'quantile', matlab.double([n_min]), matlab.double([n_max]))
        # engine.GMM_plot(distribution1, 'singlePDF', x1, picName, nargout=0)
        # response['data'] = {'result': quantile[-1][0], 'pictureName': [str(timestamp1)]}
    if option == 'KL':
        if options == 'joint':
            gmm_config2 = GmmConfig.objects.get(pk=id2)
            distribution2 = getDistribution(gmm_config2)
            # KL = engine.GMM_calculation(distribution1, 'KL', distribution2)
            timestamp1 = time.time()
            picName = "/gmm/" + str(timestamp1) + '.png'
            # engine.GMM_plot(distribution1, 'multiPDF', x1, picName, y1, nargout=0)
            timestamp2 = time.time()
            picName = "/gmm/" + str(timestamp2) + '.png'
            # engine.GMM_plot(distribution2, 'multiPDF', x1, picName, y1, nargout=0)
            # response['data'] = {'result': KL, 'pictureName': [str(timestamp1), str(timestamp2)]}
        else:
            gmm_config2 = GmmConfig.objects.get(pk=id2)
            distribution2 = getDistribution(gmm_config2)
            # KL = engine.GMM_calculation(distribution1, 'KL', distribution2)
            timestamp1 = time.time()
            picName = "/gmm/" + str(timestamp1) + '.png'
            # engine.GMM_plot(distribution1, 'singlePDF', x1, picName, nargout=0)
            timestamp2 = time.time()
            picName = "/gmm/" + str(timestamp2) + '.png'
            # engine.GMM_plot(distribution2, 'singlePDF', x1, picName, nargout=0)
            # response['data'] = {'result': KL, 'pictureName': [str(timestamp1), str(timestamp2)]}
    if option == 'RMSE':
        if options == 'joint':
            gmm_config2 = GmmConfig.objects.get(pk=id2)
            distribution2 = getDistribution(gmm_config2)
            # RMSE = engine.GMM_calculation(distribution1, 'RMSE', distribution2, x)
            timestamp1 = time.time()
            picName = "/gmm/" + str(timestamp1) + '.png'
            # engine.GMM_plot(distribution1, 'multiPDF', x1, picName, y1, nargout=0)
            timestamp2 = time.time()
            picName = "/gmm/" + str(timestamp2) + '.png'
            # engine.GMM_plot(distribution2, 'multiPDF', x1, picName, y1, nargout=0)
            # response['data'] = {'result': RMSE, 'pictureName': [str(timestamp1), str(timestamp2)]}
        else:
            gmm_config2 = GmmConfig.objects.get(pk=id2)
            distribution2 = getDistribution(gmm_config2)
            # RMSE = engine.GMM_calculation(distribution1, 'RMSE', distribution2, x)
            timestamp1 = time.time()
            picName = "/gmm/" + str(timestamp1) + '.png'
            # engine.GMM_plot(distribution1, 'singlePDF', x1, picName, nargout=0)
            timestamp2 = time.time()
            picName = "/gmm/" + str(timestamp2) + '.png'
            # engine.GMM_plot(distribution2, 'singlePDF', x1, picName, nargout=0)
            # response['data'] = {'result': RMSE, 'pictureName': [str(timestamp1), str(timestamp2)]}
    if option == 'linear':
        if options == 'joint':
            # linear = engine.GMM_calculation(distribution1, 'linear', matlab.double(A), matlab.double(b))
            timestamp1 = time.time()
            picName = "/gmm/" + str(timestamp1) + '.png'
            # engine.GMM_plot(linear, 'multiPDF', x1, picName, y1, nargout=0)
            # response['data'] = {'result': RMSE, 'pictureName': [str(timestamp1)]}
        else:
            # linear = engine.GMM_calculation(distribution1, 'linear', matlab.double(A), matlab.double(b))
            timestamp1 = time.time()
            picName = "/gmm/" + str(timestamp1) + '.png'
            # engine.GMM_plot(linear, 'singlePDF', x1, picName, nargout=0)
            # response['data'] = {'result': RMSE, 'pictureName': [str(timestamp1)]}
    return JsonResponse(response)


@require_http_methods(['GET'])
def my_image(request):
    name = request.GET.get('name')
    image_data = open("D:/gmm/" + name + ".png", "rb").read()
    return HttpResponse(image_data, content_type="image/png")


@require_http_methods(['GET'])
def jason(request):
    a = [1, 2, 3]
    eng = matlabEngineEnv()
    eng.Example_PlotmultiCDF(nargout=0)
    print("success")

# # def __init__(self):
#     self.result = None
# """
#     计算
# """
# def calculate(self, request, distributionlist=None):
#     op = request.data.options
#     engine = matlabEngineEnv()
#     if op == 'PDF':
#         if distributionlist and len(distributionlist) == 2:
#             self.result = engine.GMM_calculation(distributionlist[0], 'pdf', distributionlist[1])
#     if op == 'CDF':
#         if distributionlist and len(distributionlist) == 2:
#             self.result = engine.GMM_calculation(distributionlist[0], 'cdf', distributionlist[1])
#     if op == 'quantile':
#         if distributionlist and len(distributionlist) == 2:
#             self.result = engine.GMM_calculation(distributionlist[0], 'quantile', distributionlist[1])
#     if op == 'KL':
#         if distributionlist and len(distributionlist) == 2:
#             self.result = engine.GMM_calculation(distributionlist[0], 'KL', distributionlist[1])
#     if op == 'RMSE':
#         if request.data.x:
#             x = matlab.double(request.data.x)
#         self.result = engine.GMM_calculation(distributionlist[0], 'RMSE', distributionlist[1], x)
#     if op == 'linear':
#         if request.data.A and request.data.b:
#             a = matlab.double(request.data.A)
#             b = matlab.double(request.data.b)
#             self.result = engine.GMM_calculation(distributionlist[0], 'linear', a, b)
#
#
# """
#         List a queryset.
# """
# def list(self, request, *args, **kwargs):
#     # 得到name
#     name = request.query_params.get('name', None)
#     distributionlist = []
#     print(name)
#     queryset = self.filter_queryset(self.get_queryset(name))
#     page = self.paginate_queryset(queryset)
#     if page is not None:
#         serializer = self.get_serializer(page, many=False)
#         return self.get_paginated_response(serializer.data)
#     serializer = self.get_serializer(queryset, many=False)
#     data = serializer.data
#     print(123412412)
#     print(data)
#     # 可代替方案
#
#     # 建立模型
#     if data['options'] == 'marginal':
#         config = self.formatData(data, getSamples(data))
#         model = Marginal.model(self, config)
#         distributionlist.push(model)
#         # 建模后绘制图形
#         self.GMM_plot(distribution=model, options='singlePDF')
#     if data['options'] == 'joint':
#         data = self.formatData(serializer.data, getSamples(data))
#         model = Joint.model(self, data)
#         distributionlist.push(model)
#         # 建模后绘制图形
#         self.GMM_plot(distribution=model, options='multiPDF')
#     if data['options'] == 'conditional':
#         data = self.formatData(serializer.data, getSamples(data))
#         Conditional.model(data)
#         distributionlist.push(model)
#     # 根据具体方法建模
#     return Response(serializer.data)
#
# def formatData(self, data={}, y=[]):
#
#     if data['options'] == 'marginal':
#         data['vector'] = [[int(z) for z in x] for x in y]
#     if data['options'] == 'joint':
#         print([[int(z) for z in x] for x in y])
#         data['matrix'] = [[int(z) for z in x] for x in y]
#     if data['options'] == 'conditional':
#         data['matrix'] = [list(int(z) for z in x) for x in y]
#         list = []
#         for var in json.loads(data['y']):
#             list.push(var)
#         data['y'] = list
#     return data
#
# # 描绘功能
# def GMM_plot(self, distribution, options, x=None, y=None, Y_test=None, Y_tenum_intervalst=None):
#     engine = matlabEngineEnv()
#     x = matlab.double([[x] for x in np.arange(-4, 12, 0.1)])
#     if y is None:
#         y = matlab.double([[y] for y in np.arange(-10, 22, 0.2)])
#     if options == 'singlePDF':
#         engine.GMM_plot(distribution, options, x,  nargout=0)
#     if options == 'multiPDF':
#         engine.GMM_plot(distribution, options, x, y,  nargout=0)
#     if options == 'testPDF':
#         engine.GMM_plot(distribution, options, x, Y_test, Y_tenum_intervalst,  nargout=0)
#     if options == 'singleCDF':
#         engine.GMM_plot(distribution, options, x,  nargout=0)
#     if options == 'multiCDF':
#         engine.GMM_plot(distribution, options, x, y,  nargout=0)
#
#


# GMM_Distribution函数
# 输入多维训练集 Y，matrix
# 输入GMM阶数 J，int
# 输入算法选项 method=‘EM’


# class EM(Distribution):
#     def model(self, data):
#         engine = matlabEngineEnv()
#         y = data.get('matrix')
#         j = data.get('J')
#         array = matlab.double([y])
#         j = matlab.int8([j])
#         return engine.GMM_Distribution(array, j, 'EM')
#
#
# # GMM_Distribution函数
# # 输入多维训练集 Y，matrix
# # 输入GMM阶数 J，int
# # 输入算法选项 method=‘MAP’
#
#
# class MAP(Distribution):
#     def model(self, data):
#         engine = matlabEngineEnv()
#         pass

#
# class Calculation(APIView):
#     def model(self, data):
#         pass
#
#     def post(self, request, format=None):
#         self.model(request.data)
#         return Response(123)
#
#
# # 计算给定点PDF值
# # GMM_calculation函数
# # 输入GMM分布 distribution
# # 输入给定点值 x，float
# # 输入选项 option=‘PDF
#
#
# class PDF(Calculation):
#     def model(self, data):
#         pass
#
#
# # 计算给定的CDF值
# # GMM_calculation函数
# # 输入GMM分布 distribution
# # 输入给定点值 x，float
# # 输入选项 option=‘CDF’
#
# class CDF(Calculation):
#     def model(self, data):
#         pass
# # 计算分位数
# # GMM_calculation函数
# # 输入GMM分布 distribution
# # 输入给样本范围
# # 输入选项 option=‘quantile
#
#
# class Quantile(Calculation):
#     def model(self, data):
#         pass
# # 计算分布间KLD值
# # 计算分布间RMSE
#
# # GMM_calculation函数
# # 输入两个GMM分布 distribution
# # 输入选项 option=‘KL
#
#
# class KL(Calculation):
#     def model(self, data):
#         pass
#
# class RMSE(Calculation):
#     def model(self, data):
#         pass
# # 计算线性变换分布
# # GMM_calculation函数
# # 输入GMM分布 distribution
# # 输入线性变化系数 A和b
# # 输入选项 option=‘linear’
#
# class Linear(Calculation):
#     def model(self, data):
#         pass
