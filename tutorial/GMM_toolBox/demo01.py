import matlab.engine
import matlab
import numpy as np
import random


engine = matlab.engine.start_matlab()
array = matlab.double([[(random.random() - np.random.randn()) * 100000 // 1 / 10000] for x in range(1000)])
# array = matlab.double([[0,0,0,0,0,0,0,0]])
print(len(array))
print(array)
num = matlab.int8([5])
distribution = engine.GMM_Distribution(array, num, 'EM', 'marginal')
print(distribution)

x = matlab.double([[x*10//1/10] for x in np.arange(0, 50, 0.1)])
print(x)
print(len(x))

engine.GMM_plot(distribution, 'singlePDF', x, nargout=0)
# engine.GMM_plot(distribution, 'singlePDF', x, nargout=0)
