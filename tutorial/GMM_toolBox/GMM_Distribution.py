from sklearn.mixture import GaussianMixture
import numpy as np

import fit_MAP, fit_EM
# from tutorial.GMM_toolBox import fit_EM, fit_MAP


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

