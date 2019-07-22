import datetime
import math
import os

import random
import time

import scipy
import scipy.io as scio
from clickhouse_driver import Client

from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import render

from .GMM_Calculation import GMM_calculation
from .functional import func_MonteCaro_JS
from .GMM_utils import getDevices, KL_martrices
from .GMM_Distribution import GMM_distribution
from .gmmTools import getDistribution
from .models import GmmConfig
from .serializer import GmmConfigSerializer
import json
import functools
from rest_framework import status
# Create your views here.
import numpy as np

# 错误wapper
from .models import GmmConfig

client = Client('192.168.0.147')


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




# 返回当前所有的distribution配置
def getAllDistributionConfigs(request):
    response = {}
    try:
        configList = json.loads((serializers.serialize('json', GmmConfig.objects.all())))
        # configList = json.dumps(GmmConfig.objects.all())
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


@require_http_methods(['GET'])
def delModel(request):
    id = request.GET.get('id')
    gmm = GmmConfig.objects.get(pk=id)
    response = {}
    try:
        gmm.delete()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(['POST'])
def gmm_qinghai(request):
    response = {}
    data = json.loads(request.body)
    config_id = data.get('id1')
    option = data.get('option')
    gmm_config = GmmConfig.objects.get(pk=config_id)
    gmm_object = getDistribution(gmm_config)
    distribution1 = gmm_object.get('gmm')['GMM']
    inf = float(gmm_object.get('min'))
    sup = float(gmm_object.get('max'))
    x_length = 100
    options = gmm_config.options  # gmm分布输出选择，maginal，joint和conditional
    option = data.get('option')
    x = np.linspace(inf, sup, x_length)
    try:
        if option == 'pdf':
            log_pdf = distribution1.score_samples(x[:, np.newaxis])
            pdf = np.exp(log_pdf)
            response['x'] = x.tolist()
            response['y'] = pdf.tolist()
        if option == 'cdf':
            cdf = list()
            for x_ in x:
                y_ = scipy.integrate.quad(lambda m: np.exp(distribution1.score_samples(np.array([[m]]))), -np.inf, x_)
                cdf.append(y_[0])
            response['x'] = x.tolist()
            response['y'] = cdf
        if option == 'kl':
            config_id2 = data.get('id2')
            gmm_config2 = GmmConfig.objects.get(pk=config_id2)
            gmm_object2 = getDistribution(gmm_config2)
            distribution2 = gmm_object2.get('gmm')['GMM']
            kl = func_MonteCaro_JS(
                distribution1, distribution2, 1000)
            response['kl'] = kl
        if option == 'quantile':
            n_min = data.get('n_min')
            n_max = data.get('n_max')
            GMM_calculation_result = GMM_calculation(distribution1, option, n_min=n_min, n_max=n_max)
            quantile = GMM_calculation_result['quantile']
            response['quantile'] = quantile.tolist()
        if option == 'rmse':
            pass
        if option == 'linear':
            A = np.array([int(data.get('A'))])
            b = np.array([int(data.get('b'))])
            GMM_calculation_result = GMM_calculation(distribution1, option, A=A, b=b)
            linear_gmm = GMM_calculation_result['linear_GMM']
            log_pdf = linear_gmm.score_samples(x[:, np.newaxis])
            pdf = np.exp(log_pdf)
            response['x'] = x.tolist()
            response['y'] = pdf.tolist()
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(['POST'])
def calculate(request):
    # engine = matlabEngineEnv()
    data = json.loads(request.body)
    config_id = data.get('id1')
    gmm_config = GmmConfig.objects.get(pk=config_id)
    gmm_object = getDistribution(gmm_config)
    distribution1 = gmm_object.get('gmm')['GMM']
    x_min = gmm_object.get('min')
    x_max = gmm_object.get('max')
    options = gmm_config.options  # gmm分布输出选择，maginal，joint和conditional
    option = data.get('option')
    A = data.get('A')
    b = data.get('b')
    id2 = data.get('id2')
    n_max = float(0 if data.get('n_max') == '' else data.get('n_min'))
    n_min = float(0 if data.get('n_min') == '' else data.get('n_min'))
    y = data.get('y')
    y_list = []
    x_scope = np.linspace(0, 15, 1000)
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
            log_pdf = distribution1.score_samples(x_scope[:, np.newaxis])
            pdf_array = np.exp(log_pdf)
            response['data'] = {'x_scope': x_scope.tolist(), 'y_scope': pdf_array.tolist()}
            # timestamp = time.time()
            # picName = "/gmm/" + str(timestamp) + '.png'
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


@require_http_methods(['POST'])
def test_gmm(request):
    data = json.loads(request.body)
    method = data.get('method')
    output = data.get('output')
    tableName = data.get('file')
    variableList = data.get('variableList')
    inf = data.get('inf')
    inf = 0
    x_length = request.GET.get('x_length')
    sup = data.get('sup')
    response = {}
    sup = 300
    x_length = 100
    var_str = 'toFloat32OrZero(' + '),toFloat32OrZero('.join(variableList) + ')'
    try:
        res = client.execute(
            "select " + var_str + " from " + tableName + " where orderNum between %(start)d and %(end)d",
            {'start': 0, 'end': 500})
        variableList = np.array(res).T.tolist()
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    if method == 'em':
        if output == 'pdf':
            power = np.array(variableList[0])
            gmm = GMM_distribution(
                power, 3, 'EM', 'marginal')['GMM']
            x = np.linspace(inf, sup, x_length)
            log_pdf = gmm.score_samples(x[:, np.newaxis])
            pdf = np.exp(log_pdf)
            response['x'] = x.tolist()
            response['y'] = pdf.tolist()
        if output == 'cdf':
            power = np.array(variableList[0])
            cdf = list()
            x = np.linspace(inf, sup, x_length)
            gmm = GMM_distribution(
                power, 3, 'EM', 'marginal')['GMM']
            for x_ in x:
                y_ = scipy.integrate.quad(lambda m: np.exp(gmm.score_samples(np.array([[m]]))), -np.inf, x_)
                cdf.append(y_[0])
            response['x'] = x.tolist()
            response['y'] = cdf
        if output == 'kl':
            matrix = KL_martrices(variableList, 'em')
            matrix_3d = list()
            axis = []
            for i in range(len(matrix)):
                axis.append(i)
                for j in range(len(matrix[i])):
                    matrix_3d.append([i, j, matrix[i][j]])
            response['x'] = axis
            response['y'] = axis
            response['data'] = matrix_3d
    return JsonResponse(response)


@require_http_methods(['GET'])
def my_image(request):
    name = request.GET.get('name')
    image_data = open("D:/gmm/" + name + ".png", "rb").read()
    return HttpResponse(image_data, content_type="image/png")

