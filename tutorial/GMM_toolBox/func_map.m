function [weight,mean,cov] = func_map(y,J,v,mu,tau,alpha,u,weight,mean,cov)
%% Introduction
%
% This function aims to realize the process of Centralized MAP via obtain
% all sample
%
% Author: JMS
% Date: 2017-12-12

%% Input
d = size(y,1);       % ����������Ŀǰ��2ά��һ��Ԥ�������һ��ʵ�ʳ���.d�������е��±���У�����������̬�ֲ�ʱά�Ȳ���ȷ
N = size(y,2);       % �۲������� - �±�Ϊi
detcov = zeros(J,1);          % Э���������ʽ
invcov = zeros(d,d,J);        % Э�������

%% ����ͳ����
for j = 1:J                   % ����Э���������ʽ���棬�������
    detcov(j) = det(cov(:,:,j));
    invcov(:,:,j) = inv(cov(:,:,j));
end

% ����C
Cji = zeros(J,N);
for i = 1:N
    allnorm = 0;
    for j = 1:J
        Cji(j,i) = weight(j)*((2*pi)^(-d/2))*(detcov(j)^(-0.5))*exp(-0.5*(y(:,i)-mean(:,j))'*invcov(:,:,j)*(y(:,i)-mean(:,j)));
        allnorm = allnorm + Cji(j,i);
    end
    Cji(:,i) = Cji(:,i)/allnorm;
end

Cj = sum(Cji,2);            % ά��ΪJ,������

% �����ֵy
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
Betaj = sum(Yji,3);                % ά��Ϊd*J
Gammaj = sum(Zji,3);               % ά��ͬ��
Omega = sum(Xji,4);                % ά��Ϊd*d*J
Yj = Betaj;                        % ��һ��������
Yj(1,:) = Betaj(1,:)./Cj';
Yj(2,:) = Betaj(2,:)./Cj';

% ����S
Sji = zeros(d,d,J,N);
for j = 1:J
    for i = 1:N
        Sji(:,:,j,i) = Cji(j,i)*(y(:,i)-Yj(:,j))*(y(:,i)-Yj(:,j))';
    end
end

Sj = sum(Sji,4);        % ά��Ϊd*d*J

% ��һ�ַ�ʽ����S
Sjtest = zeros(d,d,J);
for j = 1:J
    Sjtest(:,:,j) = Omega(:,:,j) + Yj(:,j)*Yj(:,j)'*Cj(j) - Betaj(:,j)*Yj(:,j)' - Yj(:,j)*Gammaj(j,:);
end

%% ����GMM����
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

        
        



    




