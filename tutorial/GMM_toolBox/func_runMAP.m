%% 介绍
%
% 功能：最大后验计算概率分布

%% 函数
function distribution = func_runMAP(Y,J,Y_hyper,period)

warning off

% 定义相关计算参数
d = size(Y_hyper,2);         % 变量个数
N = size(Y_hyper,1)/period;  % 段数，也是GMM参数的组数
sigma_hyper = zeros(J*d,d,N);
w_hyper = zeros(J,1,N);
mu_hyper = zeros(J,d,N);

% 按多个时段计算多组GMM参数
for n = 1:N

    % 计算一组
    [w,mu,sigma] = func_runEM(Y_hyper((n-1)*period+1:n*period,:),J);

    % 记录多组
    for j=1:J
        sigma_hyper((j-1)*size(sigma,1)+1:j*size(sigma,1),:,n)=sigma(:,:,j);   % 每d行，也就是每numRan行，记录一个协方差矩阵
    end
    w_hyper(:,:,n) = w';
    mu_hyper(:,:,n) = mu;

end

% 形成超参数
[v,mu,tau,alpha,u] = func_hyperparameter(w_hyper,mu_hyper,sigma_hyper);

% 形成分布
Num = 1000;           % max iterative number
e = 10^(-3);          % convergent accuracy

% 初始化
weight0 = (v-1)/(sum(v) - J);  % 权重系数初值  (v-1)/(sum(v) - J)
mean0 = mu;                    % 均值初值
cov0 = zeros(d,d,J);           % 协方差初值
for j = 1:J
    cov0(:,:,j) = u(:,:,j)/(alpha(j) - d);      % 协方差
end

% 计算
for n = 1 : Num
    [weight,mean,cov] = func_map(Y',J,v,mu,tau,alpha,u,weight0,mean0,cov0);        
    % 判断是否收敛
    if norm(weight - weight0) <= e && norm(mean - mean0) <= e && max(max(max(cov - cov0))) <= e
        weight0 = weight;
        mean0 = mean;
        cov0 = cov;
        disp('收敛！');
        break;
    else
        weight0 = weight;
        mean0 = mean;
        cov0 = cov;
    end
end

distribution.w = weight;
distribution.mu = mean';
distribution.sigma = cov;