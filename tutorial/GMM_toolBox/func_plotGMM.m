%% 介绍
%
% 功能：绘制GMM的PDF

%% 函数
function func_plotGMM(GMM,x)

plot(x,pdf(GMM,x))
