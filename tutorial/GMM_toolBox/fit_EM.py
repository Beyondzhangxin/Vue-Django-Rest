from sklearn.mixture import GaussianMixture
import numpy as np
from scipy.stats import multivariate_normal

def _fit_marginal(data, n_components):
    is_matrix = (len(data.shape) == 2)
    if is_matrix:
        gmm = list()
        for idx in range(data.shape[1]):
            gmm.append(GaussianMixture(n_components=n_components, tol=1e-8, max_iter=1000, n_init=10))
            gmm[idx].fit(data[:, idx][:, np.newaxis])
    else:
        gmm = GaussianMixture(n_components=n_components, tol=1e-8, max_iter=1000, n_init=10)
        gmm.fit(data[:, np.newaxis])
    return {'GMM':gmm, 'Corr':None}

def _fit_joint(data, n_components):
    is_matrix = (len(data.shape) == 2)
    if not is_matrix:
        raise Exception('Data to train joint distribution must have at least 2 dimensions.')
    corr = np.corrcoef(data.transpose())
    gmm = GaussianMixture(n_components=n_components, tol=1e-8, max_iter=1000, n_init=10)
    gmm.fit(data)
    return {'GMM': gmm, 'Corr': corr}

def _fit_conditional(data, n_components, y):
    is_matrix = (len(data.shape) == 2)
    if not is_matrix \
            or not isinstance(y, np.ndarray) \
            or len(y.shape) != 1 \
            or y.shape[0] != data.shape[1]:
        raise Exception('Input data is illegal')
    corr = np.corrcoef(data.transpose())
    data_shift = data.copy()

    # 如果给定值按照要求输入后，则平移Y和y，形成第一列为目标分布的格局
    idx_0 = np.where(y==0)[0]
    if idx_0 != 0:
        y[[0, idx_0]] = y[[idx_0, 0]]
        data_shift[:, [0, idx_0]] = data_shift[:, [idx_0, 0]]
    y = y[1:]

    # 按照平移后的Y形成联合分布
    gmm_joint = GaussianMixture(n_components=n_components, tol=1e-8, max_iter=1000, n_init=10)
    gmm_joint.fit(data_shift)

    # 按照平移后的y形成条件分布
    # 首先构造已知边界的临时分布
    temp_gmm = GaussianMixture(n_components=n_components)
    temp_gmm.weights_ = gmm_joint.weights_
    temp_gmm.covariances_ = gmm_joint.covariances_[:,1:,1:]
    temp_gmm.means_ = gmm_joint.means_[:,1:]
    temp_gmm.precisions_ = np.linalg.inv(temp_gmm.covariances_)
    temp_gmm.precisions_cholesky_ = np.linalg.cholesky(temp_gmm.precisions_)

    sum_weights_ = np.exp(temp_gmm.score_samples(y.reshape(1,-1))[0])
    gmm_condition = GaussianMixture(n_components=n_components)

    weights = np.zeros((n_components,), dtype=np.float32)
    means = np.zeros((n_components,1), dtype=np.float32)
    covariances = np.zeros((n_components,1,1), dtype=np.float32)

    for component in range(n_components):
        weights[component] = temp_gmm.weights_[component] * multivariate_normal.pdf(y, temp_gmm.means_[component], temp_gmm.covariances_[component]) / sum_weights_
        means[component][0] = gmm_joint.means_[component,0] + np.dot(
            np.transpose(
                np.linalg.solve(
                    gmm_joint.covariances_[component, 1:, 1:],
                    gmm_joint.covariances_[component, 1:, 0]
                )
            )[0],
            gmm_joint.means_[component, 1:]
        )
        covariances[component][0,0] = gmm_joint.covariances_[component, 0, 0] - np.dot(
            np.transpose(
                np.linalg.solve(
                    gmm_joint.covariances_[component, 1:, 1:],
                    gmm_joint.covariances_[component, 1:, 0]
                )
            ),
            gmm_joint.covariances_[component, 1:, 0]
        ).item()
    gmm_condition.weights_ = weights
    gmm_condition.means_ = means
    gmm_condition.covariances_ = covariances
    gmm_condition.precisions_ = np.linalg.inv(gmm_condition.covariances_)
    gmm_condition.precisions_cholesky_ = np.linalg.cholesky(gmm_condition.precisions_)

    # 按照原始输入的Y_original形成联合分布，输出结果和输入的Y完美匹配
    gmm_joint.fit(data)

    return {'GMM': gmm_joint, 'CGMM': gmm_condition, 'Corr': corr}