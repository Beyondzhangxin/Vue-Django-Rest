%% ����
%
% ���ܣ�����ֱ��ͼ
% ���룺�������ݵ�������
%      ���ƶ��ٸ�����
% 
% ���ߣ�JMS
% ʱ�䣺2018-06-09

%% ����
function func_plotHist(data_vector,num_interval)
c = data_vector;
[a,b]=hist(c,num_interval);              % ��Ϊ���ɸ�����ͳ��Ƶ����yΪÿ�������е�Ԥ�������Ƶ����xΪ�����������ֵ
a=a/length(c)/(b(2)-b(1));   % ��������ܶȣ�Ƶ�����������������������
bar(b,a,1,'Facecolor',[1,1,1]);  