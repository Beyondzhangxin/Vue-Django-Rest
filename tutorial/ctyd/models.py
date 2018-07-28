from django.db import models

# Create your models here.

#天井光伏发电系统数据表
class DataCtyd(models.Model):
    datatime = models.DateTimeField(db_column='DATATIME', primary_key=True)  # 数据记录时间
    systemcode = models.CharField(db_column='SYSTEMCODE', max_length=32)  # 系统型号
    edsugl = models.DecimalField(db_column='EDSUGL', max_digits=15, decimal_places=4, blank=True, null=True)  # 额定输出功率
    sclx = models.DecimalField(db_column='SCLX', max_digits=2, decimal_places=0, blank=True, null=True)  #
    rfdl = models.DecimalField(db_column='RFDL', max_digits=15, decimal_places=4, blank=True, null=True)  # 日发电量
    zyxsj = models.DecimalField(db_column='ZYXSJ', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    jnkqwd = models.DecimalField(db_column='JNKQWD', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    zldl1 = models.DecimalField(db_column='ZLDL1', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    zldl2 = models.DecimalField(db_column='ZLDL2', max_digits=15, decimal_places=4, blank=True, null=True)  # 直流电流
    zldl3 = models.DecimalField(db_column='ZLDL3', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    zldl4 = models.DecimalField(db_column='ZLDL4', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    zldy1 = models.DecimalField(db_column='ZLDY1', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    zldy2 = models.DecimalField(db_column='ZLDY2', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    zldy3 = models.DecimalField(db_column='ZLDY3', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    zldy4 = models.DecimalField(db_column='ZLDY4', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    zzlgl = models.DecimalField(db_column='ZZLGL', max_digits=15, decimal_places=4, blank=True, null=True)  # 总直流功率
    dl_a = models.DecimalField(db_column='DL_A', max_digits=15, decimal_places=4, blank=True, null=True)  # A相电压
    dl_b = models.DecimalField(db_column='DL_B', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dl_c = models.DecimalField(db_column='DL_C', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dy_a = models.DecimalField(db_column='DY_A', max_digits=15, decimal_places=4, blank=True, null=True)  # A相电流
    dy_b = models.DecimalField(db_column='DY_B', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dy_c = models.DecimalField(db_column='DY_C', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    zyggl = models.DecimalField(db_column='ZYGGL', max_digits=15, decimal_places=4, blank=True, null=True)  # 总有功功率
    dwpl = models.DecimalField(db_column='DWPL', max_digits=15, decimal_places=4, blank=True, null=True)  # 电网频率
    nbqxl = models.DecimalField(db_column='NBQXL', max_digits=15, decimal_places=4, blank=True, null=True)  # 逆变器效率
    zt = models.CharField(db_column='ZT', max_length=128, blank=True, null=True)  # Field name made lowercase.
    bj = models.CharField(db_column='BJ', max_length=128, blank=True, null=True)  # Field name made lowercase.
    work_zt = models.DecimalField(db_column='WORK_ZT', max_digits=2, decimal_places=0)  # Field name made lowercase.
    dataflag = models.DecimalField(db_column='DATAFLAG', max_digits=2, decimal_places=0)  # Field name made lowercase.
    zfdl = models.DecimalField(db_column='ZFDL', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    intzt = models.DecimalField(db_column='INTZT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'data_ctyd_buffer'
        unique_together = (('datatime', 'systemcode'),)


