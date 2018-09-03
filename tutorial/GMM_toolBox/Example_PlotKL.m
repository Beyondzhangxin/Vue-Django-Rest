%% 示例
%
% 绘制KLD

%% 输入训练集
Y1 = 15*rand(1000,1)+2*randn(1000,1)+20;
Y2 = 12*rand(1000,1)+5*randn(1000,1)+30;
Y3 = 10*rand(1000,1)+8*randn(1000,1)+40;
Y4 = 9*rand(1000,1)+11*randn(1000,1)+50;
Y5 = 7*rand(1000,1)+14*randn(1000,1)-20;
Y6 = 5*rand(1000,1)+17*randn(1000,1)-30;
Y7 = 3*rand(1000,1)+20*randn(1000,1)-40;


%% 构建单维变量的概率分布
distribution1 = GMM_Distribution(Y1,5,'EM','marginal');  % 选用EM算法,阶数选择为5
distribution2 = GMM_Distribution(Y2,5,'EM','marginal');  % 选用EM算法,阶数选择为5
distribution3 = GMM_Distribution(Y3,5,'EM','marginal');  % 选用EM算法,阶数选择为5
distribution4 = GMM_Distribution(Y4,5,'EM','marginal');  % 选用EM算法,阶数选择为5
distribution5 = GMM_Distribution(Y5,5,'EM','marginal');  % 选用EM算法,阶数选择为5
distribution6 = GMM_Distribution(Y6,5,'EM','marginal');  % 选用EM算法,阶数选择为5
distribution7 = GMM_Distribution(Y7,5,'EM','marginal');  % 选用EM算法,阶数选择为5

%% 计算KLD和RMSE
x = [0:0.1:100]';
KL(1) = GMM_calculation(distribution1,'KL',distribution2);
KL(2) = GMM_calculation(distribution1,'KL',distribution3);
KL(3) = GMM_calculation(distribution1,'KL',distribution4);
KL(4) = GMM_calculation(distribution1,'KL',distribution5);
KL(5) = GMM_calculation(distribution1,'KL',distribution6);
KL(6) = GMM_calculation(distribution1,'KL',distribution7);

RMSE(1) = GMM_calculation(distribution1,'RMSE',distribution2,x);
RMSE(2) = GMM_calculation(distribution1,'RMSE',distribution3,x);
RMSE(3) = GMM_calculation(distribution1,'RMSE',distribution4,x);
RMSE(4) = GMM_calculation(distribution1,'RMSE',distribution5,x);
RMSE(5) = GMM_calculation(distribution1,'RMSE',distribution6,x);
RMSE(6) = GMM_calculation(distribution1,'RMSE',distribution7,x);

%% 绘制
x = [0:0.1:100]';
GMM_plot(distribution1,'singlePDF',x); 
hold on
GMM_plot(distribution2,'singlePDF',x); 
hold on
GMM_plot(distribution3,'singlePDF',x); 
hold on
GMM_plot(distribution4,'singlePDF',x); 
hold on
GMM_plot(distribution5,'singlePDF',x); 
hold on
GMM_plot(distribution6,'singlePDF',x); 
hold on
GMM_plot(distribution7,'singlePDF',x); 

legend('Standard','Distribution 1','Distribution 2'...
                              ,'Distribution 3'...
                              ,'Distribution 4'...
                              ,'Distribution 5'...
                              ,'Distribution 6');
figure;
bar(KL);

