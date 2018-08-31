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
    response = {}
    try:
        samples = switch[gmmConfig['system']]
        samples = samples.objects.filter(datatime__range=(start, end))
        gmmConfig['varables'] = gmmConfig['varables'].lower()
        samples = samples.values_list(*tuple(json.loads(gmmConfig['varables'])), flat=True)
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
        y = np.array(data.get('vector')).T
        j = data.get('j')
        option = 'marginal'
        # 纵向量
        # 将数据封装成matlab格式
        array = matlab.double(list(y))
        print(array)
        J = matlab.int8([j])
        # array = matlab.double([[(random.random()) * 100000 // 1 / 10000] for x in range(1000)])
        return engine.GMM_Distribution(array, J, 'EM', 'marginal')

# GMM_Distribution函数
# 输入多维训练集Y，matrix(矩阵)
# 输入GMM阶数J，int
# 输入option = 'marginal'
# 输入算法选项 method，str


class Joint:
    def model(self, data):
        engine = matlabEngineEnv()
        y = np.array(data.get('matrix')).T
        j = data.get('J')
        method = data.get('method')
        option = 'joint'
        array = matlab.double(list(y))
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
        j = data.get('J')
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
        # 可代替方案
        # 建立模型
        if data['options'] == 'marginal':
            config = self.formatData(data, getSamples(data))
            Marginal.model(self, config)

        # 计算功能
        if data['options'] == 'joint':
            data = self.formatData(serializer.data, getSamples(serializer.data))
            Joint.model(data)
        if data['options'] == 'conditional':
            data = self.formatData(serializer.data, getSamples(serializer.data))
            Conditional.model(data)

        # 根据具体方法建模
        return Response(serializer.data)

    def formatData(self, data={}, y=[]):
        if data['options'] == 'marginal':
            print(y)
            data['vector'] = [x for x in y]
        if data['options'] == 'joint':
            data['matrix'] = [x for x in y]
        if data['options'] == 'conditional':
            data['vector'] = [x for x in y]
        return data


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
