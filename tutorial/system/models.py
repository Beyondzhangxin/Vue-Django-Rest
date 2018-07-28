# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AnnoCtydBuffer(models.Model):
    title = models.CharField(db_column='TITLE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    target = models.CharField(db_column='TARGET', max_length=20, blank=True, null=True)  # Field name made lowercase.
    connent = models.TextField(db_column='CONNENT', blank=True, null=True)  # Field name made lowercase.
    author = models.CharField(db_column='AUTHOR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    annotime = models.DateTimeField(db_column='ANNOTIME', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'anno_ctyd_buffer'
# 角色表
class BasicRole(models.Model):
    roleid = models.CharField(db_column='ROLEID', primary_key=True, max_length=32)  # Field name made lowercase.
    rolename = models.CharField(db_column='ROLENAME', max_length=32)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=128, blank=True, null=True)  # Field name made lowercase.
    candelete = models.DecimalField(db_column='CANDELETE', max_digits=1, decimal_places=0)  # Field name made lowercase.
    sortindex = models.DecimalField(db_column='SORTINDEX', max_digits=4, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'basic_role'
# 用户表
class BasicUser(models.Model):
    userid = models.CharField(db_column='USERID', primary_key=True, max_length=32)  # Field name made lowercase.
    roleid = models.CharField(db_column='ROLEID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    usercode = models.CharField(db_column='USERCODE', max_length=32)  # Field name made lowercase.
    username = models.CharField(db_column='USERNAME', max_length=32)  # Field name made lowercase.
    psw = models.CharField(db_column='PSW', max_length=128)  # Field name made lowercase.
    pswsalt = models.CharField(db_column='PSWSALT', max_length=128)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=128, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CREATEDATE')  # Field name made lowercase.
    islocked = models.DecimalField(db_column='ISLOCKED', max_digits=1, decimal_places=0)  # Field name made lowercase.
    candelete = models.DecimalField(db_column='CANDELETE', max_digits=1, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'basic_user'
#设备类型表
class DeviceType(models.Model):
    devicecode = models.CharField(db_column='DEVICECODE', max_length=32)  # Field name made lowercase.
    systemtype = models.CharField(db_column='SYSTEMTYPE', max_length=32)  # Field name made lowercase.
    device = models.CharField(db_column='DEVICE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    devicename = models.CharField(db_column='DEVICENAME', max_length=128, blank=True, null=True)  # Field name made lowercase.
    sortindex = models.DecimalField(db_column='SORTINDEX', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'device_type'
#系统参数、字段信息表
class SystemParam(models.Model):
    systemtype = models.CharField(db_column='SYSTEMTYPE', max_length=32)  # Field name made lowercase.
    paramcode = models.CharField(db_column='PARAMCODE', max_length=32)  # Field name made lowercase.
    paramname = models.CharField(db_column='PARAMNAME', max_length=128)  # Field name made lowercase.
    datatype = models.DecimalField(db_column='DATATYPE', max_digits=2, decimal_places=0)  # Field name made lowercase.
    paramtype = models.DecimalField(db_column='PARAMTYPE', max_digits=2, decimal_places=0)  # Field name made lowercase.
    unit = models.CharField(db_column='UNIT', max_length=32, blank=True, null=True)  # Field name made lowercase.
    ismonitor = models.DecimalField(db_column='ISMONITOR', max_digits=1, decimal_places=0)  # Field name made lowercase.
    canoper = models.DecimalField(db_column='CANOPER', max_digits=1, decimal_places=0)  # Field name made lowercase.
    sortindex = models.DecimalField(db_column='SORTINDEX', max_digits=4, decimal_places=0)  # Field name made lowercase.
    paramid = models.CharField(db_column='PARAMID', primary_key=True, max_length=32)  # Field name made lowercase.
    pos = models.DecimalField(db_column='POS', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'system_param'
#系统信息表
class SystemType(models.Model):
    systemtype = models.CharField(db_column='SYSTEMTYPE', primary_key=True, max_length=32)  # Field name made lowercase.
    systemname = models.CharField(db_column='SYSTEMNAME', max_length=128)  # Field name made lowercase.
    sortindex = models.DecimalField(db_column='SORTINDEX', max_digits=4, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'system_type'

#报警简介
class Warnning(models.Model):
    device_type = models.CharField(db_column='DEVICE_TYPE', max_length=32)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=50)  # Field name made lowercase.
    position = models.DecimalField(db_column='POSITION', max_digits=4, decimal_places=0)  # Field name made lowercase.
    systemtype = models.CharField(db_column='SYSTEMTYPE', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'warnning'

#报警数据表
class WarnningHistory(models.Model):
    tagid = models.DecimalField(db_column='TAGID', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    systemtype = models.CharField(db_column='SYSTEMTYPE', max_length=32)  # Field name made lowercase.
    devicetype = models.CharField(db_column='DEVICETYPE', max_length=32)  # Field name made lowercase.
    paramid = models.CharField(db_column='PARAMID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='STARTTIME')  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='ENDTIME', blank=True, null=True)  # Field name made lowercase.
    warningcontent = models.CharField(db_column='WARNINGCONTENT', max_length=128)  # Field name made lowercase.
    isend = models.DecimalField(db_column='ISEND', max_digits=1, decimal_places=0)  # Field name made lowercase.
    warningid = models.CharField(db_column='WARNINGID', primary_key=True, max_length=32)  # Field name made lowercase.
    postion = models.DecimalField(db_column='POSTION', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'warnning_history'

#监测电站总数

class PowerStation(models.Model):
    systemtype = models.ForeignKey('SystemType', models.DO_NOTHING, db_column='systemType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'power_station'



