%% 示例
%
% 绘制单维变量PDF以及测试集直方图

%% 输入训练集
Y1 = 10*rand(1000,1)+randn(1000,1);
Y2 = 15*rand(1000,1)+3*randn(1000,1);
Y = [Y1,Y2];
x = [-4:0.1:12]';
y = [-10:0.2:22]';

%% 构建单维变量的概率分布
distribution = GMM_Distribution(Y,5,'EM','joint');  % 选用EM算法,阶数选择为5

%% 绘制
GMM_plot(distribution,'testPDF',x,y); 