# coding=utf-8


# 根据distribution配置得到训练集样本，包括MAP算法下用于计算超参数的训练集，返回结果为N-by-d matrix，N为训练集样本数量，d为训练集维度/变量个数
import datetime
import json
import matlab.engine
import matlab
from pvmg.models import DataPvmgHistory
from spgs.models import DataSpgsHistory
import numpy as np

from .GMM_Distribution import GMM_distribution


def getSamples(gmmConfig):
    switch = {
        "SPGS": DataSpgsHistory,
        "PVMG": DataPvmgHistory,
    }
    start = datetime.datetime.strptime(gmmConfig.start_time, "%Y-%m-%d %H:%M:%S")
    end = datetime.datetime.strptime(gmmConfig.end_time, "%Y-%m-%d %H:%M:%S")
    yHyper_start = json.loads(gmmConfig.y_hyper).get('start_time')
    if not yHyper_start=='':
        yHyper_start=datetime.datetime.strptime(yHyper_start, "%Y-%m-%dT%H:%M:%S.%fZ")
    yHyper_end = json.loads(gmmConfig.y_hyper).get('end_time')
    if not yHyper_end=='':
        yHyper_end = datetime.datetime.strptime(yHyper_end,"%Y-%m-%dT%H:%M:%S.%fZ")
    yHyper_system = json.loads(gmmConfig.y_hyper).get('system')
    data={}
    try:
        system = switch[gmmConfig.system]
        samples = system.objects.filter(datatime__range=(start, end))
        gmmConfig.varables = gmmConfig.varables.lower()
        training_samples = samples.values_list(*tuple(json.loads(gmmConfig.varables)))
        data['training_samples']=training_samples
        if not yHyper_system=='':
            system = switch[yHyper_system]
            samples = system.objects.filter(datatime__range=(yHyper_start, yHyper_end))
            yHper_samples = samples.values_list(*tuple(json.loads(gmmConfig.varables)))
            data['yHper_samples']=yHper_samples
        else:
            data['yHper_samples']=[]
        return data
    except Exception as e:
        print(e)
        return []


# 通过distribution配置获得distribution对象

def getDistribution(gmmConfig):
    # engine = matlab.engine.start_matlab()
    data = getSamples(gmmConfig)
    Y = np.array(data['training_samples']).T[0]
    max=np.max(Y)
    min=np.min(Y)
    J =  gmmConfig.j
    method = gmmConfig.method
    options = gmmConfig.options
    y_temp = json.loads(gmmConfig.y)
    y_list=[]
    if len(y_temp)>0:
        for x in y_temp:
            y_list.append(int(x.get('value')))
    y= np.array(y_list)
    y_hyper = np.array(list(data['yHper_samples']))
    period = gmmConfig.period
    len_y = len(y_hyper)
    y_hyper =y_hyper[0:int(len_y/50)*50]
    if len(y_list)>0:
        if method=='EM':
            return {'gmm':GMM_distribution(Y,J,'EM',options,y),'max':max,'min':min}
        else:
            return {'gmm':GMM_distribution(Y,J,'MAP',options,y,y_hyper,period),'max':max,'min':min}
    else:
        if method=='EM':
            return {'gmm':GMM_distribution(Y,J,'EM',options),'max':max,'min':min}
        else:
            return {'gmm':GMM_distribution(Y,J,'MAP',options,y_hyper,period),'max':max,'min':min}

def getDistribution_echart(distribution):
    pass




# 转置矩阵
def trans(m):
    return zip(*d)

# 根据输入X输出GMM分布数据Y

