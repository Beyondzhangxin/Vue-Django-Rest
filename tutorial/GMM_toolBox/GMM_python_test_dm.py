# coding=utf-8
import scipy.io as scio
import numpy as np
import datetime
import matplotlib.pyplot as plt
import functional
import copy

from GMM_Distribution import GMM_distribution

data = scio.loadmat('201803a_Origin.mat')
data = data['data']
def matlab2datetime(matlab_datenum):
    day = datetime.datetime.fromordinal(int(matlab_datenum))
    day = day.replace(year=day.year + 1900)
    dayfrac = datetime.timedelta(days=matlab_datenum %
                                 1) - datetime.timedelta(days=366)
    return day + dayfrac


pv_devices = list()
for idx in range(20):
    if idx == 2-1 or idx == 4-1:
        current_device = {'time': None,
                          'power': np.zeros((50,), dtype=np.float64)}
        pv_devices.append(current_device)
    else:
        current_device = {'time': list(), 'power': list()}
        for (tval, pval) in zip(data[:, 2*idx], data[:, 2*idx+1]):
            if tval == 0:
                break
            current_device['time'].append(matlab2datetime(tval))
            current_device['power'].append(pval)
        # current_device['power'] = np.array(current_device['power'])
        pv_devices.append(current_device)

(pv_devices[0]['time'][0] - datetime.datetime(2018, 3, 30)).total_seconds()

# out:-1757999.999998

# Data analysis
def get_devices(date_day):
    pv_devices_ = list()
    for idx_device in range(len(pv_devices)):
        if idx_device == 2-1 or idx_device == 4-1:
            pv_devices_.append(pv_devices[idx_device])
        else:
            for idx_time_start in range(len(pv_devices[idx_device]['time'])):
                if (pv_devices[idx_device]['time'][idx_time_start]
                    >= datetime.datetime(2018, 3, date_day)):
                    break
            for idx_time_end in range(idx_time_start, len(pv_devices[idx_device]['time'])):
                if not (pv_devices[idx_device]['time'][idx_time_end]
                        < datetime.datetime(2018, 3, date_day+1)):
                    break
            pv_devices_.append(
                {'time':
                 pv_devices[idx_device]['time'][idx_time_start:idx_time_end],
                 'power':
                 np.array(pv_devices[idx_device]['power']
                          [idx_time_start:idx_time_end])}
            )
    print(pv_devices_)
    return pv_devices_

pv_devices_30 = get_devices(30)
fig = plt.figure()
plt.plot(pv_devices_30[0]['time'], pv_devices_30[0]['power'])
plt.xlabel('time')
plt.ylabel('PV #1 Power')
plt.title('PV #1 Power Curve')
plt.show()

# data from 2018-3-30




