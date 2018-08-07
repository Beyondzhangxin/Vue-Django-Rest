from django.db import models

# Create your models here.
# 图书馆微电网系统数据
class DataPvmgBuffer(models.Model):
    datatime = models.DateTimeField(db_column='DATATIME', primary_key=True)  # 数据录入时间
    systemcode = models.CharField(db_column='SYSTEMCODE', max_length=32)  # 系统型号
    nbqgl1 = models.DecimalField(db_column='NBQGL1', max_digits=15, decimal_places=4, blank=True, null=True)  # 逆变器1功率
    nbqgl2 = models.DecimalField(db_column='NBQGL2', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    nbqgl3 = models.DecimalField(db_column='NBQGL3', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    nbqgl4 = models.DecimalField(db_column='NBQGL4', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    nbqgl5 = models.DecimalField(db_column='NBQGL5', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    nbqgl6 = models.DecimalField(db_column='NBQGL6', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    nbqgl7 = models.DecimalField(db_column='NBQGL7', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    nbqgl8 = models.DecimalField(db_column='NBQGL8', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    nbqgl9 = models.DecimalField(db_column='NBQGL9', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    fdzgl = models.DecimalField(db_column='FDZGL', max_digits=15, decimal_places=4, blank=True, null=True)  # 发电总功率
    ljfdl = models.DecimalField(db_column='LJFDL', max_digits=15, decimal_places=4, blank=True, null=True)  # 累计发电量
    jrfdl = models.DecimalField(db_column='JRFDL', max_digits=15, decimal_places=4, blank=True, null=True)  # 今日发电量
    hjwd = models.DecimalField(db_column='HJWD', max_digits=15, decimal_places=4, blank=True, null=True)  # 环境温度
    rz = models.DecimalField(db_column='RZ', max_digits=15, decimal_places=4, blank=True, null=True)  # 日照
    fs = models.DecimalField(db_column='FS', max_digits=15, decimal_places=4, blank=True, null=True)  # 风速
    fx = models.DecimalField(db_column='FX', max_digits=15, decimal_places=4, blank=True, null=True)  # 风向
    co2jp = models.DecimalField(db_column='CO2JP', max_digits=15, decimal_places=4, blank=True, null=True)  # 二氧化碳减排量
    fzhdl = models.DecimalField(db_column='FZHDL', max_digits=15, decimal_places=4, blank=True, null=True)  # 负载耗电量
    fzzgl = models.DecimalField(db_column='FZZGL', max_digits=15, decimal_places=4, blank=True, null=True)  # 负载总功率
    llxyggl = models.DecimalField(db_column='LLXYGGL', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    llxwggl = models.DecimalField(db_column='LLXWGGL', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pcsscgl = models.DecimalField(db_column='PCSSCGL', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pcspl = models.DecimalField(db_column='PCSPL', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    lizdy = models.DecimalField(db_column='LIZDY', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    lizdl = models.DecimalField(db_column='LIZDL', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    lisoc = models.DecimalField(db_column='LISOC', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    lisoh = models.DecimalField(db_column='LISOH', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    work_mode = models.DecimalField(db_column='WORK_MODE', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    work_zt = models.CharField(db_column='WORK_ZT', max_length=128, blank=True, null=True)  # Field name made lowercase.
    bj = models.CharField(db_column='BJ', max_length=128, blank=True, null=True)  # Field name made lowercase.
    dataflag = models.DecimalField(db_column='DATAFLAG', max_digits=2, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'data_pvmg_buffer'
        unique_together = (('datatime', 'systemcode'),)
