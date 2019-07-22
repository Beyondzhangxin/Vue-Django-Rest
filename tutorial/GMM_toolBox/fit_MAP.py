from sklearn.mixture import GaussianMixture
import numpy as np
import copy
from scipy.stats import multivariate_normal


def _fit_marginal(data, n_components, Y_hyper, period:int):
    is_matrix = (len(data.shape) == 2)
    if is_matrix:
        raise Exception('错误: 您输入的训练数据维度大于1维，请重新输入！')
    else:
        if Y_hyper.shape[0] % period != 0:
            raise Exception('错误: 您输入的用于形成超参数的历史数据和时段没有形成整除关系，请重新输入！')
        else:
            gmm = GaussianMixture(n_components=n_components, tol=1e-8, max_iter=1000, n_init=10)
            gmm.fit(Y_hyper[:, np.newaxis])
            gmm = gmm_map_qb(data[:, np.newaxis], gmm, display=False)
    return {'GMM':gmm, 'Corr':None}

def _fit_joint(data, n_components, Y_hyper, period:int):
    is_matrix = (len(data.shape) == 2)
    if not is_matrix:
        raise Exception('错误: 您输入的训练数据维度小于2维，请重新输入！')
    else:
        if Y_hyper.shape[0] % period != 0:
            raise Exception('错误: 您输入的用于形成超参数的历史数据和时段没有形成整除关系，请重新输入！')
        else:
            gmm = GaussianMixture(n_components=n_components, tol=1e-8, max_iter=1000, n_init=10)
            gmm.fit(Y_hyper)
            gmm = gmm_map_qb(data, gmm, display=False)
    return {'GMM':gmm, 'Corr':None}

