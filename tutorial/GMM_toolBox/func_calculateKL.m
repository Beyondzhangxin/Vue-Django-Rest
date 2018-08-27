%% 介绍
%
% 功能：计算两个GMM之间的拟合差异
% 输入：两个GMM的模型
% 输出：基于EMD和KLD的拟合差异值，越值越大，说明两个GMM之间的距离越远，其相似性越小; 反之该值越小，相似性越大
% 作者：JMS
% 时间：2018-07-07

%% 函数
function KLDEMD = func_calculateKL(GMMp,GMMq)

% 参数读取
Num_J = size(GMMp.ComponentProportion,2);  % component个数
d = size(GMMp.Sigma,1);

% 线性规划参数设置
D = zeros(Num_J,Num_J);    % 距离矩阵，其实没必要存储
f = zeros(Num_J*Num_J,1);  % 目标函数系数列向量
A_up = zeros(Num_J,Num_J*Num_J);  % 不等式约束系数矩阵,上半部分
A_down = zeros(Num_J,Num_J*Num_J);  % 不等式约束系数矩阵,下半部分，两者串联为最终的A
b = zeros(2*Num_J,1);    % 不等式约束列向量
lb = zeros(Num_J*Num_J,1);  % 下界约束
Aeq = ones(1,Num_J*Num_J);  % 等式约束系数矩阵
beq = 1;                    % 等式约束列向量

% 形成目标函数系数列向量f
m = 1; % 计数器
for i = 1:Num_J
    for j = 1:Num_J
        KLDij = 0.5* (...
                log(det(GMMq.Sigma(:,:,j))/det(GMMp.Sigma(:,:,i))) + ...
                trace(inv(GMMq.Sigma(:,:,j))*GMMp.Sigma(:,:,i)) + ...
                (GMMp.mu(i,:) - GMMq.mu(j,:))*inv(GMMq.Sigma(:,:,j))*(GMMp.mu(i,:) - GMMq.mu(j,:))' - d ...
                );
        KLDji = 0.5* (...
                log(det(GMMp.Sigma(:,:,i))/det(GMMq.Sigma(:,:,j))) + ...
                trace(inv(GMMp.Sigma(:,:,i))*GMMq.Sigma(:,:,j)) + ...
                (GMMq.mu(j,:) - GMMp.mu(i,:))*inv(GMMp.Sigma(:,:,i))*(GMMq.mu(j,:) - GMMp.mu(i,:))' - d ...
                );
        D(i,j) = 0.5*(KLDij+KLDji);
        % 由D直接形成线性规划中的目标函数系数列向量
        f(m) = D(i,j);
        m = m + 1;
    end
end

% 形成不等式约束系数矩阵A
for n = 1:Num_J
    A_up(n,(n-1)*Num_J+1:n*Num_J) = 1;
    A_down(n,n:Num_J:(Num_J-1)*Num_J+n) = 1;
end
A = [A_up;A_down];

% 形成不等式约束列向量
b_up = GMMp.ComponentProportion';
b_down = GMMq.ComponentProportion';
b = [b_up;b_down];

% 求解线性规划
[~,KLDEMD] = linprog(f,A,b,Aeq,beq,lb,[],[]);
    
