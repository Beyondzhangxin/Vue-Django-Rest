%% ʾ��
%
% ���Ƶ�ά����CDF

%% ����ѵ����
Y = 15*rand(1000,1)+2*randn(1000,1)+20;

%% ������ά�����ĸ��ʷֲ�
distribution = GMM_Distribution(Y,5,'EM','marginal');  % ѡ��EM�㷨,����ѡ��Ϊ5

%% ����
x = [0:0.1:30]';
GMM_plot(distribution,'singleCDF',x); 


