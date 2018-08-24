%% ����
% ���ܣ���EM�㷨����GMMģ��
% ���룺ѵ�����ݺ͸�˹�����ĸ���
% �������ֵ�������Ȩ��
% ���ߣ�JMS
% ʱ�䣺2018-07-05


%% ����
function [wGMM,miuGMM,sigmaGMM] = func_runEM(originalPWf,Mc)


%% ����ά���趨
sizePwf=size(originalPWf);  % ��糡��Ԥ�������ʵ�ʳ�����2������=2��������ÿ������8759���۲�ֵ
Nsample=sizePwf(1);         % ���ݵĸ�������observations
numRan=sizePwf(2);          % ���ݵ����࣬��variables��Ҳ��֮Ϊά��

%% �������й��ƣ�����GMModel
IDX = kmeans(originalPWf, Mc);   % ����һ��k-means���࣬����������label������EM���ᰴ��labelȥ������ͬlabel�ľ�ֵ������
fprintf('xxxxxxxxxxxxxxxxx\n');  % ��ˣ��������Ŀ=label����Ŀ=mixture components����Ŀ
options = statset( 'Display','final','MaxIter',1000,'TolFun',1e-8);  % �趨EM��ѡ�����display���������������������������о�
GMModel = gmdistribution.fit(originalPWf,...   % ����X��n*dά��nΪobservations��Ŀ��dΪvariables��Ŀ
                             Mc,...            % mixture components��Ŀ������ͨ��PAC��AIC����ǰɸѡһ��best Mc������ֱ�Ӹ�����
                             'Start',IDX,...   % ����k-means������X�����ݴ���label��ʹEM���Ʋ���ʱ��Ŀ��
                             'Regularize',0.00001,...  % Ϊ�˱������ill-condition��С������ȷ��Э�����������Ƿ�����predictor������
                             'Options',options);       % ����EM����ѡ��

% GMModel.NlogL; % Negetive log likelihood

% ͳ�ƾ�ֵ��Э�����Ȩ��
wGMM=GMModel.PComponents;                 % Ȩ��ΪPComponent��ά��ΪMc*1
miuGMM=GMModel.mu;          % ��ֵΪmu��ά��ΪMc*d��Ҳ����Mc*numRan��ÿ����һ����ֵ����
sigmaGMM=GMModel.Sigma; % Э�������ΪSigma��ÿ�������ά��Ϊd*d��Ҳ����numRan*numRan��Ȼ����Mc��
  

