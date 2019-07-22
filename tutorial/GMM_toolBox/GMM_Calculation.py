from __future__ import absolute_import, unicode_literals

import datetime
import json
import random
import time
from threading import Thread

import pika
from clickhouse_driver import Client
from numpy import unicode
from sklearn.mixture import GaussianMixture
import math
import copy
import numpy as np
import scipy.integrate

# from tutorial.GMM_toolBox import functional
# from GMM_toolBox import functional
# import GMM_distribution

import fit_MAP, fit_EM, functional

from send import send_data_to_clickhouse

from receive import save_data_to_clickhouse


def byteify(input, encoding='utf-8'):
    if isinstance(input, dict):
        return {byteify(key): byteify(value) for key, value in input.items()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, str):
        return input.encode(encoding)
    else:
        return input


# 模拟实时数据
def mock_data_from_clickhouse(period):
    def run1():
        send_data_to_clickhouse(period)

    def run2():
        save_data_to_clickhouse()

    t1 = Thread(target=run1, args=())
    t1.setDaemon(False)
    t1.start()
    t2 = Thread(target=run2, args=())
    t2.setDaemon(False)
    t2.start()


def siemense_cal(msg, rbmq, ret_queue):
    data = json.loads(msg)
    client = Client(host='10.112.10.24')
    inf = 0
    sup = 300
    x_length = 100
    response = {}
    flag = {'cal': True}
    stop_queue = ret_queue.replace('count', 'stop')

    def run():
        def callback(ch, method, properties, body):
            data = bytes.decode(body)
            flag['cal'] = False
            ch.connection.close()

        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='10.112.10.24'))
        channel = connection.channel()
        channel.queue_declare(queue=stop_queue)
        channel.basic_consume(callback,
                              queue=stop_queue,
                              no_ack=True)
        channel.start_consuming()

    t = Thread(target=run, args=(flag))
    t.setDaemon(True)
    t.start()

    with open('GMMConfig.json', 'r', encoding='utf-8') as f:
        data_config = json.load(f)
    if data['selectedmethod'] == 'em':
        if data['selectedout'] == 'pdf':
            response['y'] = []
            if not data['real_time']:
                for device in data['device']:
                    deviceObj = None
                    factory_data = []
                    search_list = []
                    desc_list = []
                    for obj in data_config['GMMObjs']:
                        if obj['GMMObj']['guid'] == device['guid']:
                            deviceObj = obj['GMMObj']
                            break
                    for factory in device['factories']:
                        factoryObj = None
                        for factoryCfgObj in deviceObj['SubObjs']:
                            if factoryCfgObj['guid'] == factory['guid']:
                                factoryObj = factoryCfgObj
                        search_list.append(factoryObj['note'])
                        desc_list.append(factoryObj['desc'])
                    UTC_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
                    start_time = data['datefrom']
                    end_time = data['dateto']
                    search_sql = "select " + ','.join(
                        search_list) + " from siemense.siemense_objlist where TimeStamp between '" + str(
                        datetime.datetime.strptime(start_time, UTC_FORMAT)) + "' AND '" + str(
                        datetime.datetime.strptime(end_time, UTC_FORMAT)) + "'"
                    factory_data = client.execute(search_sql)
                    power = np.array(factory_data)
                    gmm = GMM_distribution(
                        power, 3, 'EM', 'marginal')['GMM']

                    x = np.linspace(inf, sup, x_length)
                    response['x'] = x.tolist()
                    pdf = {}
                    for index in range(len(gmm)):
                        log_pdf = gmm[index].score_samples(x[:, np.newaxis])
                        pdf[desc_list[index]] = list(np.exp(log_pdf))
                    response['y'].append({
                        'name': deviceObj['desc'],
                        'data': pdf
                    })
                rbmq.sendMsg(json.dumps(response), ret_queue)
            else:
                period = data['period']

                def run():
                    response['y'] = []
                    for device in data['device']:
                        deviceObj = None
                        factory_data = []
                        search_list = []
                        desc_list = []
                        for obj in data_config['GMMObjs']:
                            if obj['GMMObj']['guid'] == device['guid']:
                                deviceObj = obj['GMMObj']
                                break
                        for factory in device['factories']:
                            factoryObj = None
                            for factoryCfgObj in deviceObj['SubObjs']:
                                if factoryCfgObj['guid'] == factory['guid']:
                                    factoryObj = factoryCfgObj
                            search_list.append(factoryObj['note'])
                            desc_list.append(factoryObj['desc'])

                        start_time = datetime.datetime.strftime(
                            datetime.datetime.now() - datetime.timedelta(seconds=period * 3600), "%Y-%m-%d %H:%M:%S")
                        end_time = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")
                        search_sql = "select " + ','.join(
                            search_list) + " from siemense.siemense_objlist where TimeStamp between '" \
                                     + start_time + "' AND '" + end_time + "'"
                        factory_data = client.execute(search_sql)
                        power = np.array(factory_data)
                        gmm = GMM_distribution(
                            power, 3, 'EM', 'marginal')['GMM']

                        x = np.linspace(inf, sup, x_length)
                        response['x'] = x.tolist()
                        pdf = {}
                        for index in range(len(gmm)):
                            log_pdf = gmm[index].score_samples(x[:, np.newaxis])
                            pdf[desc_list[index]] = list(np.exp(log_pdf))
                        response['y'].append({
                            'name': deviceObj['desc'],
                            'data': pdf
                        })
                    rbmq.sendMsg(json.dumps(response), ret_queue)

                while flag['cal']:
                    run()

        if data['selectedout'] == 'cdf':
            response['y'] = []
            if not data['real_time']:
                for device in data['device']:
                    deviceObj = None
                    factory_data = []
                    search_list = []
                    desc_list = []
                    for obj in data_config['GMMObjs']:
                        if obj['GMMObj']['guid'] == device['guid']:
                            deviceObj = obj['GMMObj']
                            break
                    for factory in device['factories']:
                        factoryObj = None
                        for factoryCfgObj in deviceObj['SubObjs']:
                            if factoryCfgObj['guid'] == factory['guid']:
                                factoryObj = factoryCfgObj
                        search_list.append(factoryObj['note'])
                        desc_list.append(factoryObj['desc'])
                    UTC_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
                    start_time = data['datefrom']
                    end_time = data['dateto']
                    search_sql = "select " + ','.join(
                        search_list) + " from siemense.siemense_objlist where TimeStamp between '" + str(
                        datetime.datetime.strptime(start_time, UTC_FORMAT)) + "' AND '" + str(
                        datetime.datetime.strptime(end_time, UTC_FORMAT)) + "'"
                    factory_data = client.execute(search_sql)

                    power = np.array(factory_data)
                    gmm = GMM_distribution(
                        power, 3, 'EM', 'marginal')['GMM']

                    x = np.linspace(inf, sup, x_length)
                    response['x'] = x.tolist()
                    cdf = {}
                    for index in range(len(gmm)):
                        cdf_ = list()
                        for x_ in x:
                            y_ = scipy.integrate.quad(lambda m: np.exp(gmm[index].score_samples(np.array([[m]]))),
                                                      -np.inf,
                                                      x_)
                            cdf_.append(y_[0])
                        cdf[desc_list[index]] = cdf_
                    response['y'].append({
                        'name': deviceObj['desc'],
                        'data': cdf
                    })
                rbmq.sendMsg(json.dumps(response), ret_queue)
            else:
                period = data['period']
                response['y'] = []

                def run():
                    for device in data['device']:
                        deviceObj = None
                        factory_data = []
                        search_list = []
                        desc_list = []
                        for obj in data_config['GMMObjs']:
                            if obj['GMMObj']['guid'] == device['guid']:
                                deviceObj = obj['GMMObj']
                                break
                        for factory in device['factories']:
                            factoryObj = None
                            for factoryCfgObj in deviceObj['SubObjs']:
                                if factoryCfgObj['guid'] == factory['guid']:
                                    factoryObj = factoryCfgObj
                            search_list.append(factoryObj['note'])
                            desc_list.append(factoryObj['desc'])
                        start_time = datetime.datetime.strftime(
                            datetime.datetime.now() - datetime.timedelta(seconds=period * 3600), "%Y-%m-%d %H:%M:%S")
                        end_time = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")
                        search_sql = "select " + ','.join(
                            search_list) + " from siemense.siemense_objlist where TimeStamp between '" \
                                     + start_time + "' AND '" + end_time + "'"
                        factory_data = client.execute(search_sql)

                        power = np.array(factory_data)
                        gmm = GMM_distribution(
                            power, 3, 'EM', 'marginal')['GMM']

                        x = np.linspace(inf, sup, x_length)
                        response['x'] = x.tolist()
                        cdf = {}
                        for index in range(len(gmm)):
                            cdf_ = list()
                            for x_ in x:
                                y_ = scipy.integrate.quad(lambda m: np.exp(gmm[index].score_samples(np.array([[m]]))),
                                                          -np.inf,
                                                          x_)
                                cdf_.append(y_[0])
                            cdf[desc_list[index]] = cdf_
                        response['y'].append({
                            'name': deviceObj['desc'],
                            'data': cdf
                        })
                    rbmq.sendMsg(json.dumps(response), ret_queue)

                while flag['cal']:
                    run()

        if data['selectedout'] == 'kl':

            if not data['real_time']:
                devices = []
                axis = []
                t1 = datetime.datetime.now()
                for device in data['device']:
                    deviceObj = None
                    factory_data = []
                    search_list = []
                    for obj in data_config['GMMObjs']:
                        if obj['GMMObj']['guid'] == device['guid']:
                            deviceObj = obj['GMMObj']
                            break
                    for factory in device['factories']:
                        factoryObj = None
                        for factoryCfgObj in deviceObj['SubObjs']:
                            if factoryCfgObj['guid'] == factory['guid']:
                                factoryObj = factoryCfgObj
                        search_list.append(factoryObj['note'])
                    UTC_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
                    start_time = data['datefrom']
                    end_time = data['dateto']
                    search_sql = "select " + ','.join(
                        search_list) + " from siemense.siemense_objlist where TimeStamp between '" + str(
                        datetime.datetime.strptime(start_time, UTC_FORMAT)) + "' AND '" + str(
                        datetime.datetime.strptime(end_time, UTC_FORMAT)) + "'"
                    factory_data = client.execute(search_sql)
                    devices.append(factory_data)
                    axis.append(device['name'])
                matrix = KL_martrices(devices, 'em')
                matrix_3d = list()
                for i in range(len(matrix)):
                    for j in range(len(matrix[i])):
                        matrix_3d.append([axis[i], axis[j], matrix[i][j]])
                t2 = datetime.datetime.now()
                print('all ', t2 - t1)
                response['x'] = axis
                response['y'] = axis
                response['data'] = matrix_3d
                rbmq.sendMsg(json.dumps(response), ret_queue)
            else:
                period = data['period']

                def run():
                    devices = []
                    axis = []
                    for device in data['device']:
                        deviceObj = None
                        factory_data = []
                        search_list = []
                        for obj in data_config['GMMObjs']:
                            if obj['GMMObj']['guid'] == device['guid']:
                                deviceObj = obj['GMMObj']
                                break
                        for factory in device['factories']:
                            factoryObj = None
                            for factoryCfgObj in deviceObj['SubObjs']:
                                if factoryCfgObj['guid'] == factory['guid']:
                                    factoryObj = factoryCfgObj
                            search_list.append(factoryObj['note'])
                        start_time = datetime.datetime.strftime(
                            datetime.datetime.now() - datetime.timedelta(seconds=period * 3600), "%Y-%m-%d %H:%M:%S")
                        end_time = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")
                        search_sql = "select " + ','.join(
                            search_list) + " from siemense.siemense_objlist where TimeStamp between '" \
                                     + start_time + "' AND '" + end_time + "'"
                        factory_data = client.execute(search_sql)
                        devices.append(factory_data)
                        axis.append(device['name'])
                    matrix = KL_martrices(devices, 'em')
                    matrix_3d = list()
                    for i in range(len(matrix)):
                        for j in range(len(matrix[i])):
                            matrix_3d.append([axis[i], axis[j], matrix[i][j]])
                    response['x'] = axis
                    response['y'] = axis
                    response['data'] = matrix_3d
                    rbmq.sendMsg(json.dumps(response), ret_queue)

                while flag['cal']:
                    run()
        if data['selectedout'] == 'linear':
            response['y'] = []
            if not data['real_time']:
                for device in data['device']:
                    deviceObj = None
                    factory_data = []
                    search_list = []
                    desc_list = []
                    for obj in data_config['GMMObjs']:
                        if obj['GMMObj']['guid'] == device['guid']:
                            deviceObj = obj['GMMObj']
                            break
                    for factory in device['factories']:
                        factoryObj = None
                        for factoryCfgObj in deviceObj['SubObjs']:
                            if factoryCfgObj['guid'] == factory['guid']:
                                factoryObj = factoryCfgObj
                        search_list.append(factoryObj['note'])
                        desc_list.append(factoryObj['desc'])
                    UTC_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
                    start_time = data['datefrom']
                    end_time = data['dateto']
                    search_sql = "select " + ','.join(
                        search_list) + " from siemense.siemense_objlist where TimeStamp between '" + str(
                        datetime.datetime.strptime(start_time, UTC_FORMAT)) + "' AND '" + str(
                        datetime.datetime.strptime(end_time, UTC_FORMAT)) + "'"
                    factory_data = client.execute(search_sql)
                    power = np.array(factory_data)
                    gmm = GMM_distribution(
                        power, 3, 'EM', 'marginal')['GMM']
                    a = np.array([float(data['linear_a'])])
                    b = np.array([float(data['linear_b'])])
                    x = np.linspace(inf, sup, x_length)
                    response['x'] = x.tolist()
                    pdf = {}
                    for index in range(len(gmm)):
                        linear_gmm = GMM_calculation(gmm[index], 'linear', A=a, b=b)['linear_GMM']
                        log_pdf = linear_gmm.score_samples(x[:, np.newaxis])
                        pdf[desc_list[index]] = list(np.exp(log_pdf))
                    response['y'].append({
                        'name': deviceObj['desc'],
                        'data': pdf
                    })
                rbmq.sendMsg(json.dumps(response), ret_queue)
            else:
                period = data['period']

                def run():
                    response['y'] = []
                    for device in data['device']:
                        deviceObj = None
                        factory_data = []
                        search_list = []
                        desc_list = []
                        for obj in data_config['GMMObjs']:
                            if obj['GMMObj']['guid'] == device['guid']:
                                deviceObj = obj['GMMObj']
                                break
                        for factory in device['factories']:
                            factoryObj = None
                            for factoryCfgObj in deviceObj['SubObjs']:
                                if factoryCfgObj['guid'] == factory['guid']:
                                    factoryObj = factoryCfgObj
                            search_list.append(factoryObj['note'])
                            desc_list.append(factoryObj['desc'])

                        start_time = datetime.datetime.strftime(
                            datetime.datetime.now() - datetime.timedelta(seconds=period * 3600), "%Y-%m-%d %H:%M:%S")
                        end_time = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")
                        search_sql = "select " + ','.join(
                            search_list) + " from siemense.siemense_objlist where TimeStamp between '" \
                                     + start_time + "' AND '" + end_time + "'"
                        factory_data = client.execute(search_sql)
                        power = np.array(factory_data)
                        gmm = GMM_distribution(
                            power, 3, 'EM', 'marginal')['GMM']
                        a = np.array([float(data['linear_a'])])
                        b = np.array([float(data['linear_b'])])
                        x = np.linspace(inf, sup, x_length)
                        response['x'] = x.tolist()
                        pdf = {}
                        for index in range(len(gmm)):
                            linear_gmm = GMM_calculation(gmm[index], 'linear', A=a, b=b)
                            log_pdf = linear_gmm['linear_GMM'].score_samples(x[:, np.newaxis])
                            pdf[desc_list[index]] = list(np.exp(log_pdf))
                        response['y'].append({
                            'name': deviceObj['desc'],
                            'data': pdf
                        })
                    rbmq.sendMsg(json.dumps(response), ret_queue)

                while flag['cal']:
                    run()


