%% ʾ��
%
% ���Ƶ�ά����PDF�Լ����Լ�ֱ��ͼ

%% ����ѵ����
Y1 = 10*rand(1000,1)+randn(1000,1);
Y2 = 15*rand(1000,1)+3*randn(1000,1);
Y = [Y1,Y2];
x = [-4:0.1:12]';
y = [-10:0.2:22]';

%% ������ά�����ĸ��ʷֲ�
distribution = GMM_Distribution(Y,5,'EM','joint');  % ѡ��EM�㷨,����ѡ��Ϊ5

%% ����
GMM_plot(distribution,'testPDF',x,y); 