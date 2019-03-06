import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 输入训练集
from tutorial.GMM_toolBox.GMM_Distribution import GMM_distribution

Y1 = 10*np.random.rand(1000, 1)+np.random.randn(1000, 1)
Y2 = 15*np.random.rand(1000, 1)+3*np.random.randn(1000, 1)
Y = np.concatenate((Y1, Y2), axis=1)
x = np.linspace(-4, 12, 100)
y = np.linspace(-10, 22, 100)

# 构建联合概率分布
joint_distribution = GMM_distribution(Y, 5, 'EM', 'joint')
# 画pdf
x, y = np.meshgrid(x, y)
sample_points = np.hstack((x.flatten().reshape((-1, 1)), y.flatten().transpose().reshape((-1, 1))))
log_pdf = joint_distribution['GMM'].score_samples(sample_points)
pdf = np.exp(log_pdf)
pdf = np.reshape(pdf, x.shape)

fig = plt.figure()
fig.set_tight_layout(False)
ax = Axes3D(fig)
ax.plot_surface(x, y, pdf, cmap=plt.get_cmap('rainbow'))
plt.show()
