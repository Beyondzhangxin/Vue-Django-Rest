# coding=utf-8
import datetime
import random
import time
from threading import Thread

import numpy as np
import pika

from GMM_Calculation import GMM_distribution, GMM_calculation, KL_martrices
from clickhouse_driver import Client

from receive import save_data_to_clickhouse
from send import send_data_to_clickhouse


def test_gmmDistribution():
    client = Client(host='10.112.10.24')
    inf = 0
    sup = 300
    x_length = 100
    x = np.linspace(inf, sup, x_length)
    sql = "select power from siemense.siemense_objlist where TimeStamp between '2019-07-17 23:27:18' AND '2019-07-18 23:27:18' "
    factory_data = client.execute(sql)
    power = np.array(factory_data)
    gmm = GMM_distribution(power, 3, 'EM', 'marginal')['GMM']
    a = np.array([1])
    b = np.array([2])
    linear_gmm = GMM_calculation(gmm[0], 'linear', A=a, b=b)
    log_pdf = linear_gmm['linear_GMM'].score_samples(x[:, np.newaxis])
    pdf = list(np.exp(log_pdf))
    pass


# test_gmmDistribution()


def test_kl():
    devices = []
    client = Client(host='10.112.10.24')
    t1 = datetime.datetime.now()
    sql = "select power from siemense.siemense_objlist where TimeStamp between '2019-07-22 09:27:18' AND '2019-07-22 23:27:18' "
    factory_data = client.execute(sql)
    print(len(factory_data))
    devices.append(factory_data)
    devices.append(factory_data)
    t2=datetime.datetime.now()
    matrix = KL_martrices(devices, 'em')
    matrix_3d = list()
    t4 = datetime.datetime.now()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix_3d.append([i, j, matrix[i][j]])
    t3 = datetime.datetime.now()

    period = t2 - t1
    print(period)
    print(t4-t2)
    print(t3 - t4)

test_kl()


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
# mock_data_from_clickhouse(3600*12)
