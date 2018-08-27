%% 示例
%
% 绘制单维变量CDF

%% 输入训练集
Y = 15*rand(1000,1)+2*randn(1000,1)+20;

%% 构建单维变量的概率分布
distribution = GMM_Distribution(Y,5,'EM','marginal');  % 选用EM算法,阶数选择为5

%% 绘制
x = [0:0.1:30]';
GMM_plot(distribution,'singleCDF',x); 


