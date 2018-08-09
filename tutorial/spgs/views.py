from enum import Enum

import pymysql
import time
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_http_methods

from .tools import getStatus, getStationMsg
from .models import *




@require_http_methods(['GET'])
def apiTest(request):
    response = {}
    rs = DataSpgsBuffer.objects.all()
    # data = DataSpgsBuffer.objects.all()
    for x in [eval('DataSpgsBuffer.objects.all()[0].' + 'nbqgl' + str(i)) for i in range(1, 11)]:
        print(x)
        print(range(1, 11))
    print(type(rs[0]))
    response['msg'] = str(rs[0].datatime)
    response['error_num'] = 1
    return JsonResponse(response)
