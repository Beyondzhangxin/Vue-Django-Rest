import datetime
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

from pvmg.tools import getPvmgGL, getPvmgDXSS, getPvmgFDL
from spgs.tools import getSpgsGL, getSpgsDXSS, getSpgsFDL

from pvmg.tools import getPvmgDeviceInfo
from spgs.tools import getSpgsDeviceInfo
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
                sql_all = "select * from  " + x.get(
                    "systemType") + "_day  where total_d ='" + time.strftime(
                    '%Y-%m-%d',
                    time.localtime()) + "'"
                cursor.execute(sql_all)
                rs_all = cursor.fetchone()

                for i in range(0,len(x['devices'])):
                    dic = {}
                    (key, value), = x['devices'][i].items()
                    sql = "select " + key + " from  data_" + x.get("systemType") + "_buffer "
                    cursor.execute(sql)
                    rs = cursor.fetchone()
                    if not rs is None:
                        dqgl = rs[0]
                    else:
                        dqgl = 0.00
                    dic['dev_dqgl'] = dqgl
                    if not rs_all is None:
                        jrfd = rs_all[i+4]
                        dayHours = rs_all[2]
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
            response['data'] = {"tab": tab[start:end], "count": len(tab)}
            response['msg'] = 'success'
            response['error_num'] = 0
        except Exception as e:
            response['msg'] = str(e)
            response['error_num'] = 1
    else:
        response['msg'] = "缺少参数！"
        response['error_num'] = 1
    db.close()
    return JsonResponse(response)


# 返回首页下面的环保数据
@require_http_methods(['GET'])
def getHBSJ(request):
    response = {}
    try:
        data = getHuanBaoData()
        response['data'] = data
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 返回电站对比的信息，参数分别为电站型号列表如['SPGS','PVMG']，必须是大写
# compareParam是对比内容，汉子拼音简写，必须大写
# searchDate是查询日期字符串，格式为“2017-04-07”,默认是今天,请求头content_Type:application/x-www-form-urlencoded
@require_http_methods(['POST'])
def getStationCompareInfo(request):
    stationList =list(eval(request.POST.get("stationList")))
    compareParam = request.POST.get("compareParam")
    searhcDate = request.POST.get("searchDate")
    print(stationList, compareParam, searhcDate)
    print(type(stationList))
    if searhcDate is None:
        searhcDate = datetime.datetime.now().strftime('%Y-%m-%d')
    response = {}
    series = []
    xAxis = []
    try:
        if compareParam == 'GL':
            for temp in stationList:
                if temp == 'SPGS':
                    series.append({"name": "SPGS", "data": getSpgsGL(searhcDate).get("data")})
                    xAxis.append({"name": "SPGS", "data": getSpgsGL(searhcDate).get("time")})
                if temp == "PVMG":
                    series.append({"name": "PVMG", "data": getPvmgGL(searhcDate).get("data")})
                    xAxis.append({"name": "PVMG", "data": getPvmgGL(searhcDate).get("time")})
        if compareParam == 'DXSS':
            for temp in stationList:
                if temp == 'SPGS':
                    series.append({"name": "SPGS", "data": getSpgsDXSS(searhcDate).get("data")})
                    xAxis.append({"name": "SPGS", "data": getSpgsDXSS(searhcDate).get("time")})
                if temp == "PVMG":
                    series.append({"name": "PVMG", "data": getPvmgDXSS(searhcDate).get("data")})
                    xAxis.append({"name": "PVMG", "data": getPvmgDXSS(searhcDate).get("time")})
        if compareParam == 'FDL':
            for temp in stationList:
                if temp == 'SPGS':
                    series.append({"name": "SPGS", "data": getSpgsFDL(searhcDate).get("data")})
                    xAxis.append({"name": "SPGS", "data": getSpgsFDL(searhcDate).get("time")})
                if temp == "PVMG":
                    series.append({"name": "PVMG", "data": getPvmgFDL(searhcDate).get("data")})
                    xAxis.append({"name": "PVMG", "data": getPvmgFDL(searhcDate).get("time")})
        response['data'] = {"series": series, "xAxis": xAxis}
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 返回设备对比信息，参数分别为电站设备列表deviceList,格式如[{'SPGS':['NBQGL1','NBQGL2','NBQGL3']},{'PVMG':['NBQGL1','NBQGL2']}]
# 以及对比内容compareParam，还有查询日期searchDate
@require_http_methods(['POST'])
def getDeviceCompareInfo(request):
    current=datetime.datetime.now()
    deviceList = eval(request.POST.get("deviceList"))
    compareParam = request.POST.get("compareParam")
    searhcDate = request.POST.get("searchDate")
    if searhcDate is None:
        searhcDate = datetime.datetime.now().strftime('%Y-%m-%d')
    response = {}
    series = []
    xAxis = []
    try:
        for temp in deviceList:
            (key, value), = temp.items()
            if key == "SPGS":
                if not value is None:
                    for x in value:
                        series.append(
                            {"name": "SPGS",
                             "data": getSpgsDeviceInfo(x.lower(), compareParam, searhcDate).get("data")})
                        xAxis.append(
                            {"name": "SPGS",
                             "data": getSpgsDeviceInfo(x.lower(), compareParam, searhcDate).get("time")})
            if key == "PVMG":
                if not value is None:
                    for x in value:
                        series.append(
                            {"name": "PVMG",
                             "data": getPvmgDeviceInfo(x.lower(), compareParam, searhcDate).get("data")})
                        xAxis.append(
                            {"name": "PVMG",
                             "data": getPvmgDeviceInfo(x.lower(), compareParam, searhcDate).get("time")})
        response['data'] = {"series": series, "xAxis": xAxis}
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    ter = datetime.datetime.now()
    print(ter-current)
    return JsonResponse(response)