def KL_martrices(devices, method):
    length = len(devices)
    Gmms_matrix = list()
    KL_matrix = np.zeros((length, length), dtype=np.float64)
    t1 = datetime.datetime.now()

    if method == 'em':
        for device in devices:
            print(len(device))
            Gmms_matrix.append(GMM_distribution(
                np.array(device), 3, 'EM', 'joint')['GMM'])
    t2 = datetime.datetime.now()
    print('gmmtime  ', t2 - t1)
    for i in range(length):
        for j in range(i + 1, length):
            KL_matrix[i, j] = GMM_calculation(Gmms_matrix[i], 'KL', gmm_extra=Gmms_matrix[j])['KL']
    KL_matrix = KL_matrix.T + KL_matrix
    np.fill_diagonal(KL_matrix, 0)
    return KL_matrix.tolist()


def siemense_cal1(msg, rbmq, ret_queue):
    data = byteify(json.loads(msg, encoding='utf-8'))
    client = Client(host='10.112.10.24')
    inf = 0
    sup = 300
    x_length = 100
    response = {}

    send_data_to_clickhouse(300)

    with open('GMMConfig.json', 'r') as f:
        data_config = json.load(f)

    if data['method'] == 'em':
        if data['output'] == 'pdf':
            response['y'] = []
            for device in data['device']:
                deviceObj = None
                factory_data = []
                search_list = []
                for obj in data_config['GMMObjs']:
                    if obj['GMMObj']['guid'] == device['guid']:
                        deviceObj = obj
                        return
                for factory in device['factories']:
                    factoryObj = None
                    for factoryCfgObj in deviceObj['SubObjs']:
                        if factoryCfgObj['guid'] == factory['guid']:
                            factoryObj = factoryCfgObj
                    search_list.append(factoryObj['note'])
                UTC_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
                if data['real_time']:
                    start_time = data['datefrom']
                    end_time = data['dateto']
                    search_sql = "select " + ','.join(
                        search_list) + " from siemense.siemense_objlist where TimeStamp between '" + str(
                        datetime.datetime.strptime(start_time, UTC_FORMAT)) + "' AND '" + str(
                        datetime.datetime.strptime(end_time, UTC_FORMAT)) + "'"
                    factory_data = client.execute(search_sql)
                else:
                    period = data['period']

                    start_time = str(datetime.datetime.now() - datetime.timedelta(seconds=period * 3600))
                    end_time = str(datetime.datetime.now())
                    search_sql = "select " + ','.join(
                        search_list) + " from siemense.siemense_objlist where TimeStamp between '" \
                                 + start_time + "' AND '" + end_time + "'"
                    factory_data = client.execute(search_sql)
                power = np.array(factory_data)
                gmm = GMM_distribution(
                    power, 3, 'EM', 'marginal')['GMM']

                x = np.linspace(data['inf'], data['sup'], data['x_length'])
                log_pdf = gmm.score_samples(x[:, np.newaxis])
                pdf = np.exp(log_pdf)
                response['x'] = x.tolist()
                response['y'].append({
                    'name': deviceObj['desc'],
                    'data': pdf.tolist()
                })
            rbmq.sendMsg(json.dumps(response), ret_queue)
        if data['output'] == 'cdf':

            response['y'] = []
            for device in data['device']:
                deviceObj = None
                factory_data = []
                search_list = []
                for obj in data_config['GMMObjs']:
                    if obj['GMMObj']['guid'] == device['guid']:
                        deviceObj = obj
                        return
                for factory in device['factories']:
                    factoryObj = None
                    for factoryCfgObj in deviceObj['SubObjs']:
                        if factoryCfgObj['guid'] == factory['guid']:
                            factoryObj = factoryCfgObj
                    search_list.append(factoryObj['note'])
                UTC_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
                if data['real_time']:
                    start_time = data['datefrom']
                    end_time = data['dateto']
                    search_sql = "select " + ','.join(
                        search_list) + " from siemense.siemense_objlist where TimeStamp between '" + str(
                        datetime.datetime.strptime(start_time, UTC_FORMAT)) + "' AND '" + str(
                        datetime.datetime.strptime(end_time, UTC_FORMAT)) + "'"
                    factory_data = client.execute(search_sql)
                else:
                    period = data['period']

                    start_time = str(datetime.datetime.now() - datetime.timedelta(seconds=period * 3600))
                    end_time = str(datetime.datetime.now())
                    search_sql = "select " + ','.join(
                        search_list) + " from siemense.siemense_objlist where TimeStamp between '" \
                                 + start_time + "' AND '" + end_time + "'"
                    factory_data = client.execute(search_sql)
                power = np.array(factory_data)
                cdf = list()
                gmm = GMM_distribution(
                    power, 3, 'EM', 'marginal')['GMM']

                x = np.linspace(data['inf'], data['sup'], data['x_length'])
                for x_ in x:
                    y_ = scipy.integrate.quad(lambda m: np.exp(gmm.score_samples(np.array([[m]]))), -np.inf, x_)
                    cdf.append(y_[0])
                log_pdf = gmm.score_samples(x[:, np.newaxis])
                pdf = np.exp(log_pdf)
                response['x'] = x.tolist()
                response['y'].append({
                    'name': deviceObj['desc'],
                    'data': pdf.tolist()
                })
            rbmq.sendMsg(json.dumps(response), ret_queue)
        if data['output'] == 'kl':
            devices = []
            for device in data['device']:
                deviceObj = None
                factory_data = []
                search_list = []
                for obj in data_config['GMMObjs']:
                    if obj['GMMObj']['guid'] == device['guid']:
                        deviceObj = obj
                        return
                for factory in device['factories']:
                    factoryObj = None
                    for factoryCfgObj in deviceObj['SubObjs']:
                        if factoryCfgObj['guid'] == factory['guid']:
                            factoryObj = factoryCfgObj
                    search_list.append(factoryObj['note'])
                UTC_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
                if data['real_time']:
                    start_time = data['datefrom']
                    end_time = data['dateto']
                    search_sql = "select " + ','.join(
                        search_list) + " from siemense.siemense_objlist where TimeStamp between '" + str(
                        datetime.datetime.strptime(start_time, UTC_FORMAT)) + "' AND '" + str(
                        datetime.datetime.strptime(end_time, UTC_FORMAT)) + "'"
                    factory_data = client.execute(search_sql)
                else:
                    period = data['period']

                    start_time = str(datetime.datetime.now() - datetime.timedelta(seconds=period * 3600))
                    end_time = str(datetime.datetime.now())
                    search_sql = "select " + ','.join(
                        search_list) + " from siemense.siemense_objlist where TimeStamp between '" \
                                 + start_time + "' AND '" + end_time + "'"
                    factory_data = client.execute(search_sql)
                devices.append(factory_data)
            matrix = KL_martrices(devices, 'em')
            matrix_3d = list()
            axis = []
            for i in range(len(matrix)):
                axis.append(i)
                for j in range(len(matrix[i])):
                    matrix_3d.append([i, j, matrix[i][j]])
            response['x'] = axis
            response['y'] = axis
            response['data'] = matrix_3d
            rbmq.sendMsg(json.dumps(response), ret_queue)


