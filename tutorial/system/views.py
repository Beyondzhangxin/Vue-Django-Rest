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

from pvmg.models import DataPvmgBuffer
from spgs.models import DataSpgsBuffer
from .tools import *
from .models import *
from tutorial.settings import DATABASES

# database configuration
database_ip = DATABASES['default']['HOST']
database_port = DATABASES['default']['PORT']
database_name = DATABASES['default']['NAME']
user = DATABASES['default']['USER']
pwd = DATABASES['default']['PASSWORD']


# 返回监测的发电站及其站内逆变器信息
@require_http_methods(['GET'])
def powerStations(request):
    response = {}
    try:
        list = getDeviceList()
        response['data'] = list
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
        response['data'] = data
        response['msg'] = 'success'
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


# 返回设备监测信息，参数systemType和deviceName，分别为系统类别如PVMG和设备名称如NBQGL1,区分大小写
@require_http_methods(['GET'])
def getDeviceMonitor(request):
    response = {}
    try:
        systemType = request.GET.get('systemType')
        deviceName = request.GET.get('deviceName')
        info = getDeviceInfo(systemType, deviceName)
        response['data'] = info
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 返回首页当前发电功率模块的数据信息
@require_http_methods(['GET'])
def getDQFDGL(request):
    dic = {}
    response = {}
    try:
        rs1 = DataSpgsBuffer.objects.all()
        rs2 = DataPvmgBuffer.objects.all()
        zgl = float(rs1[0].fdzgl) + float(rs2[0].fdzgl)
        jrlj = getTotalGeneratingCapacity_today()
        dylj = getTotalGeneratingCapacity_thisMonth()
        total = getTotalGeneratingCapacity()
        dic['ele'] = zgl
        dic['total'] = getTotalVolume()
        dic['day'] = jrlj
        dic['month'] = dylj
        dic['sumAll'] = total
        response['data'] = {'c1': dic}
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


# 返回设备监测页面,设备列表数据,必须有参数pageNum和pageSize，分别是第几页和每页显示多少条记录
@require_http_methods(['GET'])
def getDeviceTable(request):
    response = {}
    db = pymysql.connect(database_ip, user, pwd, database_name)
    cursor = db.cursor()
    tab = []
    lists = getDeviceList()
    pageNum = request.GET.get('pageNum')
    pageSize = request.GET.get('pageSize')
    if pageNum and pageSize:
        try:
            end = int(pageNum) * int(pageSize)
            start = (int(pageNum) - 1) * int(pageSize)
            for x in lists:
                for y in x['devices']:
                    dic = {}
                    (key, value), = y.items()
                    sql = "select " + key + " from  data_" + x.get("systemType") + "_buffer "
                    cursor.execute(sql)
                    rs = cursor.fetchone()
                    print(rs)
                    if not rs is None:
                        dqgl = rs[0]
                    else:
                        dqgl = 0.00
                    dic['dev_dqgl'] = dqgl
                    sql = "select FDL_" + key + " ,dayHours from  " + x.get("systemType") + "_day  where total_d ='" + time.strftime(
                        '%Y-%m-%d',
                        time.localtime()) + "'"
                    cursor.execute(sql)
                    rs = cursor.fetchone()
                    if not rs is None:
                        jrfd = rs[0]
                        dayHours = rs[1]
                    else:
                        jrfd = 0.00
                        dayHours = 0
                    dic['dev_jrfd'] = jrfd
                    dic['dev_name'] = value
                    dic['dev_xh'] = key
                    dic['dev_systemType'] = x.get('systemType')
                    dic['dev_systemName'] = x.get('systemName')
                    dic['dev_drdx'] = dayHours
                    tab.append(dic)
            response['data'] = {"tab":tab[start:end],"count":len(tab)}
            response['msg'] = 'success'
            response['error_num'] = 0
        except Exception as e:
            response['msg'] = str(e)
            response['error_num'] = 1
    else:
        response['msg'] = "缺少参数！"
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(['GET'])
def apiTest(request):
    response = {}
    try:
        systemType = request.GET.get('systemType')
        deviceName = request.GET.get('deviceName')
        info = getDeviceInfo(systemType, deviceName)
        response['data'] = info
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