# 故障检测相关的table信息,参数为pageSize和pageNum

@require_http_methods(['GET'])
def getDetectionInfo(request):
    current = datetime.datetime.now()
    response = {}
    tabList = []
    deviceList = getDeviceList()
    pageNum = request.GET.get('pageNum')
    pageSize = request.GET.get('pageSize')
    end = int(pageNum) * int(pageSize)
    start = (int(pageNum) - 1) * int(pageSize)
    try:
        db = pymysql.connect(database_ip, user, pwd, database_name)
        cursor = db.cursor()
        for temp in deviceList:
            devices = temp.get('devices')
            sql_fdl= "select * from spgs_day WHERE total_d  = '" + datetime.datetime.now().strftime('%Y-%m-%d') + "'"
            cursor.execute(sql_fdl)
            rs_fdl = cursor.fetchone()
            for i in range(0,len(devices)):
                (key, value), = devices[i].items()
                info = {}
                systemType = temp.get('systemType')
                systemName = temp.get('systemName')
                info['dev_name'] = systemName + value
                info['dev_xh'] = key
                sql = "select " + key + "  from data_" + systemType + "_buffer "
                cursor.execute(sql)
                rs = cursor.fetchone()
                if not rs is None:
                    rs = float(rs[0])
                    if rs > 2:
                        info['dev_cjqzt'] = '正常'
                    elif rs > 0:
                        info['dev_cjqzt'] = '告警'
                    else:
                        info['dev_cjqzt'] = '停机'
                else:
                    rs = 0.00
                    info['dev_cjqzt'] = '离线'
                info['dev_dqgl'] = rs
                if not rs_fdl is None:
                    info['dev_jrfd']=round(rs_fdl[i+4],2)
                    info['dev_drdx']=rs_fdl[i+2]
                else:
                    info['dev_jrfd'] =0.00
                    info['dev_drdx'] = 0
                tabList.append(info)
        db.close()
        response['data'] = {"tab": tabList[start:end], "count": len(tabList)}
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    ter = datetime.datetime.now()
    print(ter-current)
    return JsonResponse(response)


@require_http_methods(['POST'])
def apiTest(request):
    print(request)
    print(request.body)
    a = request.POST.get("a")
    b = request.POST.get("b")
    print(a)
    print(b)
