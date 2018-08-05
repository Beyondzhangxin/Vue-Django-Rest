from django.core import serializers
from django.shortcuts import render
# coding=utf-8
# Create your views here.
import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods

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


@require_http_methods(['GET'])
def apiTest(request):
    pass