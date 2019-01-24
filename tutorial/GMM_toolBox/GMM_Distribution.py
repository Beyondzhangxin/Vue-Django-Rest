from sklearn.mixture import GaussianMixture
from scipy.stats import multivariate_normal
import numpy as np


def GMM_distribution(data, n_components, method, options, y=None):
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
    :return:
    """
    if data.shape[0] == 1:
        raise Exception('Sample count cannot be 1.')
    if method != 'EM':
        raise Exception('The input method is unavailable.')
    if options == 'marginal':
        return _fit_marginal(data, n_components)
    elif options == 'joint':
        return _fit_joint(data, n_components)
    elif options == 'conditional':
        return _fit_conditional(data, n_components, y)

def _fit_marginal(data, n_components):
    is_matrix = (len(data.shape) == 2)
    if is_matrix:
        gmm = list()
        for idx in range(data.shape[1]):
            gmm.append(GaussianMixture(n_components=n_components, tol=1e-8, max_iter=1000))
            gmm[idx].fit(data[:, idx][:, np.newaxis])
    else:
        gmm = GaussianMixture(n_components=n_components, tol=1e-8, max_iter=1000)
        gmm.fit(data[:, np.newaxis])
    return {'GMM':gmm, 'Corr':None}

def _fit_joint(data, n_components):
    is_matrix = (len(data.shape) == 2)
    if not is_matrix:
        raise Exception('Data to train joint distribution must have at least 2 dimensions.')
    corr = np.corrcoef(data.transpose)
    gmm = GaussianMixture(n_components=n_components, tol=1e-8, max_iter=1000)
    gmm.fit(data)
    return {'GMM': gmm, 'Corr': corr}

def _fit_conditional(data, n_components, y):
    is_matrix = (len(data.shape) == 2)
    if not is_matrix \
            or not isinstance(y, np.ndarray) \
            or len(y.shape) != 1 \
            or y.shape[0] != data.shape[1]:
        raise Exception('Input data is illegal')
    corr = np.corrcoef(data.transpose)
    data_shift = data.copy()

    # 如果给定值按照要求输入后，则平移Y和y，形成第一列为目标分布的格局
    idx_0 = np.where(y==0)[0]
    y[[0, idx_0]] = y[[idx_0, 0]]
    y = y[1:]
    data_shift[:, [0, idx_0]] = data_shift[:, [idx_0, 0]]

    # 按照平移后的Y形成联合分布
    gmm_joint = GaussianMixture(n_components=n_components, tol=1e-8, max_iter=1000)
    gmm_joint.fit(data_shift)

    # 按照平移后的y形成条件分布

    # 首先获得 gmm_joint 的 mu 和 sigma
    # TODO
    return None
