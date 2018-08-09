import time

import pymysql
from django.core import serializers
from django.shortcuts import render
# coding=utf-8
# Create your views here.
import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods

from ctyd.models import *
from pvmg.models import *
from spgs.models import *

from spgs.models import *

from pvmg.tools import powerStationInfoPvmg
from spgs.tools import powerStationInfoSpgs
from .tools import *
from .models import *

# database configuration
database_ip = 'localhost'
database_port = '3306'
database_name = 'solar'
user = 'root'
pwd = ''


# 返回监测的发电站及其站内逆变器信息
@require_http_methods(['GET'])
def powerStations(request):
    response = {}
    list = []
    try:
        stations = PowerStation.objects.all()
        for item in stations:
            if item.pk == 1:
                templist = ["逆变器"]
                list.append({'systemType': item.systemtype.systemtype, 'systemName': item.systemtype.systemname,
                             'devices': templist})
            if item.pk == 2:
                templist = [("逆变器" + str(i)) for i in range(1, 10)]
                list.append({'systemType': item.systemtype.systemtype, 'systemName': item.systemtype.systemname,
                             'devices': templist})
            if item.pk == 3:
                templist = [("逆变器" + str(i)) for i in range(1, 11)]
                list.append({'systemType': item.systemtype.systemtype, 'systemName': item.systemtype.systemname,
                             'devices': templist})
        response['list'] = list
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 所有系统的当日累计发电量总和
@require_http_methods(['GET'])
def totalGeneratingCapacity_today(request):
    response = {}
    try:
        data = getTotalGeneratingCapacity_today()
        response['data'] = data
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 所有系统的当月累计发电量总和
@require_http_methods(['GET'])
def totalGeneratingCapacity_thisMonth(request):
    response = {}
    try:
        data = getTotalGeneratingCapacity_thisMonth()
        response['data'] = data
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 所有系统累计发电量总和
@require_http_methods(['GET'])
def totalGeneratingCapacity(request):
    response = {}
    try:
        response['data'] = getTotalGeneratingCapacity()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 返回当前所有电站的总容量
@require_http_methods(['GET'])
def totalVolume(request):
    response = {}
    try:
        data = getTotalVolume()
        response['data'] = data
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 返回首页echarts图当日发电量模块中逆变器发电量的数据
@require_http_methods(['GET'])
def echartsDataForInverterFDL(request):
    response = {}
    try:
        data = getEchartsDataForInverterFDL()
        response['data'] = data
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 返回首页当日发电功率的逆变器发电功率数据
@require_http_methods(['GET'])
def echartsDataForInverterFDGL(request):
    response = {}
    try:
        data = getEchartsDataForInverterFDGL()
        response['msg'] = data
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 返回当日发电功率echarts图总辐照度的数据
@require_http_methods(['GET'])
def echartsDataForFZD(request):
    response = {}
    try:
        data = getEchartsForZGL()
        response['data'] = data
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 返回电站总数
@require_http_methods(['GET'])
def powerStationsNum(request):
    response = {}
    try:
        num = getSationNum()
        response['data'] = num
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 返回电站监测信息
@require_http_methods(['GET'])
def getStationMonitorInfo(request):
    response = {}
    try:
        dzzs = getSationNum()
        zjrl = getTotalVolume()
        jrfdl = getTotalGeneratingCapacity_today()
        ljzjdl = getTotalGeneratingCapacity()
        items = {"dzzs": dzzs, "zjrl": zjrl, "jrfdl": jrfdl, "ljzjdl": ljzjdl}
        temp1 = powerStationInfoPvmg()
        temp2 = powerStationInfoSpgs()
        cardLists = [temp1, temp2]
        response['data'] = {"items": items, "cardLists": cardLists}
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(['GET'])
def apiTest(request):
    response = {}
    try:
        rs = PowerStation.objects.all()
        num = len(rs)
        response['data'] = num
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
