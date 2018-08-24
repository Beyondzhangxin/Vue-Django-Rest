%% Introduction
%
% ��������GMM������������������ס���̬-����ɳ�طֲ��ĳ�������
% ���ߣ�JMS
% ʱ�䣺2017-12-20

function [v,mu,tau,alpha,u] = func_hyperparameter(wGMM,miuGMM,sigmaGMM)

%% ȫ���½Ǳ�
N = size(wGMM,3);     % ������������
J = size(wGMM,1);     % Mc����
d = size(miuGMM,2);   % ����ά��

%% ����wGMM���ӵĵ������׷ֲ��ĳ�����v
strength = 1000;       % ������v��ǿ��ϵ����Խ�󳬲���Խǿ��������100����ʹv�����϶�����1
A = zeros(J,J);
for j = 1:J
    A(j,:) = sum(wGMM(j,:,:));
end
v = strength*A(:,1)/N;         % ��������ֵ����v
% % ����η��������v
% one = ones(1,J);
% one = diag(one);      % ��õ�λ�Խ���
% A = A/N - one;      % ���ϵ������
% [~,v] = solveLS(A,zeros(size(A,1),1));   % ֱ�����˷������������⣬Ϊ�ˣ�Ҫôѡ��A��һ����Ϊv��Ҫô���뷽��ļ���
% % �����Թ滮���v
% v = sdpvar(J,1);
% f = 0;
% for j = 1:J
%     f = f + abs(A(j,:)*v);
% end
% F = [v > 0];
% result = solvesdp(F,f);
% v = double(v);
    
%% ����miuGMM���ӵ�������̬�ֲ��ĳ�����mu
mu = zeros(J,d);      % ����d=2�������������1��2��ʾ
for j = 1:J
    mu(j,1) = sum(miuGMM(j,1,:))/N;
    mu(j,2) = sum(miuGMM(j,2,:))/N;
end

%% ����miuGMM���ӵ���̬�ֲ��ĳ�����tau����̬�ֲ�����Ϊ�������������ֵ��tau�ı�ֵ

% ���ȼ���miuGMM����������Э�����miuSIGMA��ʾ
miuGMMT = permute(miuGMM,[3,2,1]);
miuSIGMA = zeros(d,d,J);          % miuSIGMA�ĵ���ά��Mc�ĸ���
for j = 1:J
    miuSIGMA(:,:,j) = cov(miuGMMT(:,:,j));
end

% ��μ���sigmaGMM���������ľ�ֵ����sigmaBAR��ʾ��ͬʱ����precisionBAR����sigmaBAR�ĵ�����Ϊ�˼������ĳ�����
sigmaTemp = sum(sigmaGMM,3);
sigmaBAR = zeros(d,d,J);              % sigmaBAR�ĵ���ά��Mc�ĸ���
precisionBAR = zeros(d,d,J);          % precisionBAR��sigmaBAR�ĵ����������ά��Mc�ĸ���
for j = 1:J
    sigmaBAR(:,:,j) = sigmaTemp((j-1)*d+1:j*d,:);
    precisionBAR(:,:,j) = inv(sigmaBAR(:,:,j));
end

% Ȼ�󹹽��Ż��������tau��ÿ��j����һ���Ż�����
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

%% ����sigmaGMM�ĵ������ӵ���ɳ�طֲ��ĳ�����alpha�ͳ�����u
u = zeros(d,d,J);
alpha = zeros(J,1);
for j = 1:J
    iux = sdpvar(d,d);      % ����ux����
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
    u(:,:,j) = inv(iux);   % ��iux��������
    alpha(j) = alphax;
end

mu = mu';    % Ϊ�˷�������ļ���

    




