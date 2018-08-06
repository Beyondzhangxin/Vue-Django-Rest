from django.db import models


# Create your models here.

# 多功能光伏电站系统
class DataSpgsBuffer(models.Model):
    datatime = models.CharField(db_column='DATATIME', primary_key=True, max_length=22)  # 数据录入时间
    systemcode = models.CharField(db_column='SYSTEMCODE', max_length=6)  # 系统型号
    nbqgl1 = models.DecimalField(db_column='NBQGL1', max_digits=15, decimal_places=4, blank=True, null=True)  # 逆变器功率
    nbqgl2 = models.DecimalField(db_column='NBQGL2', max_digits=15, decimal_places=4, blank=True,
                                 null=True)  # Field name made lowercase.
    nbqgl3 = models.DecimalField(db_column='NBQGL3', max_digits=15, decimal_places=4, blank=True,
                                 null=True)  # Field name made lowercase.
    nbqgl4 = models.DecimalField(db_column='NBQGL4', max_digits=15, decimal_places=4, blank=True,
                                 null=True)  # Field name made lowercase.
    nbqgl5 = models.DecimalField(db_column='NBQGL5', max_digits=15, decimal_places=4, blank=True,
                                 null=True)  # Field name made lowercase.
    nbqgl6 = models.DecimalField(db_column='NBQGL6', max_digits=15, decimal_places=4, blank=True,
                                 null=True)  # Field name made lowercase.
    nbqgl7 = models.DecimalField(db_column='NBQGL7', max_digits=15, decimal_places=4, blank=True,
                                 null=True)  # Field name made lowercase.
    nbqgl8 = models.DecimalField(db_column='NBQGL8', max_digits=15, decimal_places=4, blank=True,
                                 null=True)  # Field name made lowercase.
    nbqgl9 = models.DecimalField(db_column='NBQGL9', max_digits=15, decimal_places=4, blank=True,
                                 null=True)  # Field name made lowercase.
    nbqgl10 = models.DecimalField(db_column='NBQGL10', max_digits=15, decimal_places=4, blank=True,
                                  null=True)  # Field name made lowercase.
    fdzgl = models.DecimalField(db_column='FDZGL', max_digits=15, decimal_places=4, blank=True, null=True)  # 发电总功率
    ljfdl = models.DecimalField(db_column='LJFDL', max_digits=15, decimal_places=4, blank=True, null=True)  # 累计发电量
    drfdl = models.DecimalField(db_column='DRFDL', max_digits=15, decimal_places=4, blank=True, null=True)  # 当日发电量
    zjrl = models.DecimalField(db_column='ZJRL', max_digits=15, decimal_places=4, blank=True, null=True)  # 装机容量
    hjwd = models.DecimalField(db_column='HJWD', max_digits=15, decimal_places=4, blank=True, null=True)  # 环境温度
    fz = models.DecimalField(db_column='FZ', max_digits=15, decimal_places=4, blank=True, null=True)  # 辐照
    fs = models.DecimalField(db_column='FS', max_digits=15, decimal_places=4, blank=True, null=True)  # 风速
    fx = models.DecimalField(db_column='FX', max_digits=15, decimal_places=4, blank=True, null=True)  # 风向
    co2jp = models.DecimalField(db_column='CO2JP', max_digits=15, decimal_places=4, blank=True, null=True)  # 二氧化碳减排量
    bzmjp = models.DecimalField(db_column='BZMJP', max_digits=15, decimal_places=4, blank=True, null=True)  # 标准煤减排
    ntfcjp = models.DecimalField(db_column='NTFCJP', max_digits=15, decimal_places=4, blank=True, null=True)  # 年碳粉尘减排
    nojp = models.DecimalField(db_column='NOJP', max_digits=15, decimal_places=4, blank=True, null=True)  # 氮氧化合物减排
    h2ojp = models.DecimalField(db_column='H2OJP', max_digits=15, decimal_places=4, blank=True, null=True)  # 减少水消耗
    work_mode = models.DecimalField(db_column='WORK_MODE', max_digits=2, decimal_places=0, blank=True,
                                    null=True)  # 工作模式
    dataflag = models.DecimalField(db_column='DATAFLAG', max_digits=2, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'data_spgs_buffer'
        unique_together = (('datatime', 'systemcode'),)


class SpgsDay(models.Model):
    total_d = models.CharField(max_length=10, blank=True, null=True)
    systemtype = models.CharField(db_column='systemType', max_length=4, blank=True,
                                  null=True)  # Field name made lowercase.
    fdl_nbqjl1 = models.DecimalField(db_column='FDL_NBQJL1', max_digits=45, decimal_places=12, blank=True,
                                     null=True)  # Field name made lowercase.
    fdl_nbqjl2 = models.DecimalField(db_column='FDL_NBQJL2', max_digits=45, decimal_places=12, blank=True,
                                     null=True)  # Field name made lowercase.
    fdl_nbqjl3 = models.DecimalField(db_column='FDL_NBQJL3', max_digits=45, decimal_places=12, blank=True,
                                     null=True)  # Field name made lowercase.
    fdl_nbqjl4 = models.DecimalField(db_column='FDL_NBQJL4', max_digits=45, decimal_places=12, blank=True,
                                     null=True)  # Field name made lowercase.
    fdl_nbqjl5 = models.DecimalField(db_column='FDL_NBQJL5', max_digits=45, decimal_places=12, blank=True,
                                     null=True)  # Field name made lowercase.
    fdl_nbqjl6 = models.DecimalField(db_column='FDL_NBQJL6', max_digits=45, decimal_places=12, blank=True,
                                     null=True)  # Field name made lowercase.
    fdl_nbqjl7 = models.DecimalField(db_column='FDL_NBQJL7', max_digits=45, decimal_places=12, blank=True,
                                     null=True)  # Field name made lowercase.
    fdl_nbqjl8 = models.DecimalField(db_column='FDL_NBQJL8', max_digits=45, decimal_places=12, blank=True,
                                     null=True)  # Field name made lowercase.
    fdl_nbqjl9 = models.DecimalField(db_column='FDL_NBQJL9', max_digits=45, decimal_places=12, blank=True,
                                     null=True)  # Field name made lowercase.
    fdl_nbqjl10 = models.DecimalField(db_column='FDL_NBQJL10', max_digits=45, decimal_places=12, blank=True,
                                      null=True)  # Field name made lowercase.
    total_fdl = models.DecimalField(db_column='TOTAL_FDL', max_digits=54, decimal_places=12, blank=True,
                                    null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spgs_day'


class SpgsMinute(models.Model):
    total_d = models.CharField(max_length=21, blank=True, null=True)
    systemtype = models.CharField(db_column='systemType', max_length=4, blank=True,
                                  null=True)  # Field name made lowercase.
    fdl_nbqjl1 = models.DecimalField(db_column='FDL_NBQJL1', max_digits=45, decimal_places=12, blank=True,
                                     null=True)  # Field name made lowercase.
    fdl_nbqjl2 = models.DecimalField(db_column='FDL_NBQJL2', max_digits=45, decimal_places=12, blank=True,
                                     null=True)  # Field name made lowercase.
    fdl_nbqjl3 = models.DecimalField(db_column='FDL_NBQJL3', max_digits=45, decimal_places=12, blank=True,
                                     null=True)  # Field name made lowercase.
    fdl_nbqjl4 = models.DecimalField(db_column='FDL_NBQJL4', max_digits=45, decimal_places=12, blank=True,
                                     null=True)  # Field name made lowercase.
    fdl_nbqjl5 = models.DecimalField(db_column='FDL_NBQJL5', max_digits=45, decimal_places=12, blank=True,
                                     null=True)  # Field name made lowercase.
    fdl_nbqjl6 = models.DecimalField(db_column='FDL_NBQJL6', max_digits=45, decimal_places=12, blank=True,
                                     null=True)  # Field name made lowercase.
    fdl_nbqjl7 = models.DecimalField(db_column='FDL_NBQJL7', max_digits=45, decimal_places=12, blank=True,
                                     null=True)  # Field name made lowercase.
    fdl_nbqjl8 = models.DecimalField(db_column='FDL_NBQJL8', max_digits=45, decimal_places=12, blank=True,
                                     null=True)  # Field name made lowercase.
    fdl_nbqjl9 = models.DecimalField(db_column='FDL_NBQJL9', max_digits=45, decimal_places=12, blank=True,
                                     null=True)  # Field name made lowercase.
    fdl_nbqjl10 = models.DecimalField(db_column='FDL_NBQJL10', max_digits=45, decimal_places=12, blank=True,
                                      null=True)  # Field name made lowercase.
    total_fdl = models.DecimalField(db_column='TOTAL_FDL', max_digits=54, decimal_places=12, blank=True,
                                    null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spgs_minute'


class SpgsMonth(models.Model):
    total_m = models.CharField(max_length=7, blank=True, null=True)
    systemtype = models.CharField(db_column='systemType', max_length=4, blank=True,
                                  null=True)  # Field name made lowercase.
    fdl_nbqjl1 = models.DecimalField(db_column='FDL_NBQJL1', max_digits=65, decimal_places=12, blank=True,
                                     null=True)  # Field name made lowercase.
    fdl_nbqjl2 = models.DecimalField(db_column='FDL_NBQJL2', max_digits=65, decimal_places=12, blank=True,
                                     null=True)  # Field name made lowercase.
    fdl_nbqjl3 = models.DecimalField(db_column='FDL_NBQJL3', max_digits=65, decimal_places=12, blank=True,
                                     null=True)  # Field name made lowercase.
    fdl_nbqjl4 = models.DecimalField(db_column='FDL_NBQJL4', max_digits=65, decimal_places=12, blank=True,
                                     null=True)  # Field name made lowercase.
    fdl_nbqjl5 = models.DecimalField(db_column='FDL_NBQJL5', max_digits=65, decimal_places=12, blank=True,
                                     null=True)  # Field name made lowercase.
    fdl_nbqjl6 = models.DecimalField(db_column='FDL_NBQJL6', max_digits=65, decimal_places=12, blank=True,
                                     null=True)  # Field name made lowercase.
    fdl_nbqjl7 = models.DecimalField(db_column='FDL_NBQJL7', max_digits=65, decimal_places=12, blank=True,
                                     null=True)  # Field name made lowercase.
    fdl_nbqjl8 = models.DecimalField(db_column='FDL_NBQJL8', max_digits=65, decimal_places=12, blank=True,
                                     null=True)  # Field name made lowercase.
    fdl_nbqjl9 = models.DecimalField(db_column='FDL_NBQJL9', max_digits=65, decimal_places=12, blank=True,
                                     null=True)  # Field name made lowercase.
    fdl_nbqjl10 = models.DecimalField(db_column='FDL_NBQJL10', max_digits=65, decimal_places=12, blank=True,
                                      null=True)  # Field name made lowercase.
    total_fdl = models.DecimalField(max_digits=65, decimal_places=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spgs_month'




class SpgsTotal(models.Model):
    systemtype = models.CharField(db_column='systemType', max_length=4, blank=True,
                                  null=True)  # Field name made lowercase.
    total_fdl = models.DecimalField(max_digits=65, decimal_places=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spgs_total'
