%% ����
%
% ���ܣ������λ��
% ���룺GMMģ�ͣ�gmdistribution
% �������λ��
% 
% ���ߣ�JMS
% ʱ�䣺2018-06-08

%% ����
function [quantile,quantile_test] = func_quantile(GMMdistribution,n_min,n_max)
% �γ�GMMģ��
GMM = gmdistribution(GMMdistribution.mu,GMMdistribution.sigma,GMMdistribution.w');
% ��һ����������cdf����
n = 1;
probability = zeros(10000,2);
for i = n_min:0.001:n_max
    probability(n,1) = i;
    probability(n,2) = cdf(GMM,i);
    n = n + 1;
end
% ������Ӧ��λ��
quantile = zeros(100,1);
quantile_test = zeros(100,1);
for i = 1:100
    [~,quantile_index] = min(abs(probability(:,2)-0.01*i));   % Ѱ�Һ�0.01*i����ӵ�����
    quantile(i) = probability(quantile_index,1);
    quantile_test(i) = cdf(GMM,quantile(i));    % ����
end
