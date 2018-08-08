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
        # connect database
        db = pymysql.connect(database_ip, user, pwd, database_name)
        # use cursor to manipulate
        cursor = db.cursor()
        sql1 = "select total_fdl from spgs_day WHERE total_d='" + time.strftime('%Y-%m-%d', time.localtime()) + "'"
        # sql2 = "select total_fdl from pvmg_day WHERE total_d='" + time.strftime('%Y-%m-%d', time.localtime()) + "'"
        cursor.execute(sql1)
        rs1 = cursor.fetchone()
        if rs1 is None:
            rs1 = 0
        # cursor.execute(sql2)
        # rs2 = cursor.fetchone()
        # if rs2 is None:
        #     rs2 = 0
        db.close()
        response['data'] = float(rs1[0])
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
        db = pymysql.connect(database_ip, user, pwd, database_name)
        # use cursor to manipulate
        cursor = db.cursor()
        sql1 = "select total_fdl from spgs_month WHERE total_m='" + time.strftime('%Y-%m-%d', time.localtime()) + "'"
        sql2 = "select total_fdl from pvmg_month WHERE total_m='" + time.strftime('%Y-%m-%d', time.localtime()) + "'"
        cursor.execute(sql1)
        rs1 = cursor.fetchone()
        if rs1 is None:
            rs1 = 0
        cursor.execute(sql2)
        rs2 = cursor.fetchone()
        if rs2 is None:
            rs2 = 0
        db.close()
        response['data'] = float(rs1[0]) + float(rs2[0])
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
        db = pymysql.connect(database_ip, user, pwd, database_name)
        # use cursor to manipulate
        cursor = db.cursor()
        sql1 = "select total_fdl from spgs_total "
        sql2 = "select total_fdl from pvmg_total "
        cursor.execute(sql1)
        rs1 = cursor.fetchone()
        if rs1 is None:
            rs1 = 0
        cursor.execute(sql2)
        rs2 = cursor.fetchone()
        if rs2 is None:
            rs2 = 0
        db.close()
        response['data'] = float(rs1[0]) + float(rs2[0])
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
        dataSpgsBuffer = DataSpgsBuffer.objects.all()
        response['data'] = float(dataSpgsBuffer[0].zjrl) * 1.9
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 返回首页echarts图当日发电量模块中逆变器发电量的数据
@require_http_methods(['GET'])
def echartsDataForInverterFDL(request):
    currentDay = time.strftime('%Y-%m-%d', time.localtime())
    response = {}
    try:
        db = pymysql.connect(database_ip, user, pwd, database_name)
        cursor = db.cursor()
        # sql_time = "select total_d from pvmg_minute WHERE date_format(total_d,'%Y-%m-%d')='" + "2017-04-27" + "'"
        # sql_data = "SELECT  (@csum := @csum + TOTAL_FDL) AS total_fdl  FROM spgs_minute  WHERE DATE_FORMAT(total_d,'%Y-%m-%d') ='" + "2017-04-27" + "'"
        # cursor.execute(sql_time)
        # rs1_time = cursor.fetchall()
        # cursor.execute('SET @csum := 0')
        # cursor.execute(sql_data)
        # rs1_data = cursor.fetchall()
        sql_time = "select date_format(total_d,'%H:%m:%s') from spgs_minute WHERE date_format(total_d,'%Y-%m-%d')='" + '2017-04-27' + "'"
        sql_data = "SELECT (@csum := @csum + TOTAL_FDL) AS total_fdl FROM spgs_minute  WHERE DATE_FORMAT(total_d,'%Y-%m-%d') ='" + '2017-04-27' + "'"

        cursor.execute(sql_time)
        rs2_time = cursor.fetchall()
        cursor.execute('SET @csum := 0')
        cursor.execute(sql_data)
        rs2_data = cursor.fetchall()
        rs_time = rs2_time
        rs_data = rs2_data
        response['data'] = {'series':rs_data , 'xAxix':rs_time }
        response['msg'] = 'success'
        response['error_num'] = 0
        db.close()
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 返回首页当日发电功率的逆变器发电功率数据
@require_http_methods(['GET'])
def echartsDataForInverterFDGL(request):
    currentDay = time.strftime('%Y-%m-%d', time.localtime())
    response = {}
    try:
        db = pymysql.connect(database_ip, user, pwd, database_name)
        cursor = db.cursor()
        # sql1 = "select FDZGL from data_spgs_history WHERE date_format(datatime,'%Y-%m-%d')='" + "2017-04-27" + "'"
        # cursor.execute(sql1)
        # data1 = cursor.fetchall()
        # sql2 = "select datatime  from data_spgs_history WHERE date_format(datatime,'%Y-%m-%d')='" + "2017-04-27" + "'"
        # cursor.execute(sql2)
        # time1 = cursor.fetchall()
        sql1 = "select FDZGL from data_spgs_history WHERE date_format(datatime,'%Y-%m-%d')='" + "2017-04-27" + "'"
        cursor.execute(sql1)
        data2 = cursor.fetchall()
        sql2 = "select date_format(datatime,'%H:%m:%s')  from data_spgs_history WHERE date_format(datatime,'%Y-%m-%d')='" + "2017-04-27" + "'"
        cursor.execute(sql2)
        time2 = cursor.fetchall()
        rs_time = time2
        rs_data = data2
        response['data'] = {'series': rs_data, 'xAxix':  rs_time}
        response['msg'] = 'success'
        response['error_num'] = 0
        db.close()
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 返回当日发电功率echarts图总辐照度的数据
@require_http_methods(['GET'])
def echartsDataForFZD(request):
    currentDay = time.strftime('%Y-%m-%d', time.localtime())
    response = {}
    try:
        db = pymysql.connect(database_ip, user, pwd, database_name)
        cursor = db.cursor()
        # sql1 = "select FDZGL from data_spgs_history WHERE date_format(datatime,'%Y-%m-%d')='" + "2017-04-27" + "'"
        # cursor.execute(sql1)
        # data1 = cursor.fetchall()
        # sql2 = "select datatime  from data_spgs_history WHERE date_format(datatime,'%Y-%m-%d')='" + "2017-04-27" + "'"
        # cursor.execute(sql2)
        # time1 = cursor.fetchall()
        sql1 = "select fz from data_spgs_history WHERE date_format(datatime,'%Y-%m-%d')='" + "2017-04-27" + "'"
        cursor.execute(sql1)
        data2 = cursor.fetchall()
        sql2 = "select date_format(datatime,'%H:%m:%s') from data_spgs_history WHERE date_format(datatime,'%Y-%m-%d')='" + "2017-04-27" + "'"
        cursor.execute(sql2)
        time2 = cursor.fetchall()
        rs_time = time2
        rs_data = data2
        response['data'] = {'series':rs_data , 'xAxix':rs_time }
        response['msg'] = 'success'
        response['error_num'] = 0
        db.close()
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(['GET'])
def powerStationsNum(request):
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
