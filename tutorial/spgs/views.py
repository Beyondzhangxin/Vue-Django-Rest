import datetime
from enum import Enum

import pymysql
import time
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_http_methods

from .tools import getStatus, getStationMsg, getSpgsDeviceInfoAll
from .models import *
from tutorial.settings import DATABASES

# database configuration
database_ip = DATABASES['default']['HOST']
database_port = DATABASES['default']['PORT']
database_name = DATABASES['default']['NAME']
user = DATABASES['default']['USER']
pwd = DATABASES['default']['PASSWORD']


@require_http_methods(['GET'])
def apiTest(request):
    rs = getSpgsDeviceInfoAll('nbqgl1','FDL','2017-04-27')
    ls = rs.get('data')
    print(type(ls[0]))
    return JsonResponse({"time":rs.get('time')})

