# database configuration
import datetime

import pymysql
import time
import json
from django.core import serializers
from spgs.models import DataSpgsBuffer

from pvmg.models import DataPvmgBuffer

from pvmg.tools import powerStationInfoPvmg

from spgs.tools import powerStationInfoSpgs

from pvmg.models import DataPvmgHistory
from spgs.models import DataSpgsHistory
from .models import *
from tutorial.settings import DATABASES

# database configuration
database_ip = DATABASES['default']['HOST']
database_port = DATABASES['default']['PORT']
database_name = DATABASES['default']['NAME']
user = DATABASES['default']['USER']
pwd = DATABASES['default']['PASSWORD']


def getSationNum():
    rs = PowerStation.objects.all()
    num = len(rs)
    return num


def getEchartsForZGL():
    db = pymysql.connect(database_ip, user, pwd, database_name)
    cursor = db.cursor()
    # sql1 = "select FDZGL from data_spgs_history WHERE date_format(datatime,'%Y-%m-%d')='" + "2017-04-27" + "'"
    # cursor.execute(sql1)
    # data1 = cursor.fetchall()
    # sql2 = "select datatime  from data_spgs_history WHERE date_format(datatime,'%Y-%m-%d')='" + "2017-04-27" + "'"
    # cursor.execute(sql2)
    # time1 = cursor.fetchall()
    sql1 = "select fz from data_spgs_history WHERE datatime BETWEEN '" + "2017-05-06 " + datetime.datetime.strftime(
        datetime.datetime.now() - datetime.timedelta(hours=2),
        '%H:%M') + "' and '" + "2017-05-06 " + datetime.datetime.strftime(datetime.datetime.now(), '%H:%M') + "' "
    cursor.execute(sql1)
    data2 = cursor.fetchall()
    sql2 = "select date_format(datatime,'%H:%i') from data_spgs_history WHERE datatime BETWEEN '" + "2017-05-06 " + datetime.datetime.strftime(
        datetime.datetime.now() - datetime.timedelta(hours=2),
        '%H:%M') + "' and '" + "2017-05-06 " + datetime.datetime.strftime(datetime.datetime.now(), '%H:%M') + "' "
    cursor.execute(sql2)
    time2 = cursor.fetchall()
    rs_time = []
    rs_data = []
    for x in data2:
        rs_data.append(x[0])
    for y in time2:
        rs_time.append(y[0])
    data = {'series': rs_data, 'xAxix': rs_time}
    db.close()
    return data


def getEchartsDataForInverterFDGL():
    db = pymysql.connect(database_ip, user, pwd, database_name)
    cursor = db.cursor()
    # sql1 = "select FDZGL from data_spgs_history WHERE date_format(datatime,'%Y-%m-%d')='" + "2017-04-27" + "'"
    # cursor.execute(sql1)
    # data1 = cursor.fetchall()
    # sql2 = "select datatime  from data_spgs_history WHERE date_format(datatime,'%Y-%m-%d')='" + "2017-04-27" + "'"
    # cursor.execute(sql2)
    # time1 = cursor.fetchall()
    sql1 = "select FDZGL from data_spgs_history WHERE datatime BETWEEN '" + " 2017-05-06 " + datetime.datetime.strftime(
        datetime.datetime.now() - datetime.timedelta(hours=2),
        '%H:%M') + "' and '" + " 2017-05-06 " + datetime.datetime.strftime(datetime.datetime.now(), '%H:%M') + "' "
    cursor.execute(sql1)
    data2 = cursor.fetchall()
    sql2 = "select date_format(datatime,'%H:%i') from data_spgs_history WHERE datatime BETWEEN '" + "2017-05-06 " + datetime.datetime.strftime(
        datetime.datetime.now() - datetime.timedelta(hours=2),
        '%H:%M') + "' and '" + " 2017-05-06 " + datetime.datetime.strftime(datetime.datetime.now(), '%H:%M') + "' "
    cursor.execute(sql2)
    time2 = cursor.fetchall()
    rs_time = []
    rs_data = []
    for x in data2:
        rs_data.append(x[0])
    for y in time2:
        rs_time.append(y[0])
    data = {'series': rs_data, 'xAxix': rs_time}
    db.close()
    return data


