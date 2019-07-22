# coding=utf-8
import os
import scipy.io as scio
import numpy as np

from GMM_Distribution import GMM_distribution
from GMM_Calculation import GMM_calculation

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = curPath[:curPath.find("Vue-Django-Rest\\") + len("Vue-Django-Rest\\")]


def getDevices():
    filePath = os.path.abspath(rootPath + 'tutorial\\201803a_Origin.mat')
    data = scio.loadmat(filePath)
    data = data['data']
    devices = list()
    for idx in range(20):
        devices.append(data[:, 2 * idx + 1].tolist())
    return devices

def KL_martrices(devices, method):
    length=len(devices)
    Gmms_matrix=list()
    KL_matrix = np.zeros((length, length), dtype=np.float64)
    if method=='em':
        for device in devices:
            Gmms_matrix.append(GMM_distribution(
                np.array(device), 3, 'EM', 'marginal')['GMM'][0])
    for i in range(length):
        for j in range(i+1, length):
            KL_matrix[i, j]= GMM_calculation(Gmms_matrix[i], 'KL', gmm_extra=Gmms_matrix[j])['KL']
    KL_matrix = KL_matrix.T + KL_matrix
    np.fill_diagonal(KL_matrix, 0)
    return KL_matrix.tolist()