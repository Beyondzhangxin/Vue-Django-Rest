%% 介绍
% 功能：用EM算法计算GMM模型
% 输入：训练数据和高斯分量的个数
% 输出：均值、方差和权重
% 作者：JMS
% 时间：2018-07-05


%% 函数
function [wGMM,miuGMM,sigmaGMM] = func_runEM(originalPWf,Mc)


%% 参数维度设定
sizePwf=size(originalPWf);  % 风电场的预测出力和实际出力，2类数据=2个变量，每类数据8759个观测值
Nsample=sizePwf(1);         % 数据的个数，即observations
numRan=sizePwf(2);          % 数据的种类，即variables，也称之为维度

%% 参数进行估计，生成GMModel
IDX = kmeans(originalPWf, Mc);   % 先做一次k-means聚类，给变量打上label，最终EM将会按照label去计算相同label的均值、方差
fprintf('xxxxxxxxxxxxxxxxx\n');  % 因此，聚类的数目=label的数目=mixture components的数目
options = statset( 'Display','final','MaxIter',1000,'TolFun',1e-8);  % 设定EM的选项，例如display迭代次数，最大迭代次数，收敛判据
GMModel = gmdistribution.fit(originalPWf,...   % 变量X，n*d维，n为observations数目，d为variables数目
                             Mc,...            % mixture components数目，可以通过PAC或AIC来提前筛选一个best Mc，这里直接给定了
                             'Start',IDX,...   % 基于k-means给变量X的数据打上label，使EM估计参数时有目标
                             'Regularize',0.00001,...  % 为了避免出现ill-condition，小正数来确保协方差正定，是否新增predictor都可以
                             'Options',options);       % 给出EM其他选项

% GMModel.NlogL; % Negetive log likelihood

% 统计均值、协方差和权重
wGMM=GMModel.PComponents;                 % 权重为PComponent，维度为Mc*1
miuGMM=GMModel.mu;          % 均值为mu，维度为Mc*d，也就是Mc*numRan；每行是一个均值向量
sigmaGMM=GMModel.Sigma; % 协方差矩阵为Sigma，每个矩阵的维度为d*d，也就是numRan*numRan，然后有Mc个
  

