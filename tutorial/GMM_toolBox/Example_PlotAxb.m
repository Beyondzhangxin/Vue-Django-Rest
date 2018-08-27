%% ʾ��
%
% �������Ա任

%% ����ѵ����
Y = 15*rand(1000,1)+2*randn(1000,1);

%% �������Ա任ϵ��
A = 0.5;
b = 7;

%% ������ά�����ĸ��ʷֲ�
distribution = GMM_Distribution(Y,5,'EM','marginal');  % ѡ��EM�㷨,����ѡ��Ϊ5

%% �������Ա任�ֲ�
distribution_AXplusb = GMM_calculation(distribution,'linear',A,b);

%% �������Ա任�ֲ�
distribution_AXplusb_test = GMM_Distribution(A*Y+b,5,'EM','marginal');  % ѡ��EM�㷨,����ѡ��Ϊ5


%% ����
x = [-10:0.1:30]';
GMM_plot(distribution,'singlePDF',x); 
hold on
GMM_plot(distribution_AXplusb,'singlePDF',x); 
hold on
GMM_plot(distribution_AXplusb_test,'singlePDF',x); 


