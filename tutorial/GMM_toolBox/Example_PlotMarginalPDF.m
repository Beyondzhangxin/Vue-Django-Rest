%% ʾ��
%
% ���Ƶ�ά����PDF�Լ����Լ�ֱ��ͼ

%% ����ѵ����
Y = 10*rand(1000,1)+randn(1000,1);
x = [-4:0.1:12]';

%% ������ά�����ĸ��ʷֲ�
distribution = GMM_Distribution(Y,5,'EM','marginal');  % ѡ��EM�㷨,����ѡ��Ϊ5

%% �������Լ������Լ����в�ͬ���������������ѵ����������ͬ�ķֲ�
Y_test = 10*rand(500,1)+randn(500,1);

%% ����
GMM_plot(distribution,'testPDF',x,Y_test,15); 