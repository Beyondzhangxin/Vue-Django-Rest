function [weight,mean,cov] = func_map(y,J,v,mu,tau,alpha,u,weight,mean,cov)
%% Introduction
%
% This function aims to realize the process of Centralized MAP via obtain
% all sample
%
% Author: JMS
% Date: 2017-12-12

%% Input
d = size(y,1);       % 变量个数，目前是2维，一个预测出力，一个实际出力.d必须是行的下标才行，这样在求正态分布时维度才正确
N = size(y,2);       % 观测量个数 - 下标为i
detcov = zeros(J,1);          % 协方差的行列式
invcov = zeros(d,d,J);        % 协方差的逆

%% 计算统计量
for j = 1:J                   % 计算协方差的行列式和逆，后面调用
    detcov(j) = det(cov(:,:,j));
    invcov(:,:,j) = inv(cov(:,:,j));
end

% 计算C
Cji = zeros(J,N);
for i = 1:N
    allnorm = 0;
    for j = 1:J
        Cji(j,i) = weight(j)*((2*pi)^(-d/2))*(detcov(j)^(-0.5))*exp(-0.5*(y(:,i)-mean(:,j))'*invcov(:,:,j)*(y(:,i)-mean(:,j)));
        allnorm = allnorm + Cji(j,i);
    end
    Cji(:,i) = Cji(:,i)/allnorm;
end

Cj = sum(Cji,2);            % 维度为J,列向量

% 计算均值y
Yji = zeros(d,J,N);
Zji = zeros(J,d,N);
Xji = zeros(d,d,J,N);
for j = 1:J
    for i = 1:N
        Yji(:,j,i) = Cji(j,i)*y(:,i);
        Zji(j,:,i) = Cji(j,i)*y(:,i)';
        Xji(:,:,j,i) = Cji(j,i)*y(:,i)*y(:,i)';
    end
end
Betaj = sum(Yji,3);                % 维度为d*J
Gammaj = sum(Zji,3);               % 维度同上
Omega = sum(Xji,4);                % 维度为d*d*J
Yj = Betaj;                        % 给一个矩阵框架
Yj(1,:) = Betaj(1,:)./Cj';
Yj(2,:) = Betaj(2,:)./Cj';

% 计算S
Sji = zeros(d,d,J,N);
for j = 1:J
    for i = 1:N
        Sji(:,:,j,i) = Cji(j,i)*(y(:,i)-Yj(:,j))*(y(:,i)-Yj(:,j))';
    end
end

Sj = sum(Sji,4);        % 维度为d*d*J

% 另一种方式计算S
Sjtest = zeros(d,d,J);
for j = 1:J
    Sjtest(:,:,j) = Omega(:,:,j) + Yj(:,j)*Yj(:,j)'*Cj(j) - Betaj(:,j)*Yj(:,j)' - Yj(:,j)*Gammaj(j,:);
end

%% 更新GMM参数
sji = zeros(d,d,N);
weight = (v -1 + Cj)/(sum(v) - J + sum(Cj));
for j = 1:J
%     weight(j) = (v(j) - 1 + Cj(j))/(sum(v) - J + sum(Cj));
    mean(:,j) = (tau(j)*mu(:,j)+Betaj(:,j))/(tau(j)+Cj(j));
    for i = 1:N
        sji(:,:,i) = Cji(j,i)*(y(:,i)-mean(:,j))*(y(:,i)-mean(:,j))';
    end
    cov(:,:,j) = (u(:,:,j) + sum(sji,3) + tau(j)*(mu(:,j) - mean(:,j))*(mu(:,j) - mean(:,j))')/(alpha(j) - d + Cj(j));
%     cov(:,:,j) = (u(:,:,j) + Sj(:,:,j) + (tau(j)*Cj(j)/(tau(j)+Cj(j)))*(mu(:,j) - Yj(:,j))*(mu(:,j) - Yj(:,j))')/(alpha(j) - d + Cj(j));
end

        
        



    




