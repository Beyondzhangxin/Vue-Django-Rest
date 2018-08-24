%% 介绍
% 功能：形成条件分布
% 输入：联合分布模型和给定值
% 作者：JMS
% 时间：2018-07-05

%% 函数
function [distributioncw,distributioncmu,distributioncsigma] = func_generateConditional(distribution,y_given)

% 获得高斯个数
J = length(distribution.w);

% 准备工作
sum_w = 0;
for j = 1:J
    sum_w = sum_w + distribution.w(j) * mvnpdf(y_given,distribution.mu(j,2:end),distribution.sigma(2:end,2:end,j));
end

% 计算
distributioncw = zeros(1,J);
distributioncmu = zeros(J,1);
distributioncsigma = zeros(1,1,J);
for j = 1:J
    
    % 权重
    distributioncw(j) = (distribution.w(j) * mvnpdf(y_given,distribution.mu(j,2:end),distribution.sigma(2:end,2:end,j))) / sum_w ;
    
    % 均值
    distributioncmu(j) = distribution.mu(j,1) + (distribution.sigma(1,2:end,j)/(distribution.sigma(2:end,2:end,j)))*(y_given'-distribution.mu(j,2:end)');
    
    % 协方差
    distributioncsigma(1,1,j) = distribution.sigma(1,1,j) - (distribution.sigma(1,2:end,j)/(distribution.sigma(2:end,2:end,j)))*distribution.sigma(1,2:end,j)';
    
end
