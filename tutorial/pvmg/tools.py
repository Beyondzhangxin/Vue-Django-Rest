from enum import Enum

import pymysql
import time

from .models import *

from tutorial.settings import DATABASES

# database configuration
database_ip = DATABASES['default']['HOST']
database_port = DATABASES['default']['PORT']
database_name = DATABASES['default']['NAME']
user = DATABASES['default']['USER']
pwd = DATABASES['default']['PASSWORD']


class Status(Enum):
    normal = "zc"
    abnormal = "yc"
    offline = "lx"
    poweroff = "tj"


def getStatus(data):
    if data is None:
        status = Status.offline.value
    else:
        nbq1 = float(data[0].nbqgl1)
        nbq2 = float(data[0].nbqgl2)
        nbq3 = float(data[0].nbqgl3)
        nbq4 = float(data[0].nbqgl4)
        nbq5 = float(data[0].nbqgl5)
        nbq6 = float(data[0].nbqgl6)
        nbq7 = float(data[0].nbqgl7)
        nbq8 = float(data[0].nbqgl8)
        nbq9 = float(data[0].nbqgl9)
        if nbq1 and nbq2 and nbq3 and nbq4 and nbq5 and nbq6 and nbq7 and nbq8 and nbq9:
            status = Status.abnormal.value
        elif not (nbq1 or nbq2 or nbq3 or nbq4 or nbq5 or nbq6 or nbq7 or nbq8 or nbq9):
            status = Status.poweroff.value
        else:
            status = Status.normal.value
    print(type(status))
    print(status)
    return status


def getStationMsg():
    return []


def powerStationInfoPvmg():
    info = {}
    try:
        data = DataPvmgBuffer.objects.all()
        info['status'] = getStatus(data)
        db = pymysql.connect(database_ip, user, pwd, database_name)
        cursor = db.cursor()
        sql = "select  dayHours from pvmg_day WHERE total_d ='" + time.strftime('%Y-%m-%d', time.localtime()) + "'"
        cursor.execute(sql)
        rs = cursor.fetchone()
        if not rs is None:
            info['dayHours'] = rs[1]
        else:
            info['dayHours'] = 0
        info['zjrl'] = 50.0
        sql = "select fdzgl from data_pvmg_buffer"
        cursor.execute(sql)
        rs = cursor.fetchall()
        if not rs is None:
            info['yxgl'] = rs[0][0]
        else:
            info['yxgl'] = 0
        sql = "select monthHours from spgs_month WHERE total_m = '" + time.strftime('%Y-%m', time.localtime()) + "'"
        cursor.execute(sql)
        rs = cursor.fetchone()
        if not rs is None:
            info['monthHours'] = rs[0]
        else:
            info['monthHours'] = 0
        info['id'] = '青海'
        info['messageNum'] = len(getStationMsg())
        db.close()
        print(info)
        return info
    except  Exception as e:
        return None
