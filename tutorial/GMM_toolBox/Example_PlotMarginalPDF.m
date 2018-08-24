%% 示例
%
% 绘制单维变量PDF以及测试集直方图

%% 输入训练集
Y = 10*rand(1000,1)+randn(1000,1);
x = [-4:0.1:12]';

%% 构建单维变量的概率分布
distribution = GMM_Distribution(Y,5,'EM','marginal');  % 选用EM算法,阶数选择为5

%% 给定测试集，测试集可有不同的样本，但必须和训练集服从相同的分布
Y_test = 10*rand(500,1)+randn(500,1);

%% 绘制
GMM_plot(distribution,'testPDF',x,Y_test,15); 