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
from tutorial.settings import DATABASES

# database configuration
database_ip = DATABASES['default']['HOST']
database_port = DATABASES['default']['PORT']
database_name = DATABASES['default']['NAME']
user = DATABASES['default']['USER']
pwd = DATABASES['default']['PASSWORD']


@require_http_methods(['GET'])
def apiTest(request):
    db = pymysql.connect(database_ip, user, pwd, database_name)
    cursor = db.cursor()
    sql = "select dayHours from spgs_day WHERE total_d  = '" + "2017-04-27" + "'"
    cursor.execute(sql)
    rs = cursor.fetchone()
    if not rs is None:
        rs =round(float(rs[0]),2)
    else:
        rs = 0
    print(rs)