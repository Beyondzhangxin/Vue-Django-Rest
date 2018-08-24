%% 介绍
%
% 功能：绘制直方图
% 输入：经验数据的列向量
%      绘制多少个区间
% 
% 作者：JMS
% 时间：2018-06-09

%% 函数
function func_plotHist(data_vector,num_interval)
c = data_vector;
[a,b]=hist(c,num_interval);              % 分为若干个区间统计频数，y为每个区间中的预测出力的频数，x为本区间的中心值
a=a/length(c)/(b(2)-b(1));   % 计算概率密度，频数除以数据种数，除以组距
bar(b,a,1,'Facecolor',[1,1,1]);  