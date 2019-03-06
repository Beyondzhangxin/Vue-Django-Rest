import scipy.io as scio
import numpy as np
import datetime
import matplotlib.pyplot as plt

# load data
from tutorial.GMM_toolBox import functional
from tutorial.GMM_toolBox.GMM_Distribution import GMM_distribution

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
            for idx_time_end in range(idx_time_start,
                                      len(pv_devices[idx_device]['time'])):
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
    return pv_devices_


pv_devices_30 = get_devices(30)
# 建立GMM模型
GMMs_30 = list()
for pv_device in pv_devices_30:
    GMMs_30.append(GMM_distribution(
        pv_device['power'], 3, 'EM', 'marginal')['GMM'])
# 画GMM模型的pdf
functional.plot_pdf(GMMs_30[6], -200, 300)
# 画GMM模型的cdf
functional.plot_cdf(GMMs_30[6], -200, 300)