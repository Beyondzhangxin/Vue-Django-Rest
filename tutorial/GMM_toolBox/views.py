
from rest_framework.views import APIView
from rest_framework.response import Response
import matlab.engine
import matlab
import json
import functools
import matlab.engine
# Create your views here.

# 错误wapper


def dealException(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        result = 0
        try:
            result = func(*args, **kw)
        except Exception as e:
          return {'exception': e}
        return 0
    return wrapper


def matlabEngineEnv():
    # 开始运行matlab engine
    engine = matlab.engine.start_matlab()
    return engine


class Distribution(APIView):

    def __init__(self):
        self._Y = None
        self._J = None
        self._options = None

    #为满足正常的赋值以及和matlab兼容的赋值
    @property
    def Y(self):
        return self._Y

    @Y.setter
    def Y(self, value):
        self._Y = value
    
    @property
    def J(self):
        return self._J


    @J.setter
    def J(self, value):
        self._J = value

    @property
    def method(self):
        return self._method

    @method.setter
    def method(self, value):
        self._Y = value

    @property
    def options(self):
        return self._options

    @options.setter
    def options(self, value):
        self._options = value

    def model(self, data):
        pass

    def post(self, request, format=None):
        jsonFormatData = self.model(request.data)
        return Response(jsonFormatData)


# GMM_Distribution函数
# 输入单维训练集Y，vector(向量)
# 输入GMM阶数J，int
# 输入option = 'marginal'
# 输入算法选项 method，str

class Marginal(Distribution):
    def model(self, data):
        engine = matlabEngineEnv()
        y = data.get('vector')
        j = data.get('J')
        option = 'marginal'
        # 纵向量
        # 将数据封装成matlab格式
        array = matlab.double([y])
        J = matlab.int8([j])
        return engine.GMM_Distribution(array, J, 'EM', option)


# GMM_Distribution函数
# 输入多维训练集Y，matrix(矩阵)
# 输入GMM阶数J，int
# 输入option = 'marginal'
# 输入算法选项 method，str

class Joint(Distribution):
    def model(self, data):
        engine = matlabEngineEnv()
        y = data.get('matrix')
        j = data.get('J')
        method = data.get('method')
        option = 'marginal'
        array = matlab.double([y])
        j = matlab.int8([j])
        return engine.GMM_Distribution(array, j, 'EM', option)
    
# GMM_Distribution函数
# 输入多维训练集 Y，matrix
# 输入GMM阶数 J，int
# 输入option=‘conditional’
# 输入算法选项 method，str
# 输入给定条件值 y，vector


class Conditional(Distribution):
    def model(self, data):
        engine = matlabEngineEnv()
        y1 = data.get('matrix')
        y2 = data.get('vector')
        j = data.get('J')
        method = data.get('method')
        option = 'conditional'
        array = matlab.double([y1])
        vector = matlab.double([y2])
        j = matlab.int8([j])
        return engine.GMM_Distribution(array, j, 'EM', option, y2)


# GMM_Distribution函数
# 输入多维训练集 Y，matrix
# 输入GMM阶数 J，int
# 输入算法选项 method=‘EM’


class EM(Distribution):
    def model(self, data):
        engine = matlabEngineEnv()
        y = data.get('matrix')
        j = data.get('J')
        array = matlab.double([y])
        j = matlab.int8([j])
        return engine.GMM_Distribution(array, j, 'EM')

# GMM_Distribution函数
# 输入多维训练集 Y，matrix
# 输入GMM阶数 J，int
# 输入算法选项 method=‘MAP’


class MAP(Distribution):
    def model(self, data):
        engine = matlabEngineEnv()
        pass 


class Calculation(APIView):
    def model(self, data):
        pass

    def post(self, request, format=None):
        self.model(request.data)
        return Response(123)

# 计算给定点PDF值
# GMM_calculation函数
# 输入GMM分布 distribution
# 输入给定点值 x，float
# 输入选项 option=‘PDF


class PDF(Calculation):
    def model(self, data):
        pass

# 计算给定的CDF值
# GMM_calculation函数
# 输入GMM分布 distribution
# 输入给定点值 x，float
# 输入选项 option=‘CDF’


class CDF(Calculation):
    def model(self, data):
        pass

# 计算分位数
# GMM_calculation函数
# 输入GMM分布 distribution
# 输入给样本范围
# 输入选项 option=‘quantile


class Quantile(Calculation):
    def model(self, data):
        pass

# 计算分布间KLD值 
# 计算分布间RMSE

# GMM_calculation函数
# 输入两个GMM分布 distribution
# 输入选项 option=‘KL


class KL(Calculation):
    def model(self, data):
        pass


class RMSE(Calculation):
    def model(self, data):
        pass

# 计算线性变换分布
# GMM_calculation函数
# 输入GMM分布 distribution
# 输入线性变化系数 A和b
# 输入选项 option=‘linear’


class Linear(Calculation):
    def model(self, data):
        pass