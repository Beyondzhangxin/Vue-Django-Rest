%% 介绍
%
% 功能：计算两个GMM之间的拟合差异，基于RMSE
% 输入：两个GMM的模型,以及随机变量的范围
% 输出：两个GMM模型PDF曲线的RMSE
% 作者：JMS
% 时间：2018-07-07

%% 函数
function RMSE = func_calculateRMSE(GMMp,GMMq,x)

% 形成两个GMM的PDF的数组
GMMp_vector = pdf(GMMp,x);
GMMq_vector = pdf(GMMq,x);

% 计算RMSE值
RMSE_vector = GMMp_vector - GMMq_vector;
RMSE_vector2 = RMSE_vector.*RMSE_vector;
RMSE = sqrt(sum(RMSE_vector2)/length(x));

    