def _fit_conditional(data, n_components, y, Y_hyper, period:int):
    is_matrix = (len(data.shape) == 2)
    if not is_matrix \
            or not isinstance(y, np.ndarray) \
            or len(y.shape) != 1 \
            or y.shape[0] != data.shape[1]:
        raise Exception('Input data is illegal')
    if Y_hyper.shape[0] % period != 0:
        raise Exception('错误: 您输入的用于形成超参数的历史数据和时段没有形成整除关系，请重新输入！')
    corr = np.corrcoef(data.transpose())
    data_shift = data.copy()
    Y_hyper_shift = Y_hyper.copy()

    # 如果给定值按照要求输入后，则平移Y和y，形成第一列为目标分布的格局
    idx_0 = np.where(y == 0)[0]
    if idx_0 != 0:
        y[[0, idx_0]] = y[[idx_0, 0]]
        data_shift[:, [0, idx_0]] = data_shift[:, [idx_0, 0]]
        Y_hyper_shift[:, [0, idx_0]] = Y_hyper_shift[:, [idx_0, 0]]
    y = y[1:]

    # 按照平移后的Y和Y_hyper形成联合分布
    gmm_joint = GaussianMixture(n_components=n_components, tol=1e-8, max_iter=1000, n_init=10)
    gmm_joint.fit(Y_hyper_shift)
    gmm_joint = gmm_map_qb(data_shift, gmm_joint, display=False)

    # 按照平移后的y形成条件分布
    # 首先构造已知边界的临时分布
    temp_gmm = GaussianMixture(n_components=n_components)
    temp_gmm.weights_ = gmm_joint.weights_
    temp_gmm.covariances_ = gmm_joint.covariances_[:, 1:, 1:]
    temp_gmm.means_ = gmm_joint.means_[:, 1:]
    temp_gmm.precisions_ = np.linalg.inv(temp_gmm.covariances_)
    temp_gmm.precisions_cholesky_ = np.linalg.cholesky(temp_gmm.precisions_)

    sum_weights_ = np.exp(temp_gmm.score_samples(y.reshape(1,-1))[0])
    gmm_condition = GaussianMixture(n_components=n_components)

    weights = np.zeros((n_components,), dtype=np.float32)
    means = np.zeros((n_components, 1), dtype=np.float32)
    covariances = np.zeros((n_components, 1, 1), dtype=np.float32)

    for component in range(n_components):
        weights[component] = temp_gmm.weights_[component] * multivariate_normal.pdf(y, temp_gmm.means_[component],
                                                                                    temp_gmm.covariances_[
                                                                                        component]) / sum_weights_
        means[component][0] = gmm_joint.means_[component, 0] + np.dot(
            np.transpose(
                np.linalg.solve(
                    gmm_joint.covariances_[component, 1:, 1:],
                    gmm_joint.covariances_[component, 1:, 0]
                )
            )[0],
            gmm_joint.means_[component, 1:]
        )
        covariances[component][0, 0] = gmm_joint.covariances_[component, 0, 0] - np.dot(
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

def gmm_map_qb(X, gmm, rho=.1, epsilon=1, niter=1000, display=False):
    """
       GMM adaptation using Quasi-Bayes MAP method.
       Usage: gmm_map_qb(X, gmm, rho, epsilon, niter)
       //Ref. 1) (1994 Gauvain, Lee) Maximum a Posteriori Estimation for Multivariate Gaussian Mixture Observations of Markov Chains
       //Ref. 2) (1997 Huo, Lee) On-line adaptive learning of the continuous density hidden markov model based on approximate recursive bayes estimate
       //Ref. 3) (2010 Kim, Loizou) Improving Speech Intelligibility in Noise Using Environment-Optimized Algorithms"""

    # init
    # logprob, pcompx = gmm.eval(X) # deprecated in new version sklearn
    # logprob = gmm.score_samples(X)
    pcompx = gmm.predict_proba(X)

    psum = np.sum(pcompx, axis=0)  # (18)
    # remove illed gaussians
    ill_g = (psum == 0)
    if any(ill_g):
        valid = psum > 0
        gmm.means_ = gmm.means_[valid, :]
        gmm.weights_ = gmm.weights_[valid]
        gmm.weights_ = gmm.weights_ / sum(gmm.weights_)
        gmm.covariances_ = gmm.covariances_[valid]

    # logprob, pcompx = gmm.eval(X) # deprecated in new version sklearn
    # logprob = gmm.score_samples(X)
    pcompx = gmm.predict_proba(X)

    psum = np.sum(pcompx, axis=0)  # (18)
    K, nDim = gmm.means_.shape
    tau = psum * epsilon  # (22)
    tau_update = tau
    nu = 1 + tau  # (23)
    nu_update = nu
    alpha = nDim + tau  # (24)
    alpha_update = alpha
    mu = np.empty([K, nDim])
    mu_update = np.empty([K, nDim])
    yu = np.empty([K, nDim, nDim])
    yu_update = np.empty([K, nDim, nDim])
    for k in range(0, K):
        mu[k] = gmm.means_[k]  # (25)
        yu[k] = tau[k] * gmm.covariances_[k]  # (26)

    # EM iterations
    s = np.empty([K, nDim, nDim])
    N = X.shape[0]
    if display:
        print('%10s|%20s|%20s|%10s' % ('iter', 'step_weights_norm', 'step_means_norm', 'step_cov'))
    for iter in range(0, niter):
        old_gmm = copy.deepcopy(gmm)
        # print('iter=', iter)
        # print(np.sum(gmm.weights_))
        # plotgmm(gmm,X)
        # E-step: posterior probabilities
        # logprob, pcompx = gmm.eval(X) # deprecated in new version sklearn
        pcompx = gmm.predict_proba(X)

        # remove illed gaussians
        psum = np.sum(pcompx, axis=0)  # (18)
        # print psum
        # raw_input()
        ill_g = (psum == 0)
        # print ill_g
        if any(ill_g):
            valid = psum > 0
            gmm.means_ = gmm.means_[valid, :]
            gmm.weights_ = gmm.weights_[valid]
            gmm.weights_ = gmm.weights_ / sum(gmm.weights_)
            gmm.covariances_ = gmm.covariances_[valid]
            mu = mu[valid]
            mu_update = mu_update[valid]
            yu = yu[valid]
            yu_update = yu_update[valid]
            tau = tau[valid]
            tau_update = tau_update[valid]
            alpha = alpha[valid]
            alpha_update = alpha_update[valid]
            nu = nu[valid]
            nu_update = nu_update[valid]
            K = gmm.means_.shape[0]
            continue

        # M-step, eqs. from KimLoizou'10
        # Hyper-parameters
        psum = np.sum(pcompx, axis=0)  # (18)
        # print np.sum(pcompx,axis=1)
        # print 'psum',psum
        # print gmm.weights_
        # raw_input()
        x_expected = np.dot(pcompx.T, X) / np.tile(psum[np.newaxis].T, (1, nDim))  # (19)
        # print 'x_expected',x_expected
        for k in range(0, K):
            # raw_input()
            # (20)
            s[k] = np.dot((X - np.tile(x_expected[k], (N, 1))).T,
                          (X - np.tile(x_expected[k], (N, 1))) * np.tile(pcompx[:, k][np.newaxis].T, (1, nDim)))
            # (15)
            # print 'yu[k]',yu[k]
            # print 'x_expected - mu', (x_expected-mu).T
            # yu_update[k] = rho*yu[k] + s[k] + rho*tau[k]*psum[k]/(rho*tau[k]+psum[k])*np.dot((x_expected-mu).T, x_expected-mu)
            yu[k] = rho * yu[k] + s[k] + rho * tau[k] * psum[k] / (rho * tau[k] + psum[k]) * np.dot(
                (x_expected[k, :] - mu[k, :]).T, x_expected[k, :] - mu[k, :])
            # print 'yu[k],after',yu[k]

        # (21)
        beta = psum / (rho * tau + psum)
        # mu, eq (14)
        # print beta.shape
        # print mu.shape
        # print x_expected.shape
        # mu_update = np.tile(beta[np.newaxis].T,(1,nDim))*x_expected + np.tile((1-beta)[np.newaxis].T,(1,nDim))*mu
        mu = np.tile(beta[np.newaxis].T, (1, nDim)) * x_expected + np.tile((1 - beta)[np.newaxis].T, (1, nDim)) * mu
        # tau, eq (11)
        # tau_update = rho*tau + psum
        tau = rho * tau + psum
        # alpha, eq (12)
        # alpha_update = rho*(alpha-nDim) + nDim + psum
        alpha = rho * (alpha - nDim) + nDim + psum
        # print 'alpha',alpha
        # nu, eq (13)
        # nu_update = rho*(nu-1) + 1 + psum
        nu = rho * (nu - 1) + 1 + psum

        # GMM parameters
        # weight, (27)
        # gmm.weights_ = (nu_update-1)/np.sum(nu_update-1)
        gmm.weights_ = (nu - 1) / np.sum(nu - 1)
        ill = (gmm.weights_ == 0)
        # print(np.sum(gmm.weights_))
        # mean, (28)
        # gmm.means_ = mu_update
        gmm.means_ = mu
        # sigma, (29)
        for k in range(0, K):
            # if alpha_update[k] != nDim:
            if alpha[k] != nDim:
                # gmm.covariances_[k] = yu_update[k]/(alpha_update[k]-nDim)
                gmm.covariances_[k] = yu[k] / (alpha[k] - nDim)
            else:
                # gmm.covariances_[k] = yu_update[k]/tau_update[k]
                gmm.covariances_[k] = yu[k] / tau[k]
            try:
                np.linalg.cholesky(gmm.covariances_[k])
            except:
                ill[k] = 1
                # print('cov_%d not positive definite' % k)

        step_weights_norm = np.linalg.norm(old_gmm.weights_ - gmm.weights_)
        step_means_norm = np.linalg.norm(old_gmm.means_-gmm.means_)
        step_cov = np.amax(old_gmm.covariances_ - gmm.covariances_)
        if display:
            print('%10d|%20f|%20f|%10f' % (iter, step_weights_norm, step_means_norm, step_cov))
        if step_weights_norm<=1e-3 and step_means_norm<=1e-3 \
            and step_cov<=1e-3:
            break

        # remove non positive definite matrices
        if np.any(ill):
            valid = (ill == 0)
            gmm.means_ = gmm.means_[valid]
            gmm.weights_ = gmm.weights_[valid]
            gmm.weights_ = gmm.weights_ / sum(gmm.weights_)
            gmm.covariances_ = gmm.covariances_[valid]
            mu = mu[valid]
            mu_update = mu_update[valid]
            yu = yu[valid]
            yu_update = yu_update[valid]
            tau = tau[valid]
            tau_update = tau_update[valid]
            alpha = alpha[valid]
            alpha_update = alpha_update[valid]
            nu = nu[valid]
            nu_update = nu_update[valid]
            K = gmm.means_.shape[0]

    gmm.precisions_ = np.linalg.inv(gmm.covariances_)
    gmm.precisions_cholesky_ = np.linalg.cholesky(gmm.precisions_)
    return gmm