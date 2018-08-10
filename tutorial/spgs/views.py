import datetime
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
    start = datetime.datetime.strptime("2017-04-27", '%Y-%m-%d')
    end = start + datetime.timedelta(days=1)
    datatime = list(DataSpgsHistory.objects.filter(datatime__range=(start, end)).values_list('datatime', flat=True))
    print(str(datatime))

