# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Pvdata(models.Model):
    cityid = models.CharField(db_column='CityID', max_length=6)  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='UpdateTime')  # Field name made lowercase.
    pcbid = models.IntegerField(db_column='PcbID')  # Field name made lowercase.
    channelid = models.IntegerField(db_column='ChannelID')  # Field name made lowercase.
    batid = models.IntegerField(db_column='BatID', blank=True, null=True)  # Field name made lowercase.
    u = models.FloatField(db_column='U', blank=True, null=True)  # Field name made lowercase.
    i = models.FloatField(db_column='I', blank=True, null=True)  # Field name made lowercase.
    p = models.FloatField(db_column='P', blank=True, null=True)  # Field name made lowercase.
    t = models.FloatField(db_column='T', blank=True, null=True)  # Field name made lowercase.
    v12 = models.FloatField(db_column='V12', blank=True, null=True)  # Field name made lowercase.
    v5 = models.FloatField(db_column='V5', blank=True, null=True)  # Field name made lowercase.
    devicetime = models.CharField(db_column='DeviceTime', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pcor = models.FloatField(db_column='Pcor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pvdata'
        unique_together = (('cityid', 'updatetime', 'pcbid', 'channelid'),)