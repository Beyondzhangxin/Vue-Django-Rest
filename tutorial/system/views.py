import time
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
from .models import *


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
        spgsDay = SpgsDay.objects.filter(total_d=time.strftime('%Y-%m-%d', time.localtime()))
        pvmgDay = PvmgDay.objects.filter(total_d=time.strftime('%Y-%m-%d', time.localtime()))
        ctydDay = CtydDay.objects.filter(total_d=time.strftime('%Y-%m-%d', time.localtime()))
        response['data'] = float(spgsDay[0].total_fdl) + float(pvmgDay[0].total_fdl) + float(ctydDay[0].total_fdl)
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 所有系统的当月累计发电量总和
@require_http_methods(['GET'])
def totalGeneratingCapacity_thisMonth(request):
    try:
        spgsMonth = SpgsMonth.objects.get(total_m=time.strftime('%Y-%m', time.localtime()))
        pvmgMonth = PvmgMonth.objects.get(total_m=time.strftime('%Y-%m', time.localtime()))
        ctydMonth = CtydMonth.objects.get(total_m=time.strftime('%Y-%m', time.localtime()))
        response['data'] = float(spgsMonth.total_fdl) + float(pvmgMonth.total_fdl) + float(ctydMonth.total_fdl)
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 所有系统累计发电量总和
@require_http_methods(['GET'])
def totalGeneratingCapacity(request):
    try:
        spgsTotal = SpgsToal.objects.get(pk=1)
        pvmgTotal = PvmgToal.objects.get(pk=1)
        pvmgTotal = pvmgToal.objects.get(pk=1)
        response['data'] = float(spgsTotal.total_fdl) + float(pvmgTotal.total_fdl) + float(pvmgTotal.total_fdl)
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(['GET'])
def apiTest(request):
    pass
