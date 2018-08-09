# database configuration
import pymysql
import time
import json
from django.core import serializers
from spgs.models import DataSpgsBuffer

from pvmg.models import DataPvmgBuffer

from pvmg.tools import powerStationInfoPvmg

from spgs.tools import powerStationInfoSpgs
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
    currentDay = time.strftime('%Y-%m-%d', time.localtime())
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
    data = {'series': rs_data, 'xAxix': rs_time}
    db.close()
    return data


def getEchartsDataForInverterFDGL():
    currentDay = time.strftime('%Y-%m-%d', time.localtime())
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
    data = {'series': rs_data, 'xAxix': rs_time}
    db.close()
    return data


def getEchartsDataForInverterFDL():
    currentDay = time.strftime('%Y-%m-%d', time.localtime())
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
    data = {'series': rs_data, 'xAxix': rs_time}
    db.close()
    return data


def getTotalVolume():
    dataSpgsBuffer = DataSpgsBuffer.objects.all()
    data = float(dataSpgsBuffer[0].zjrl) * 1.9
    return data


def getTotalGeneratingCapacity():
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
    data = float(rs1[0]) + float(rs2[0])
    return data


def getTotalGeneratingCapacity_thisMonth():
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
    data = float(rs1[0]) + float(rs2[0])
    return data


def getTotalGeneratingCapacity_today():
    # connect database
    db = pymysql.connect(database_ip, user, pwd, database_name)
    # use cursor to manipulate
    cursor = db.cursor()
    sql1 = "select total_fdl from spgs_day WHERE total_d='" + time.strftime('%Y-%m-%d', time.localtime()) + "'"
    # sql2 = "select total_fdl from pvmg_day WHERE total_d='" + time.strftime('%Y-%m-%d', time.localtime()) + "'"
    cursor.execute(sql1)
    rs1 = cursor.fetchone()
    if rs1 is None:
        return 0.0
    else:
        db.close()
        return float(rs1[0])


def getDeviceInfo(systemType, deviceName):
    info = {}
    if systemType == "PVMG":
        pvmgBuffer = DataPvmgBuffer.objects.all()
        if not pvmgBuffer is None:

            data = json.loads((serializers.serialize('json', pvmgBuffer)))
            info['dqgl'] = data[0].get('fields').get(deviceName)
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
        except Exception as e:
            print(e)
    info['bwrq']="2018-03-21"
    return info