def GMM_calculation(gmm: GaussianMixture, options, **kwargs):
    """
    计算GMM周边
    功能：本函数包含计算概率分布周边的功能
        a) 计算在给定点的概率密度函数值
        b) 计算在给定点的积累概率函数值
        c) 计算任意两个分布之间的KL散度
        d) 计算任意两个边际分布之间的RMSE
        e) 计算随机变量的线性函数的分布
    :param gmm: GMM模型
    :param options: 输出选择,char
        1）'pdf': 计算在给定点的概率密度函数值
        2）'cdf': 计算在给定点的积累概率函数值
        3) 'quantile': 计算输入分布的10%-100%分位数
        4）'KL':  计算任意两个分布之间的KL散度
        5）'RMSE':  计算任意两个分布之间的RMSE散度
        6）'linear':  计算随机变量的线性函数的分布
    :param kwargs:
        1) y: 计算pdf或cdf时的给定点,1-by-d numpy array (2 dimensions)
        2) gmm_extra: 计算KL或RMSE时给定的另一个GMM模型
        3) x: 计算RMSE时变量的范围,N-by-d numpy array (2 dimensions)
        4) A: 计算随机变量线性函数的分布时随机变量的系数矩阵, d-by-d numpy array (2 dimensions)
        5) b: 计算随机变量线性函数的分布时随机变量的常数矩阵, d numpy array (1 dimensions)
        6) n_min,n_max: 计算输入分布的1%-100%分位数时随机变量的范围，float

    :return GMM_calculation_result: dict结构，内容为
        {'pdf': float, 'cdf': float, 'KL': float, 'RMSE': float, 'linear_GMM': GaussianMixture, 'quantile': np.ndarray}
        未计算的量为None

    """
    GMM_calculation_result = {'pdf': None, 'cdf': None, 'KL': None, 'RMSE': None, 'linear_GMM': None, 'quantile': None}
    if options == 'pdf':
        if 'y' not in kwargs:
            raise Exception('y must be given when calculating pdf.')
        pdf = np.exp(gmm.score_samples(kwargs['y']))
        if pdf.shape[0] == 1:
            GMM_calculation_result['pdf'] = pdf[0]
        else:
            GMM_calculation_result['pdf'] = pdf
    elif options == 'cdf':
        if 'y' not in kwargs:
            raise Exception('y must be given when calculating cdf.')
        if kwargs['y'].shape[1] > 1:
            raise Exception('y must 1-dimensional when calculating cdf.')
        yy = scipy.integrate.quad(lambda m: np.exp(gmm.score_samples(np.array([[m]]))), -np.inf, kwargs['y'][0])
        if yy.shape[0] == 1:
            GMM_calculation_result['cdf'] = yy[0]
        else:
            GMM_calculation_result['cdf'] = yy
    elif options == 'KL':
        if 'gmm_extra' not in kwargs:
            raise Exception('gmm_extra must be given when calculating KL divergence.')
        KL = functional.func_calculateKL(gmm, kwargs['gmm_extra'])
        GMM_calculation_result['KL'] = KL
    elif options == 'RMSE':
        if 'gmm_extra' not in kwargs or 'x' not in kwargs:
            raise Exception('x and gmm_extra must be given when calculating RMSE.')
        pdf1 = np.exp(gmm.score_samples(kwargs['x']))
        pdf2 = np.exp(kwargs['gmm_extra'].score_samples(kwargs['x']))
        norm2_ = np.linalg.norm(pdf1 - pdf2, ord=2)
        RMSE = norm2_ / math.sqrt(kwargs['x'].shape[0])
        GMM_calculation_result['RMSE'] = RMSE
    elif options == 'linear':
        if 'A' not in kwargs or 'b' not in kwargs:
            raise Exception("A and b must be given when 'options' is 'linear'.")
        gmm_out = copy.deepcopy(gmm)
        for i in range(0, gmm.n_components):
            gmm_out.means_[i] = np.matmul(kwargs['A'], gmm.means_[i]) + kwargs['b']
            cor_temp = np.matmul(kwargs['A'], gmm.covariances_[i])
            gmm_out.covariances_[i] = np.matmul(cor_temp, kwargs['A'].T)
        gmm_out.precisions_ = np.linalg.inv(gmm_out.covariances_)
        gmm_out.precisions_cholesky_ = np.linalg.cholesky(gmm_out.precisions_)
        GMM_calculation_result['linear_GMM'] = gmm_out
    elif options == 'quantile':
        quantile = functional.func_quantile(gmm, kwargs['n_min'], kwargs['n_max'])
        GMM_calculation_result['quantile'] = quantile

    return GMM_calculation_result