def getEchartsDataForInverterFDL():
    db = pymysql.connect(database_ip, user, pwd, database_name)
    cursor = db.cursor()
    sql_time = " select date_format(total_d,'%H:%i') from spgs_minute WHERE total_d BETWEEN '" + "2017-05-06 " + datetime.datetime.strftime(
        datetime.datetime.now() - datetime.timedelta(hours=2),
        '%H:%M') + "' and '" + "2017-05-06 " + datetime.datetime.strftime(datetime.datetime.now(), '%H:%M') + "' "
    sql_data = " SELECT (@csum := @csum + TOTAL_FDL) AS total_fdl FROM spgs_minute  WHERE total_d BETWEEN '" + "2017-05-06 " + datetime.datetime.strftime(
        datetime.datetime.now() - datetime.timedelta(hours=2),
        '%H:%M') + "' and '" + "2017-05-06 " + datetime.datetime.strftime(datetime.datetime.now(), '%H:%M') + "' "
    cursor.execute(sql_time)
    rs2_time = cursor.fetchall()
    cursor.execute('SET @csum := 0')
    cursor.execute(sql_data)
    rs2_data = cursor.fetchall()
    rs_time = []
    rs_data = []
    for x in rs2_data:
        rs_data.append(x[0])
    for y in rs2_time:
        rs_time.append(y[0])
    data = {'series': rs_data, 'xAxix': rs_time}
    db.close()
    return data


def getTotalVolume():
    dataSpgsBuffer = DataSpgsBuffer.objects.all()
    data = float(dataSpgsBuffer[0].zjrl) * 1.9
    return data


def getTotalGeneratingCapacity():
    db = pymysql.connect(database_ip, user, pwd, database_name)
    cursor = db.cursor()
    sql1 = "select LJFDL from data_pvmg_buffer "
    sql2 = "select LJFDL from data_spgs_buffer "
    cursor.execute(sql1)
    rs1 = cursor.fetchone()
    if rs1 is None:
        rs1 = 0
    cursor.execute(sql2)
    rs2 = cursor.fetchone()
    if rs2 is None:
        rs2 = 0
    db.close()
    data = float(rs1[0]) + float(rs2[0])
    return data


def getTotalGeneratingCapacity_thisMonth():
    db = pymysql.connect(database_ip, user, pwd, database_name)
    # use cursor to manipulate
    cursor = db.cursor()
    sql1 = "select total_fdl from spgs_month WHERE total_m='" + time.strftime('%Y-%m', time.localtime()) + "'"
    sql2 = "select total_fdl from pvmg_month WHERE total_m='" + time.strftime('%Y-%m', time.localtime()) + "'"
    cursor.execute(sql1)
    rs1 = cursor.fetchone()
    if not rs1 is None:
        arg1 = float(rs1[0])
    else:
        arg1 = 0.0
    cursor.execute(sql2)
    rs2 = cursor.fetchone()
    if not rs2 is None:
        arg2 = float(rs2[0])
    else:
        arg2 = 0.0
    db.close()
    data = arg1 + arg2
    return data


def getTotalGeneratingCapacity_today():
    start = datetime.datetime.strptime(time.strftime('%Y-%m-%d', time.localtime()), '%Y-%m-%d')
    end = start + datetime.timedelta(days=1)
    data_spgs = list(DataSpgsHistory.objects.filter(datatime__range=(start, end)).values_list('drfdl', flat=True))
    data_pvmg = list(DataPvmgHistory.objects.filter(datatime__range=(start, end)).values_list('jrfdl', flat=True))
    total = 0
    if len(data_spgs) > 0:
        total = + data_spgs[-1]
    if len(data_pvmg) > 0:
        total = + data_pvmg[-1]
    return total


