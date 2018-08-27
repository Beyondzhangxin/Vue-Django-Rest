from django.db import models

# Create your models here.
# 此表保存GMM_distribution配置
class GmmConfig(models.Model):
    name = models.CharField(max_length=255)#配置名称
    system = models.CharField(max_length=255)#数据库系统，对应systemType
    varables = models.CharField(max_length=1024)#选择的字段
    start_time = models.CharField(max_length=255, blank=True, null=True)#样本起始时间
    end_time = models.CharField(max_length=255, blank=True, null=True)#样本结束时间
    j = models.IntegerField(db_column='J')  # 高斯个数，int
    method = models.CharField(max_length=255)#方法选择EM或者MAP
    options = models.CharField(max_length=255)#输出选择 maginal或者joint或者conditional
    y = models.TextField(blank=True, null=True)#(选择输入) 条件分布的给定值, 1-by-d vector, 每一元素为对应变量的给定值，目标变量处的给定值设为0，
    period = models.IntegerField(blank=True, null=True)#(选择输入) MAP算法下用于计算超参数的段数划分，int，即将Y_hyper以period为长度，分成若干小训练集，从而形成多组GMM参数，进而计算超参数
    y_hyper = models.TextField(db_column='Y_hyper', blank=True, null=True)  # (选择输入) MAP算法下用于计算超参数的训练集，N-by-d matrix，N为训练集样本数量，d为训练集维度/变量个数

    class Meta:
        managed = False
        db_table = 'GMM_config'
