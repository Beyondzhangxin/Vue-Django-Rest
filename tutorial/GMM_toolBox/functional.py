import math
from numpy.random import multivariate_normal
import operator
import numpy as np
import scipy.integrate
from scipy.optimize import linprog
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture

# from GMM_toolBox import GMM_Calculation
import GMM_Calculation


def func_calculateKL(gmm1: GaussianMixture,
                     gmm2: GaussianMixture):
    if gmm1.n_components != gmm2.n_components or gmm1.means_.shape[1] != gmm2.means_.shape[1]:
        raise Exception('The two gmms must have the same number of components '
                        'and features when calculating KL divergence.')
    n_components = gmm1.n_components
    n_features = gmm1.means_.shape[1]

    # 构造线性规划参数
    c = np.zeros((n_components*n_components,), dtype=np.float)
    A_up = np.zeros((n_components, n_components*n_components), dtype=np.float)
    A_down = np.zeros((n_components, n_components*n_components), dtype=np.float)
    # bounds = tuple([tuple((0, None))]) * (n_components*n_components)
    Aeq = np.ones((1, n_components*n_components), dtype=np.float)
    beq = np.ones((1,), dtype=np.float)

    # 形成目标函数系数列向量c
    m = 0 # 计数器
    for i in range(0, n_components):
        for j in range(0, n_components):
            KLDij = 0.5 * (
                    math.log(np.linalg.det(gmm2.covariances_[j]))/np.linalg.det(gmm1.covariances_[i]) \
                    + np.trace(np.linalg.solve(gmm2.covariances_[j], gmm1.covariances_[i])) \
                    + np.matmul((gmm1.means_[i] - gmm2.means_[j]),
                                np.linalg.solve(gmm2.covariances_[j], gmm1.means_[i] - gmm2.means_[j])) \
                    - n_features
            )
            KLDji = 0.5 * (
                    math.log(np.linalg.det(gmm1.covariances_[i])) / np.linalg.det(gmm2.covariances_[j]) \
                    + np.trace(np.linalg.solve(gmm1.covariances_[i], gmm2.covariances_[j])) \
                    + np.matmul((gmm2.means_[j] - gmm1.means_[i]),
                                np.linalg.solve(gmm1.covariances_[i], gmm2.means_[j] - gmm1.means_[i])) \
                    - n_features
            )
            c[m] = 0.5 * (KLDij + KLDji)
            m += 1

    for n in range(0, n_components):
        A_up[n, n * n_components:(n + 1) * n_components] = 1
        A_down[n, np.arange(n, (n_components - 1) * n_components + n, n_components)] = 1

    A = np.concatenate((A_up, A_down), axis=0)
    b_up = gmm1.weights_
    b_down = gmm2.weights_
    b = np.concatenate((b_up, b_down), axis=0)

    res = linprog(c, A, b, Aeq, beq, options={'maxiter': 10*(n_components + 2 * n_components + n_components*n_components)})
    return res['fun']

def func_quantile(gmm: GaussianMixture, n_min, n_max):
    x = np.linspace(n_min, n_max, 1000)
    cdfs = list()
    for i in range(0, 1000):
        cdfs.append(scipy.integrate.quad(lambda m: np.exp(gmm.score_samples(np.array([[m]]))), -np.inf, x[i])[0])
    cdfs = np.array(cdfs)
    res = list()
    for j in range(1, 101):
        min_index = np.argmin(np.abs(cdfs - j*0.01))
        res.append(x[min_index])
    return np.array(res)

def func_MonteCaro_JS(gmm1: GaussianMixture,
                      gmm2: GaussianMixture,
                      sample_count: int):
    # sample gmm1 and gmm2
    # 不需要用这个，直接用gmm的sample方法
    # samples1 = func_MenteCaro_sampling(gmm1, sample_count)
    # samples2 = func_MenteCaro_sampling(gmm2, sample_count)
    samples1, _ = gmm1.sample(1000)
    samples2, _ = gmm2.sample(1000)
    logvalue12 = gmm1.score_samples(samples1)/np.log(10) - np.log10(0.5*np.exp(gmm1.score_samples(samples1))
                                                                    + 0.5*np.exp(gmm2.score_samples(samples1)))
    logvalue21 = gmm2.score_samples(samples2) / np.log(10) - np.log10(0.5 * np.exp(gmm1.score_samples(samples2))
                                                                      + 0.5 * np.exp(gmm2.score_samples(samples2)))
    return 0.5*np.mean(logvalue12)+0.5*np.mean(logvalue21)


def func_MenteCaro_sampling(gmm: GaussianMixture,
                            sample_count: int):
    # 这个函数是从matlab版本的代码翻译过来的，其实不需要用，直接用gmm的sample方法即可
    samples = list()
    weights_ = gmm.weights_
    means_ = gmm.means_
    covariances_ = gmm.covariances_

    # 生成各个分量对应的场景数
    sample_count_per_component = list()
    for w_ in weights_:
        sample_count_per_component.append(math.ceil(w_*sample_count))

    if sum(sample_count_per_component) != sample_count:
        max_idx, element = max(enumerate(sample_count_per_component), key=operator.itemgetter(1))
        sample_count_per_component[max_idx] -= (sum(sample_count_per_component)
                                                - sample_count)
    # sample from each components
    for gauss_idx in range(weights_.shape[0]):
        samples += list(multivariate_normal(means_[gauss_idx],
                                       covariances_[gauss_idx],
                                       sample_count_per_component[gauss_idx]))
    samples = np.array(samples)
    return samples


def plot_pdf(gmm, inf, sup):
    # 画出gmm模型的pdf曲线
    # 目前是只能画出1-D gmm
    x = np.linspace(inf, sup, 100)
    fig = plt.figure()
    if isinstance(gmm, list):
        pdf_array = list()
        for gmm_ in gmm:
            pdf = GMM_Calculation.GMM_calculation(gmm_, 'pdf', y=x[:, np.newaxis])['pdf']
            pdf_array.append(pdf)
        for pdf in pdf_array:
            plt.plot(x, pdf)
    else:
        pdf = GMM_Calculation.GMM_calculation(gmm, 'pdf', y=x[:, np.newaxis])['pdf']
        plt.plot(x, pdf)
    plt.xlabel('x')
    plt.ylabel('pdf')
    plt.show()
    return fig


def plot_cdf(gmm, inf, sup):
    # 画出gmm模型的cdf曲线
    # 目前是只能画出1-D gmm
    x = np.linspace(inf, sup, 100)
    fig = plt.figure()
    if isinstance(gmm, list):
        cdfs = list()
        for gmm_ in gmm:
            cdf = list()
            for x_ in x:
                y_ = scipy.integrate.quad(lambda m: np.exp(gmm_.score_samples(np.array([[m]]))), -np.inf, x_)
                cdf.append(y_[0])
            cdf = np.array(cdf)
            cdfs.append(cdf)
        for cdf in cdfs:
            plt.plot(x, cdf)
    else:
        cdf = list()
        for x_ in x:
            y_ = scipy.integrate.quad(lambda m: np.exp(gmm.score_samples(np.array([[m]]))), -np.inf, x_)
            cdf.append(y_[0])
        cdf = np.array(cdf)
        plt.plot(x, cdf)
    plt.xlabel('x')
    plt.ylabel('cdf')
    plt.show()
    return fig