def getDeviceInfo(systemType, deviceName):
    info = {}
    if systemType == "PVMG":
        pvmgBuffer = DataPvmgBuffer.objects.all()
        if not pvmgBuffer is None:

            data = json.loads((serializers.serialize('json', pvmgBuffer)))
            info['dqgl'] = data[0].get('fields').get(deviceName.lower())
        else:
            info['dqgl'] = 0.00
        try:
            db = pymysql.connect(database_ip, user, pwd, database_name)
            cursor = db.cursor()
            sql = "select " + "FDL_" + deviceName + " from pvmg_day where total_d= '" + time.strftime('%Y-%m-%d',
                                                                                                      time.localtime()) + "'"
            cursor.execute(sql)
            rs = cursor.fetchone()
            if not rs is None:
                info['jrfd'] = rs[0]
            else:
                info['jrfd'] = 0.00
            sql = "select " + deviceName + " from pvmg_total"
            cursor.execute(sql)
            rs = cursor.fetchone()
            if not rs is None:
                info['ljfd'] = rs[0]
            else:
                info['ljfd'] = 0.00
            info['zjrl'] = 50.00
            info['jrdx'] = powerStationInfoPvmg().get("dayHours")
            db.close()
        except Exception as e:
            print(e)
    if systemType == "SPGS":
        spgsBuffer = DataSpgsBuffer.objects.all()
        if not spgsBuffer is None:
            data = json.loads(serializers.serialize('json', spgsBuffer))
            info['dqgl'] = data[0].get('fields').get(deviceName)
        else:
            info['dqgl'] = 0.00
        try:
            db = pymysql.connect(database_ip, user, pwd, database_name)
            cursor = db.cursor()
            sql = "select " + "FDL_" + deviceName + " from spgs_day where total_d= '" + time.strftime('%Y-%m-%d',
                                                                                                      time.localtime()) + "'"
            cursor.execute(sql)
            rs = cursor.fetchone()
            if not rs is None:
                info['jrfd'] = rs[0]
            else:
                info['jrfd'] = 0.00
            sql = "select " + deviceName + " from spgs_total"
            cursor.execute(sql)
            rs = cursor.fetchone()
            if not rs is None:
                info['ljfd'] = rs[0]
            else:
                info['ljfd'] = 0.00
            info['zjrl'] = 50.00
            info['jrdx'] = powerStationInfoSpgs().get("dayHours")
            db.close()
        except Exception as e:
            print(e)
    info['bwrq'] = "2018-03-21"
    return info


def getDeviceList():
    list = []
    try:
        stations = PowerStation.objects.all()
        for item in stations:
            if item.pk == 1:
                templist = ["逆变器"]
                list.append({'systemType': item.systemtype.systemtype, 'systemName': item.systemtype.systemname,
                             'devices': templist})
            if item.pk == 2:
                templist = [{"NBQGL" + str(i): ("逆变器" + str(i))} for i in range(1, 10)]
                list.append({'systemType': item.systemtype.systemtype, 'systemName': item.systemtype.systemname,
                             'devices': templist})
            if item.pk == 3:
                templist = [{"NBQGL" + str(i): ("逆变器" + str(i))} for i in range(1, 11)]
                list.append({'systemType': item.systemtype.systemtype, 'systemName': item.systemtype.systemname,
                             'devices': templist})

    except Exception as e:
        print(e)
    finally:
        return list


# 获取环保数据，累计发电量所产生的环保价值
def getHuanBaoData():
    info = {}
    # connect database
    db = pymysql.connect(database_ip, user, pwd, database_name)
    # use cursor to manipulate
    cursor = db.cursor()
    sql1 = "select LJFDL from data_spgs_buffer "
    cursor.execute(sql1)
    rs1 = cursor.fetchone()
    if rs1 is None:
        rs1 = 0
    else:
        rs1 = float(rs1[0])
    sql1 = "select LJFDL from data_pvmg_buffer "
    cursor.execute(sql1)
    rs2 = cursor.fetchone()
    if rs2 is None:
        rs2 = 0
    else:
        rs2 = float(rs2[0])
    ljfdl = rs1 + rs2
    info['msg1'] = round(ljfdl * 0.4 / 1000, 2)
    info['msg2'] = round(ljfdl * 0.997 / 1000, 2)
    info['msg3'] = round(ljfdl * 0.03 / 1000, )
    info['msg4'] = round(ljfdl * 0.015 / 1000, 2)
    info['msg5'] = int(ljfdl * 0.997 / 5.023)
    db.close()
    return info
