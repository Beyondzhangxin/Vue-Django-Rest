# coding=utf-8


# 根据distribution配置得到训练集样本，包括MAP算法下用于计算超参数的训练集，返回结果为N-by-d matrix，N为训练集样本数量，d为训练集维度/变量个数
import datetime
import json
import matlab.engine
import matlab
from pvmg.models import DataPvmgHistory
from spgs.models import DataSpgsHistory


def getSamples(gmmConfig):
    switch = {
        "SPGS": DataSpgsHistory,
        "PVMG": DataPvmgHistory,
    }
    start = datetime.datetime.strptime(gmmConfig['start_time'], "%Y-%m-%d %H:%M:%S")
    end = datetime.datetime.strptime(gmmConfig['end_time'], "%Y-%m-%d %H:%M:%S")
    yHyper_start = json.loads(gmmConfig.y_hyper).get('start_time')
    yHyper_end = json.loads(gmmConfig.y_hyper).get('end_time')
    yHyper_system = json.loads(gmmConfig.y_hyper).get('system')
    data={}
    try:
        system = switch[gmmConfig['system']]
        samples = system.objects.filter(datatime__range=(start, end))
        gmmConfig['varables'] = gmmConfig['varables'].lower()
        training_samples = samples.values_list(*tuple(json.loads(gmmConfig['varables'])))
        data['training_samples']=training_samples
        system = switch[yHyper_system]
        samples = system.objects.filter(datatime__range=(yHyper_start, yHyper_end))
        yHper_samples = samples.values_list(*tuple(json.loads(gmmConfig['varables'])))
        data['yHper_samples']=yHper_samples
        return data
    except Exception as e:
        print(e)
        return []


# 通过distribution配置获得distribution对象

def getDistribution(gmmConfig):
    engine = matlab.engine.start_matlab()
    data = getSamples(gmmConfig)
    Y = matlab.double(list(data['training_samples']))
    J = gmmConfig.j
    method = gmmConfig.method
    options = gmmConfig.options
    y_temp = json.loas(gmmConfig.y)
    y_list=[]
    if len(y_temp)>0:
        for x in y_temp:
            y_list.append(int(x.get('value')))
    y= matlab.double(y_list)
    y_hyper = matlab.double(list(data['yHper_samples']))
    period = gmmConfig.period

    if len(y_list)>0:
        if method=='EM':
            return engine.GMM_Distribution(Y,J,'EM',options,y)
        else:
            return engine.GMM_Distribution(Y,J,'MAP',options,y,y_hyper,period)
    else:
        if method=='EM':
            return engine.GMM_Distribution(Y,J,'EM',options)
        else:
            return engine.GMM_Distribution(Y,J,'MAP',options,y_hyper,period)
# 转置矩阵
def trans(m):
    return zip(*d)