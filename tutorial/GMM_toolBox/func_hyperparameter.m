%% Introduction
%
% 本程序用GMM参数样本计算狄利克雷、正态-逆威沙特分布的超参数。
% 作者：JMS
% 时间：2017-12-20

function [v,mu,tau,alpha,u] = func_hyperparameter(wGMM,miuGMM,sigmaGMM)

%% 全局下角标
N = size(wGMM,3);     % 参数样本组数
J = size(wGMM,1);     % Mc个数
d = size(miuGMM,2);   % 变量维度

%% 计算wGMM服从的狄利克雷分布的超参数v
strength = 1000;       % 超参数v的强度系数，越大超参数越强，这里用100可以使v基本上都大于1
A = zeros(J,J);
for j = 1:J
    A(j,:) = sum(wGMM(j,:,:));
end
v = strength*A(:,1)/N;         % 用样本均值代替v
% % 求齐次方程组求解v
% one = ones(1,J);
% one = diag(one);      % 获得单位对角阵
% A = A/N - one;      % 获得系数矩阵
% [~,v] = solveLS(A,zeros(size(A,1),1));   % 直接求解此方程有无穷多组解，为此，要么选择A的一列作为v，要么加入方差的计算
% % 求线性规划求解v
% v = sdpvar(J,1);
% f = 0;
% for j = 1:J
%     f = f + abs(A(j,:)*v);
% end
% F = [v > 0];
% result = solvesdp(F,f);
% v = double(v);
    
%% 计算miuGMM服从的条件正态分布的超参数mu
mu = zeros(J,d);      % 这里d=2，所以下面才用1和2表示
for j = 1:J
    mu(j,1) = sum(miuGMM(j,1,:))/N;
    mu(j,2) = sum(miuGMM(j,2,:))/N;
end

%% 计算miuGMM服从的正态分布的超参数tau，正态分布方差为参数样本方差均值与tau的比值

% 首先计算miuGMM参数样本的协方差，用miuSIGMA表示
miuGMMT = permute(miuGMM,[3,2,1]);
miuSIGMA = zeros(d,d,J);          % miuSIGMA的第三维是Mc的个数
for j = 1:J
    miuSIGMA(:,:,j) = cov(miuGMMT(:,:,j));
end

% 其次计算sigmaGMM参数样本的均值，用sigmaBAR表示；同时计算precisionBAR，是sigmaBAR的倒数，为了计算后面的超参数
sigmaTemp = sum(sigmaGMM,3);
sigmaBAR = zeros(d,d,J);              % sigmaBAR的第三维是Mc的个数
precisionBAR = zeros(d,d,J);          % precisionBAR是sigmaBAR的倒数，其第三维是Mc的个数
for j = 1:J
    sigmaBAR(:,:,j) = sigmaTemp((j-1)*d+1:j*d,:);
    precisionBAR(:,:,j) = inv(sigmaBAR(:,:,j));
end

% 然后构建优化问题求解tau，每个j都是一个优化问题
tau = zeros(J,1);
for j = 1:J
    taux = sdpvar(1,1);
    f = abs(taux*miuSIGMA(1,1,j)-sigmaBAR(1,1,j)) + ...
        abs(taux*miuSIGMA(1,2,j)-sigmaBAR(1,2,j)) + ...
        abs(taux*miuSIGMA(2,1,j)-sigmaBAR(2,1,j)) + ...
        abs(taux*miuSIGMA(2,2,j)-sigmaBAR(2,2,j));
    F = [taux > 0];
    result = solvesdp(F,f);
    taux = double(taux);
    tau(j) = taux;
end

%% 计算sigmaGMM的倒数服从的威沙特分布的超参数alpha和超参数u
u = zeros(d,d,J);
alpha = zeros(J,1);
for j = 1:J
    iux = sdpvar(d,d);      % 代表ux的逆
    alphax = sdpvar(1,1);
    sum_temp = 0;
    for n1 = 1:d
        for n2 = 1:d
            sum_temp = sum_temp + abs(precisionBAR(n1,n2,j) - alphax*iux(n1,n2));
        end
    end
    f = sum_temp;
    F = [alphax > d-1];
    result = solvesdp(F,f);
    alphax = double(alphax);
    iux = double(iux);
    u(:,:,j) = inv(iux);   % 对iux重新求逆
    alpha(j) = alphax;
end

mu = mu';    % 为了方便后续的计算

    




