%% 示例
%
% 绘制线性变换

%% 输入训练集
Y = 15*rand(1000,1)+2*randn(1000,1);

%% 输入线性变换系数
A = 0.5;
b = 7;

%% 构建单维变量的概率分布
distribution = GMM_Distribution(Y,5,'EM','marginal');  % 选用EM算法,阶数选择为5

%% 计算线性变换分布
distribution_AXplusb = GMM_calculation(distribution,'linear',A,b);

%% 构建线性变换分布
distribution_AXplusb_test = GMM_Distribution(A*Y+b,5,'EM','marginal');  % 选用EM算法,阶数选择为5


%% 绘制
x = [-10:0.1:30]';
GMM_plot(distribution,'singlePDF',x); 
hold on
GMM_plot(distribution_AXplusb,'singlePDF',x); 
hold on
GMM_plot(distribution_AXplusb_test,'singlePDF',x); 


