%% ����
% ���ܣ��γ������ֲ�
% ���룺���Ϸֲ�ģ�ͺ͸���ֵ
% ���ߣ�JMS
% ʱ�䣺2018-07-05

%% ����
function [distributioncw,distributioncmu,distributioncsigma] = func_generateConditional(distribution,y_given)

% ��ø�˹����
J = length(distribution.w);

% ׼������
sum_w = 0;
for j = 1:J
    sum_w = sum_w + distribution.w(j) * mvnpdf(y_given,distribution.mu(j,2:end),distribution.sigma(2:end,2:end,j));
end

% ����
distributioncw = zeros(1,J);
distributioncmu = zeros(J,1);
distributioncsigma = zeros(1,1,J);
for j = 1:J
    
    % Ȩ��
    distributioncw(j) = (distribution.w(j) * mvnpdf(y_given,distribution.mu(j,2:end),distribution.sigma(2:end,2:end,j))) / sum_w ;
    
    % ��ֵ
    distributioncmu(j) = distribution.mu(j,1) + (distribution.sigma(1,2:end,j)/(distribution.sigma(2:end,2:end,j)))*(y_given'-distribution.mu(j,2:end)');
    
    % Э����
    distributioncsigma(1,1,j) = distribution.sigma(1,1,j) - (distribution.sigma(1,2:end,j)/(distribution.sigma(2:end,2:end,j)))*distribution.sigma(1,2:end,j)';
    
end