def gmm_cal(msg):
    data = json.loads(msg)
    response = {}
    if data['method'] == 'em':
        if data['output'] == 'pdf':
            power = np.array(data['variableList'][0])
            gmm = GMM_distribution(
                power, 3, 'EM', 'marginal')['GMM']
            x = np.linspace(data['inf'], data['sup'], data['x_length'])
            log_pdf = gmm.score_samples(x[:, np.newaxis])
            pdf = np.exp(log_pdf)
            response['x'] = x.tolist()
            response['y'] = pdf.tolist()
        if data['output'] == 'cdf':
            power = np.array(data['variableList'][0])
            cdf = list()
            x = np.linspace(data['inf'], data['sup'], data['x_length'])
            gmm = GMM_distribution(
                power, 3, 'EM', 'marginal')['GMM']
            for x_ in x:
                y_ = scipy.integrate.quad(lambda m: np.exp(gmm.score_samples(np.array([[m]]))), -np.inf, x_)
                cdf.append(y_[0])
            response['x'] = x.tolist()
            response['y'] = cdf
        if data['output'] == 'kl':
            matrix = KL_martrices(data['variableList'], 'em')
            matrix_3d = list()
            axis = []
            for i in range(len(matrix)):
                axis.append(i)
                for j in range(len(matrix[i])):
                    matrix_3d.append([i, j, matrix[i][j]])
            response['x'] = axis
            response['y'] = axis
            response['data'] = matrix_3d
        return response


