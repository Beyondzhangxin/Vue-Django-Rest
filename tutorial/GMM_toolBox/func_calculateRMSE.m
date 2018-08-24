%% ����
%
% ���ܣ���������GMM֮�����ϲ��죬����RMSE
% ���룺����GMM��ģ��,�Լ���������ķ�Χ
% ���������GMMģ��PDF���ߵ�RMSE
% ���ߣ�JMS
% ʱ�䣺2018-07-07

%% ����
function RMSE = func_calculateRMSE(GMMp,GMMq,x)

% �γ�����GMM��PDF������
GMMp_vector = pdf(GMMp,x);
GMMq_vector = pdf(GMMq,x);

% ����RMSEֵ
RMSE_vector = GMMp_vector - GMMq_vector;
RMSE_vector2 = RMSE_vector.*RMSE_vector;
RMSE = sqrt(sum(RMSE_vector2)/length(x));

    
