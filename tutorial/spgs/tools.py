# coding=utf-8
import datetime
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
    status = ''

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
        nbq10 = float(data[0].nbqgl10)
        if nbq1 and nbq2 and nbq3 and nbq4 and nbq5 and nbq6 and nbq7 and nbq8 and nbq9 and nbq10:
            status = Status.abnormal.value
        elif not (nbq1 or nbq2 or nbq3 or nbq4 or nbq5 or nbq6 or nbq7 or nbq8 or nbq9 or nbq10):
            status = Status.poweroff.value
        else:
            status = Status.normal.value
    return status


def getStationMsg():
    return []


def powerStationInfoSpgs():
    info = {}
    try:
        data = DataSpgsBuffer.objects.all()
        info['status'] = getStatus(data)
        db = pymysql.connect(database_ip, user, pwd, database_name)
        cursor = db.cursor()
        sql = "select  dayHours from spgs_day WHERE total_d ='" + time.strftime('%Y-%m-%d', time.localtime()) + "'"
        cursor.execute(sql)
        rs = cursor.fetchone()
        if not rs is None:
            info['dayHours'] = rs[1]
        else:
            info['dayHours'] = 0
        info['zjrl'] = 50.0
        sql = "select fdzgl from data_spgs_buffer"
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
        info['id'] = '多功能光伏电站系统'
        info['location']='青海'
        info['messageNum'] = len(getStationMsg())
        db.close()
        return info
    except  Exception as e:
        return None


# 获取电站某天的功率数据
def getSpgsGL(searchDate):
    start = datetime.datetime.strptime(searchDate, '%Y-%m-%d')
    end = start + datetime.timedelta(days=1)
    try:
        data = list(DataSpgsHistory.objects.filter(datatime__range=(start, end)).values_list('fdzgl', flat=True))
        datatime = list(DataSpgsHistory.objects.filter(datatime__range=(start, end)).values_list('datatime', flat=True))
        return {"data": data, "time": datatime}
    except Exception as e:
        print(e)
        return {"data": [], "time": []}


# 获取电站某天的有效时数
def getSpgsDXSS(searchDate):
    start = datetime.datetime.strptime(searchDate, '%Y-%m-%d')
    end = start + datetime.timedelta(days=1)
    try:
        db = pymysql.connect(database_ip, user, pwd, database_name)
        cursor = db.cursor()
        sql = "select dayHours from spgs_day WHERE total_d  = '" + searchDate + "'"
        cursor.execute(sql)
        rs = cursor.fetchone()
        if not rs is None:
            rs = round(float(rs[0]), 2)
        else:
            rs = 0
        datatime = list(DataSpgsHistory.objects.filter(datatime__range=(start, end)).values_list('datatime', flat=True))
        db.close()
        return {"data": rs, "time": datatime}
    except Exception as e:
        print(e)
        return {"data": [], "time": []}


# 获取电站某天当日的发电量
def getSpgsFDL(searchDate):
    start = datetime.datetime.strptime(searchDate, '%Y-%m-%d')
    end = start + datetime.timedelta(days=1)
    try:
        data = list(DataSpgsHistory.objects.filter(datatime__range=(start, end)).values_list('drfdl', flat=True))
        datatime = list(DataSpgsHistory.objects.filter(datatime__range=(start, end)).values_list('datatime', flat=True))
        return {"data": data, "time": datatime}
    except Exception as e:
        print(e)
        return {"data": [], "time": []}


# 获取设备的某个字段的数据信息
def getSpgsDeviceInfo(deviceName, param, searchDate):
    start = datetime.datetime.strptime(searchDate, '%Y-%m-%d')
    end = start + datetime.timedelta(days=1)
    if param == "GL":
        try:
            data = list(DataSpgsHistory.objects.filter(datatime__range=(start, end)).values_list(deviceName, flat=True))
            datatime = list(
                DataSpgsHistory.objects.filter(datatime__range=(start, end)).values_list('datatime', flat=True))
            return {"data": data, "time": datatime}
        except Exception as e:
            print(e)
            return {"data": [], "time": []}
    elif param == "DXSS":
        try:
            db = pymysql.connect(database_ip, user, pwd, database_name)
            cursor = db.cursor()
            sql = "select dayHours from spgs_day WHERE total_d  = '" + searchDate + "'"
            cursor.execute(sql)
            rs = cursor.fetchone()
            if not rs is None:
                rs = round(float(rs[0]), 2)
            else:
                rs = 0
            datatime = list(
                DataSpgsHistory.objects.filter(datatime__range=(start, end)).values_list('datatime', flat=True))
            db.close()
            return {"data": rs, "time": datatime}
        except Exception as e:
            print(e)
            return {"data": [], "time": []}
    elif param == "FDL":
        try:
            db = pymysql.connect(database_ip, user, pwd, database_name)
            cursor = db.cursor()
            sql = "select FDL_" + deviceName.upper() + " from spgs_minute WHERE DATE_FORMAT(total_d,'%Y-%m-%d')='" + searchDate + "'"
            cursor.execute(sql)
            rs = cursor.fetchall()
            rs_list = []
            rs_time = []
            for x in rs:
                rs_list.append(x[0])
            sql = "select total_d from spgs_minute WHERE DATE_FORMAT(total_d,'%Y-%m-%d')='" + searchDate + "'"
            cursor.execute(sql)
            datatime = cursor.fetchall()
            for x in datatime:
                rs_time.append(x[0])
            db.close()
            return {"data": rs_list, "time": rs_time}
        except Exception as e:
            print(e)
            return {"data": [], "time": []}
    else:
        return {"data": [], "time": []}


def getSpgsDeviceInfoAll(deviceName, param, searchDate):
    start = datetime.datetime.strptime(searchDate, '%Y-%m-%d')
    end = start + datetime.timedelta(days=1)
    datatime = list(
        DataSpgsHistory.objects.filter(datatime__range=(start, end)).values_list('datatime', flat=True)
    )
    time_list = []
    for i in range(0, len(datatime)):
        time_list.append(datetime.datetime.strftime(datatime[i], '%Y-%m-%d %H:%M:%S'))
    if param == "GL":
        try:
            data = list(DataSpgsHistory.objects.filter(datatime__range=(start, end)))
            ls = []
            for x in data:
                ls.append(round(eval('x.' + deviceName),2))
            return {"data": ls, "time": time_list}
        except Exception as e:
            print(e)
            return {"data": [], "time": []}
    elif param == "DXSS":
        data_list = []
        for i in range(0, len(datatime)):
            hours = round((datatime[i] - datatime[0]).total_seconds() / 3600, 2)
            data_list.append(hours)
        return {"data": data_list, "time": time_list}
    else:
        try:
            db = pymysql.connect(database_ip, user, pwd, database_name)
            cursor = db.cursor()
            sql = "select * from spgs_minute WHERE DATE_FORMAT(total_d,'%Y-%m-%d')='" + searchDate + "'"
            cursor.execute(sql)
            rs = cursor.fetchall()
            rs_list = []
            index = int(deviceName[-1])
            for x in rs:
                rs_list.append(round(x[index + 2],2))
            db.close()
            return {"data": rs_list, "time": time_list}
        except Exception as e:
            print(e)
            return {"data": [], "time": []}
