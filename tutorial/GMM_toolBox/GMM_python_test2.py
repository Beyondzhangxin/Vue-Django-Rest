# coding=utf-8
# data from 2018-3-30

from .GMM_Distribution import GMM_distribution


def calculate_matrices(pv_devices):
    # 建立GMM模型
    GMMs_30 = list()
    for pv_device in pv_devices:
        GMMs_30.append(GMM_distribution(
            pv_device['power'], 3, 'EM', 'marginal')['GMM'])

    KL_matrix_30 = np.zeros((len(GMMs_30), len(GMMs_30)), dtype=np.float64)
    # 计算KL距离矩阵的上三角部分
    for i in range(len(GMMs_30)):
        for j in range(i+1, len(GMMs_30)):
            KL_matrix_30[i, j] = functional.func_MonteCaro_JS(
                GMMs_30[i], GMMs_30[j], 1000)
    # 补全
    KL_matrix_30 = KL_matrix_30.T + KL_matrix_30
    np.fill_diagonal(KL_matrix_30, 0)
    return KL_matrix_30


def plot_matrix(matrix, mode):
    N = matrix.shape[0]
    fig2 = plt.figure(figsize=(10, 6))
    plt.imshow(matrix)
    plt.colorbar()
    plt.xticks(range(0, N), range(1, N+1))
    plt.yticks(range(0, N), range(1, N+1))
    plt.xlabel('PV number')
    plt.ylabel('PV number')
    if mode == 'KL':
        plt.title('KL divergence between different PVs')
    else:
        plt.title('Correlations of KL divergence')
    plt.show()

KL_30 = calculate_matrices(pv_devices_30)
plot_matrix(KL_30, 'KL')
corr_KL_30 = np.corrcoef(KL_30.T)
plot_matrix(corr_KL_30, 'corrKL')


# data from 2018-3-23

pv_devices_23 = get_devices(23)
KL_23 = calculate_matrices(pv_devices_23)
corr_KL_23 = np.corrcoef(KL_23.T)
plot_matrix(KL_23, 'KL')
plot_matrix(corr_KL_23, 'corrKL')

