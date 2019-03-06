import math
from numpy.random import multivariate_normal
import operator
import numpy as np
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture


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

def plot_gmm(gmm, inf, sup):
    # 画出gmm模型的pdf曲线
    # 目前是只能画出1-D gmm
    x = np.linspace(inf, sup, 1000)
    fig = plt.figure()
    if isinstance(gmm, list):
        pdf_array = list()
        for gmm_ in gmm:
            log_pdf = gmm_.score_samples(x[:, np.newaxis])
            pdf_array.append(np.exp(log_pdf))
        for pdf in pdf_array:
            plt.plot(x, pdf)
    else:
        log_pdf = gmm.score_samples(x[:, np.newaxis])
        pdf = np.exp(log_pdf)
        plt.plot(x, pdf)
    plt.xlabel('x')
    plt.ylabel('pdf')
    plt.show()
    return fig