def GMM_distribution(data, n_components, method, options, y=None, Y_hyper=None, period=None):
    """
    功能：本函数包含概率分布构建功能
        a) 构建任意随机变量的边际分布-EM/MAP
        b) 构建任意多维随机变量的联合分布-EM/MAP
        c) 构建任意多维随机变量的条件分布-EM/MAP
    :param data: n-by-d numpy array, n为训练集样本数量，d为训练集维度/变量个数 (d=1时为numpy向量）
    :param n_components: (必须输入) 高斯个数, int
    :param method: (必须输入) 方法，char，'EM'表示采用EM算法
    :param options:(必须输入) 输出选择, 字符串,
                    'marginal'表示输出边际分布，
                    'joint'表示输出联合分布，
                    'conditional'表示输出条件分布
    :param y: (选择输入) 条件分布的给定值, 1-by-d vector, 每一元素为对应变量的给定值，目标变量处的给定值设为0
    :param Y_hyper: (选择输入)  MAP算法下用于计算超参数的训练集，N-by-d matrix，N为训练集样本数量，d为训练集维度/变量个数
    :param period: (选择输入) MAP算法下用于计算超参数的段数划分，int，即将Y_hyper以period为长度，分成若干小训练集，从而形成多组GMM参数，进而计算超参数
    :return: GMM 单个对象或者 a list of GMM，取决于数据的维度
    """
    # if data.shape[0] == 1:
    #     raise Exception('Sample count cannot be 1.')
    if method == 'EM':
        if options == 'marginal':
            return fit_EM._fit_marginal(data, n_components)
        elif options == 'joint':
            return fit_EM._fit_joint(data, n_components)
        elif options == 'conditional':
            return fit_EM._fit_conditional(data, n_components, y)
    elif method == 'MAP':
        if Y_hyper is None or period is None:
            raise Exception('错误: 缺乏MAP算法必须参数! 请同时设置Y_hyper和period!')
        if options == 'marginal':
            return fit_MAP._fit_marginal(data, n_components, Y_hyper, period)
        elif options == 'joint':
            return fit_MAP._fit_joint(data, n_components, Y_hyper, period)
        elif options == 'conditional':
            return fit_MAP._fit_conditional(data, n_components, y, Y_hyper, period)
    else:
        raise Exception("错误: 您输入的方法名称有误，请重新输入！")
