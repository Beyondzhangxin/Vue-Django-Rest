%% 介绍
%
% 功能：计算分位数
% 输入：GMM模型：gmdistribution
% 输出：分位数
% 
% 作者：JMS
% 时间：2018-06-08

%% 函数
function [quantile,quantile_test] = func_quantile(GMMdistribution,n_min,n_max)
% 形成GMM模型
GMM = gmdistribution(GMMdistribution.mu,GMMdistribution.sigma,GMMdistribution.w');
% 按一定步长生成cdf概率
n = 1;
probability = zeros(10000,2);
for i = n_min:0.001:n_max
    probability(n,1) = i;
    probability(n,2) = cdf(GMM,i);
    n = n + 1;
end
% 搜索对应分位数
quantile = zeros(100,1);
quantile_test = zeros(100,1);
for i = 1:100
    [~,quantile_index] = min(abs(probability(:,2)-0.01*i));   % 寻找和0.01*i最近接的行数
    quantile(i) = probability(quantile_index,1);
    quantile_test(i) = cdf(GMM,quantile(i));    % 检验
end
