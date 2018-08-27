%%
% 计算GMM周边
%
% 功能：本函数包含计算概率分布周边的功能
%    a) 计算在给定点的概率密度函数值
%    b) 计算在给定点的积累概率函数值
%    c) 计算任意两个分布之间的KL散度
%    d) 计算任意两个边际分布之间的RMSE
%    e) 计算随机变量的线性函数的分布
% 
% 本函数输入如下
%    a) (必须输入) distribution:  GMM模型，
%       1) distribution.w: 联合分布或边际分布权重系数，1-by-J vector
%       2) distribution.mu: 联合分布或边际分布均值，J-by-d matrix
%       3) distribution.sigma: 联合分布或边际分布协方差，d-by-d-by-J martix
%    b) (必须输入) options: 输出选择,char
%       1）'pdf': 计算在给定点的概率密度函数值
%       2）'cdf': 计算在给定点的积累概率函数值
%       3) 'quantile': 计算输入分布的10%-100%分位数
%       4）'KL':  计算任意两个分布之间的KL散度
%       5）'RMSE':  计算任意两个分布之间的RMSE散度
%       6）'linear':  计算随机变量的线性函数的分布
%    c) (选择输入) y: 计算pdf或cdf时的给定点,1-by-d vector
%       e.g.: pdf = GMM_calculation(distribution,'pdf',y)
%       e.g.: cdf = GMM_calculation(distribution,'cdf',y)
%    d) (选择输入) distribution_other: 计算KL或RMSE时给定的另一个GMM模型
%       1) distribution_other.w: 联合分布或边际分布权重系数，1-by-J vector
%       2) distribution_other.mu: 联合分布或边际分布均值，J-by-d matrix
%       3) distribution_other.sigma: 联合分布或边际分布协方差，d-by-d-by-J martix
%       e.g.: KL = GMM_calculation(distribution,'KL',distribution_other)
%    e) (选择输入) x: 计算RMSE时变量的范围,N-by-d matrix
%       e.g.: RMSE = GMM_calculation(distribution,'RMSE',distribution_other,x)
%    f) (选择输入) A: 计算随机变量线性函数的分布时随机变量的系数矩阵, d-by-d matrix
%    g) (选择输入) b: 计算随机变量线性函数的分布时随机变量的常数矩阵, d-by-1 matrix
%       e.g.: distribution_AXplusb = GMM_calculation(distribution,'linear',A,b)
%    h) (选择输入) n_min,n_max: 计算输入分布的10%-100%分位数时随机变量的范围，float
%
% 本函数输出如下
%    a) pdf: 在给定点的概率密度函数值，float
%    b) cdf: 在给定点的积累概率函数值，float
%    c) quantile:计算输入分布的1%-100%分位数，float
%    d) KL: 任意两个分布之间的KL散度, float
%    e) RMSE: 任意两个分布之间的RMSE, float
%    f) distribution_AXplusb: 随机变量线性函数的分布，GMM模型，AXplusb -> Ax+b
%       1) distribution_AXplusb.w: 联合分布或边际分布权重系数，1-by-J vector
%       2) distribution_AXplusb.mu: 联合分布或边际分布均值，J-by-d matrix
%       3) distribution_AXplusb.sigma: 联合分布或边际分布协方差，d-by-d-by-J martix
%
% 注意：
%    全参数形式 [pdf,cdf,KL,RMSE,distribution] = GMM_calculation(distribution,options,y,distribution_other,x,A,b,n_min,n_max)
%    其中选择输入的y,distribution_other,x,A,b,n_min,n_max必须按照绝对顺序输入，可缺省，但绝对顺序不变

%% 函数
function varargout = GMM_calculation(distribution,options,varargin)

switch options
    
    case 'pdf'
        y = varargin{1};
        GMM = gmdistribution(distribution.mu,distribution.sigma,distribution.w');
        varargout{1} = pdf(GMM,y);
        
    case 'cdf'
        y = varargin{1};
        GMM = gmdistribution(distribution.mu,distribution.sigma,distribution.w');
        varargout{1} = cdf(GMM,y);
        
    case 'KL'
        distribution_other = varargin{1};
        GMM1 = gmdistribution(distribution.mu,distribution.sigma,distribution.w');
        GMM2 = gmdistribution(distribution_other.mu,distribution_other.sigma,distribution_other.w');
        varargout{1} = func_calculateKL(GMM1,GMM2);
        
    case 'RMSE'
        distribution_other = varargin{1};
        x = varargin{2};
        GMM1 = gmdistribution(distribution.mu,distribution.sigma,distribution.w');
        GMM2 = gmdistribution(distribution_other.mu,distribution_other.sigma,distribution_other.w');
        varargout{1} = func_calculateRMSE(GMM1,GMM2,x);
        
    case 'linear'
        A = varargin{1};
        b = varargin{2};
        J = size(distribution.mu,1);
        d = size(distribution.mu,2);
        varargout{1}.w =zeros(1,J);
        varargout{1}.mu = zeros(J,d);
        varargout{1}.sigma = zeros(d,d,J);
        for j = 1:J
            varargout{1}.w(j) = distribution.w(j);
            varargout{1}.mu(j,:) = (A*distribution.mu(j,:)'+b)';
            varargout{1}.sigma(:,:,j) = A*distribution.sigma(:,:,j)*A';
        end
        
    case 'quantile'
        [varargout{1},~] = func_quantile(distribution,varargin{1},varargin{2});
        
        
end
        
        
        
        