def calculate_matrices(pv_devices):
    # 建立GMM模型
    GMMs_30 = list()
    testData=[[8.533],[7.578],[8.692],[7.148],[7.148],[7.768],[7.768],[7.265],[7.293],[7.293],[8.961],[8.961],[9.962],[10.625],[10.625],[11.688],[12.941],[12.95],[12.853],[12.833],[13.15],[13.25],[13.643],[13.848],[13.808],[7.919],[9.72],[5.835],[5.045],[4.578],[4.45],[4.428],[4.342],[4.216],[4.101],[3.89],[3.884],[3.798],[3.701],[3.655],[3.678],[3.691],[3.695],[3.689],[3.699],[3.591],[3.604],[3.604],[3.601],[3.764],[3.831],[3.94],[4.134],[4.25],[4.496],[4.801],[5.018],[5.332],[5.662],[5.977],[6.317],[6.64],[6.947],[7.289],[7.684],[8.028],[8.383],[8.824],[9.092],[8.991],[8.929],[9.999],[10.796],[11.192],[12.924],[14.201],[13.916],[13.511],[13.76],[13.976],[13.572],[11.106],[7.84],[6.12],[5.881],[6.075],[8.914],[12.505],[12.731],[12.365],[12.954],[12.888],[12.449],[12.666],[12.616],[12.842],[12.909],[11.812],[11.475],[11.26],[11.369],[11.475],[11.267],[10.551],[10.691],[10.346],[10.677],[11.057],[11.164],[11.722],[11.983],[12.303],[12.542],[12.361],[13.132],[14.021],[14.255],[14.573],[14.701],[14.537],[7.061],[4.29],[4.382],[4.398],[14.34],[4.35],[4.293],[4.47],[4.712],[5.251],[14.31],[5.271],[6.058],[12.726],[12.633],[12.625],[12.464],[12.452],[12.381],[12.73],[12.983],[13.392],[5.678],[12.99],[12.429],[13.435],[13.105],[13.12],[12.197],[12.919],[13.125],[12.804],[12.939],[12.234],[11.511],[9.647],[13.279],[11.3],[13.375],[13.192],[12.576],[12.621],[12.821],[12.91],[12.903],[13.012],[12.901],[12.853],[12.87],[12.95],[12.807],[12.974],[12.976],[13.005],[12.929],[12.805],[13.628],[13.805],[13.399],[13.05],[8.665],[4.702],[6.563],[6.566],[4.326],[4.166],[4.366],[4.782],[11.195],[13.004],[12.984],[11.353],[12.865],[12.667],[12.509],[12.318],[12.228],[12.12],[12.136],[10.151],[10.68],[12.092],[12.162],[12.121],[11.987],[11.762],[11.528],[11.432],[11.175],[11.337],[5.285],[10.319],[9.6],[10.936],[11.767],[11.656],[11.716],[6.456],[11.004],[11.11],[11.173],[11.108],[10.997],[11.056],[11.011],[10.955],[10.916],[10.884],[10.853],[10.832],[10.74],[10.624],[10.597],[10.517],[10.407],[10.566],[10.535],[10.572],[10.57],[10.59],[10.693],[10.572],[10.423],[9.89],[10.03],[10.245],[10.142],[10.246],[10.257],[10.312],[9.545],[7.563],[6.363],[6.382],[6.222],[5.969],[5.936],[6.028],[6.01],[7.911],[8.091],[8.155],[7.577],[9.723],[9.572],[4.445],[9.25],[9.544],[9.616],[9.848],[9.718],[9.488],[9.355],[9.296],[9.159],[8.966],[8.765],[8.667],[8.561],[8.319],[7.513],[8.118],[7.49],[7.929],[7.339],[6.783],[3.006],[5.653],[7.593],[7.832],[7.898],[7.84],[7.819],[7.616],[7.494],[7.496],[7.311],[6.915],[6.908],[6.847],[6.916],[6.976],[7.106],[7.012],[6.979],[6.807],[6.558],[6.257],[6.223],[6.267],[6.331],[6.338],[6.349],[6.481],[6.432],[6.51],[6.605],[6.59],[6.513],[6.513],[6.488],[6.37],[6.189],[6.137],[6.018],[5.916],[5.641],[3.544],[3.483],[4.861],[5.348],[5.412],[5.309],[5.354],[5.195],[5.003],[2.126],[2.734],[2.08],[3.688],[2.542],[3.715],[4.597],[4.791],[4.609],[4.351],[4.168],[4.187],[4.413],[4.446],[4.288],[3.883],[3.54],[3.64],[3.494],[3.343],[3.23],[2.93],[2.803],[2.559],[2.553],[2.584],[2.207],[2.261],[2.512],[2.14],[2.032],[1.829],[1.761],[1.663],[1.599],[1.48],[1.458],[1.462],[1.381],[1.385],[1.384],[1.325],[1.266],[1.315],[1.383],[1.264],[1.26],[1.262],[1.258],[1.204],[1.212],[1.204],[1.208],[1.202],[1.212],[1.261],[1.264],[1.259],[1.267],[1.262],[1.263],[1.204],[1.198],[1.196],[1.202],[1.201],[1.085],[1.083],[1.09],[1.144],[1.134],[1.204],[1.197],[1.201],[1.261],[1.263],[1.264],[1.264],[1.206],[1.203],[1.208],[1.157],[1.09],[1.094],[1.034],[1.038],[0.979],[0.981],[0.923],[0.921],[0.92],[0.922],[0.921],[0.921],[0.863],[0.862],[0.862],[0.861],[0.861],[0.862],[0.748],[0.75],[0.75],[0.69],[0.691],[0.689],[0.691],[0.631],[0.632],[0.575],[0.635],[0.575],[0.52],[0.521],[0.522],[0.522],[0.462],[0.462],[0.463],[0.345],[0.347],[0.349],[0.288],[0.289],[0.288],[0.288],[0.172],[0.172],[0.222],[0.222],[0.208],[0.165],[0.166],[0.161],[0.145],[0.13],[0.109],[0.105],[0.055],[0.055],[0.055],[0.055],[0.055],[0.055],[0.055],[0.055],[0.055],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
    
    testData=np.array(testData)
    testData=testData.T
    for pv_device in pv_devices:
        GMMs_30.append(GMM_distribution(
            testData[0], 3, 'EM', 'marginal')['GMM'])

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

# modified data from 2018-3-30

pv_devices_30_fixed = copy.deepcopy(pv_devices_30)
pv_devices_30_fixed[1]['power'] = 0.35*pv_devices_30_fixed[0]['power'] + \
    25*np.random.rand(*pv_devices_30_fixed[0]['power'].shape)
pv_devices_30_fixed[1]['time'] = pv_devices_30_fixed[0]['time']
pv_devices_30_fixed[3]['power'] = 0.35*pv_devices_30_fixed[0]['power'] + \
    30*np.random.rand(*pv_devices_30_fixed[0]['power'].shape)
pv_devices_30_fixed[3]['time'] = pv_devices_30_fixed[0]['time']

fig = plt.figure()
for pv_device in pv_devices_30_fixed:
    plt.plot(pv_device['time'], pv_device['power'])
plt.show()

KL_30_fixed = calculate_matrices(pv_devices_30_fixed)
corr_KL_30_fixed = np.corrcoef(KL_30_fixed.T)

plot_matrix(KL_30_fixed, 'KL')
plot_matrix(corr_KL_30_fixed, 'corrKL')