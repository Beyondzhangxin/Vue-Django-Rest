import datetime

import random
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import render
from  .models import GmmConfig
from  .serializer import GmmConfigSerializer
import matlab.engine
import matlab
import json
import functools
import matlab.engine
import numpy as np
# Create your views here.

# 错误wapper
from pvmg.models import DataPvmgHistory
from spgs.models import DataSpgsHistory
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


# 根据distribution配置返回训练样本列表,参数为GmmConfig
def getSamples(gmmConfig):
    switch = {
        "SPGS": DataSpgsHistory,
        "PVMG": DataPvmgHistory,
    }
    start = datetime.datetime.strptime(gmmConfig['start_time'], "%Y-%m-%d %H:%M:%S")
    end = datetime.datetime.strptime(gmmConfig['end_time'], "%Y-%m-%d %H:%M:%S")
    try:
        samples = switch[gmmConfig['system']]
        samples = samples.objects.filter(datatime__range=(start, end))
        print(gmmConfig['varables'])
        gmmConfig['varables'] = gmmConfig['varables'].lower()
        print(gmmConfig['varables'])
        samples = samples.values_list(*tuple(json.loads(gmmConfig['varables'])))
        print(samples)
        return samples
    except Exception as e:
        print(e)
        return []


class Distribution(generics.ListCreateAPIView):
    queryset = GmmConfig.objects.all()
    serializer_class = GmmConfigSerializer


class DistributionList(generics.ListAPIView):
    serializer_class = GmmConfigSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    """
        通过名称得到config.
    """
    def get_queryset(self):
        queryset = GmmConfig.objects
        name = self.request.query_params.get('name', None)
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
        row_vec = np.array(y)
        col_vec = np.array([row_vec]).T
        array = matlab.double(col_vec.tolist())
        J = matlab.int8([j])
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
        print(y)
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
        y2 = data.get('vector')
        j = data.get('j')
        method = data.get('method')
        option = 'conditional'
        array = matlab.double([y1])
        vector = matlab.double([y2])
        j = matlab.int8([j])
        return engine.GMM_Distribution(array, j, 'EM', option, y2)


class GetMatrix(DistributionList, Marginal, Joint, Conditional):
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
        data = serializer.data
        print(data)
        # 可代替方案
        # 建立模型
        if data['options'] == 'marginal':
            config = self.formatData(data, getSamples(data))
            model = Marginal.model(self, config)

        # 计算功能
        if data['options'] == 'joint':
            data = self.formatData(serializer.data, getSamples(data))
            Joint.model(self, data)
        if data['options'] == 'conditional':
            data = self.formatData(serializer.data, getSamples(data))
            Conditional.model(data)

        # 根据具体方法建模
        return Response(serializer.data)

    def formatData(self, data={}, y=[]):
        if data['options'] == 'marginal':
            print(y)
            data['vector'] = [int(*x) for x in y]
        if data['options'] == 'joint':

            data['matrix'] = [list(int(z) for z in x) for x in y]
            print(data['matrix'])
        if data['options'] == 'conditional':
            data['vector'] = [x for x in y]
        return data

    def GMM_plot(self, distribution, options, x, varargin = None):
        engine = matlabEngineEnv()
        if options == 'singlePDF':
            engine.GMM_plot(distribution, options, )
        if options == 'multiPDF':
            engine.GMM_plot()
        if options == 'testPDF':
            engine.GMM_plot
        if options == 'singleCDF':
            engine.GMM_plot
        if options == 'multiCDF':
            engine.GMM_plot
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


class Calculation(APIView):
    def model(self, data):
        pass

    def post(self, request, format=None):
        self.model(request.data)
        return Response(123)


# 计算给定点PDF值
# GMM_calculation函数
# 输入GMM分布 distribution
# 输入给定点值 x，float
# 输入选项 option=‘PDF


class PDF(Calculation):
    def model(self, data):
        pass


# 计算给定的CDF值
# GMM_calculation函数
# 输入GMM分布 distribution
# 输入给定点值 x，float
# 输入选项 option=‘CDF’

class CDF(Calculation):
    def model(self, data):
        pass
# 计算分位数
# GMM_calculation函数
# 输入GMM分布 distribution
# 输入给样本范围
# 输入选项 option=‘quantile


class Quantile(Calculation):
    def model(self, data):
        pass
# 计算分布间KLD值
# 计算分布间RMSE

# GMM_calculation函数
# 输入两个GMM分布 distribution
# 输入选项 option=‘KL


class KL(Calculation):
    def model(self, data):
        pass

class RMSE(Calculation):
    def model(self, data):
        pass
# 计算线性变换分布
# GMM_calculation函数
# 输入GMM分布 distribution
# 输入线性变化系数 A和b
# 输入选项 option=‘linear’

class Linear(Calculation):
    def model(self, data):
        pass
