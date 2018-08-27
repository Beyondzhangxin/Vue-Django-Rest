%%
% 建立GMM模型
%
% 功能：本函数包含概率分布构建功能
%    a) 构建任意随机变量的边际分布-EM/MAP
%    b) 构建任意多维随机变量的联合分布-EM/MAP
%    c) 构建任意多维随机变量的条件分布-EM/MAP
% 
% 输入：本函数输入如下
%    a) Y: (必须输入) 训练集，n-by-d matrix, n为训练集样本数量，d为训练集维度/变量个数
%    b) J: (必须输入) 高斯个数, int
%    c) method: (必须输入) 方法选择，char，'EM'表示采用EM算法,'MAP'表示采用MAP算法
%    d) options: (必须输入) 输出选择,char,'marginal'表示输出边际分布，'joint'表示输出联合分布，'conditional'表示输出条件分布
%    e) y: (选择输入) 条件分布的给定值, 1-by-d vector, 每一元素为对应变量的给定值，目标变量处的给定值设为0
%    f) Y_hyper: (选择输入) MAP算法下用于计算超参数的训练集，N-by-d matrix，N为训练集样本数量，d为训练集维度/变量个数
%    g) period: (选择输入) MAP算法下用于计算超参数的段数划分，int，即将Y_hyper以period为长度，分成若干小训练集，从而形成多组GMM参数，进而计算超参数
%
% 输出：分布结果
%    a) distribution.w: 联合分布或边际分布权重系数，1-by-J vector
%    b) distribution.mu: 联合分布或边际分布均值，J-by-d matrix
%    c) distribution.sigma: 联合分布或边际分布协方差，d-by-d-by-J martix
%    d) distribution.cw: 条件分布权重系数，1-by-J vector
%    e) distribution.cmu: 条件分布权重系数，J-by-1 vector
%    f) distribution.csigma: 条件分布权重系数，1-by-1-by-J martix
%    g）correlation: 输入多维变量的训练集时，将同时计算多维变量之间的相关性矩阵，d-by-d matrix, 其中第m个变量和第n个变量之间的相关性为correlation(m,n),也为correlation(n,m)
%       e.g.: [distribution,correlation] = GMM_Distribution(Y,10,'EM','joint')
%
% 形式：全参数 [distribution,correlation] = GMM_Distribution(Y,J,method,options,y,Y_hyper,period)
% 其中选择输入的y,Y_hyper,period必须按照绝对顺序输入，可缺省，但绝对顺序不变



%% 函数
function [distribution,varargout] = GMM_Distribution(Y,J,method,options,varargin)

warning off

% 判断Y是否为列向量
if size(Y,1) == 1
    disp(' ')
    disp('错误: 您输入的训练数据必须是列向量或矩阵，请重新输入！');
    disp(' ')
    distribution = [];
    return
end

if strcmpi(method,'EM')  % 采用EM算法
    
    % 根据选项进行计算
    switch options

        case 'marginal'
            % 判断输入的Y是否为单维数据
            if size(Y,2) == 1
                [distribution.w,distribution.mu,distribution.sigma] = func_runEM(Y,J);

            % 判断输入的Y是否为多维数据
            elseif size(Y,2) >= 2
                for n = 1:size(Y,2)
                    eval(['[distribution.w',num2str(n),',distribution.mu',num2str(n),',distribution.sigma',num2str(n),'] = func_runEM(Y(:,n),J);']);
                end

            end


        case 'joint'
            % 判断输入的Y是否为多维数据
            if size(Y,2) <= 1
                disp(' ')
                disp('错误: 您输入的训练数据维度不足2维，请重新输入！');
                disp(' ')
                distribution = [];
                return
            % 若是，则进行计算
            else
                varargout{1} = corr(Y);  % 输出相关性系数矩阵
                [distribution.w,distribution.mu,distribution.sigma] = func_runEM(Y,J);
            end

        case 'conditional'
            % 判断是否输入了给定值y
            y = varargin{1};
            if isempty(y)
                disp(' ')
                disp('错误: 您没有输入条件分布的给定值，请重新输入！');
                disp(' ')
                distribution = [];
                return

            % 判断给定值是否按照要求输入    
            elseif size(y,2) ~= size(Y,2) || size(y,1) ~= 1
                disp(' ')
                disp('错误: 您输入的条件分布的给定值不符合要求，请重新输入！');
                disp(' ')
                distribution = [];
                return

            % 如果给定值按照要求输入后，则平移Y和y，形成第一列为目标分布的格局    
            else
                varargout{1} = corr(Y);  % 输出相关性系数矩阵
                Y_original = Y;  % 保存原始输入，用于形成按照输入人习惯的联合分布
                [~,index_0] = find(y==0);  % 寻找y中为0的列号，也就是目标分布
                Y(:, [1, index_0]) = Y(:, [index_0, 1]);  % 交换目标列和第一列
                y(:, [1, index_0]) = y(:, [index_0, 1]);  % 交换目标列和第一列
                y_given = y(2:end);  % 获得完整的给定值，不含0，维度为总维度-1
            end

            % 按照平移后的Y形成联合分布
            [distribution.w,distribution.mu,distribution.sigma] = func_runEM(Y,J);

            % 按照平移后的y_given形成条件分布
            [distribution.cw,distribution.cmu,distribution.csigma] = func_generateConditional(distribution,y_given);

            % 按照原始输入的Y_original形成联合分布，输出结果和输入的Y完美匹配
            [distribution.w,distribution.mu,distribution.sigma] = func_runEM(Y_original,J);
    end
    
elseif strcmpi(method,'MAP')  % 采用MAP算法
    
    % 根据选项进行计算
    switch options

        case 'marginal'
            % 判断输入的Y是否为单维数据
            Y_hyper = varargin{1};
            period = varargin{2};
            if size(Y,2) == 1
                if size(Y_hyper,1)/period == fix(size(Y_hyper,1)/period) 
                    distribution = func_runMAP(Y,J,Y_hyper,period);
                else
                    disp(' ')
                    disp('错误: 您输入的用于形成超参数的历史数据和时段没有形成整除关系，请重新输入！');
                    disp(' ')
                    distribution = [];
                    return
                end

            % 判断输入的Y是否为多维数据
            elseif size(Y,2) >= 2
                disp(' ')
                disp('错误: 您输入的训练数据维度大于1维，请重新输入！');
                disp(' ')
                distribution = [];
                return
            end


        case 'joint'
            % 判断输入的Y是否为多维数据
            if size(Y,2) <= 1
                disp(' ')
                disp('错误: 您输入的训练数据维度不足2维，请重新输入！');
                disp(' ')
                distribution = [];
                return
            % 若是，则进行计算
            else
                varargout{1} = corr(Y);  % 输出相关性系数矩阵
                Y_hyper = varargin{1};
                period = varargin{2};
                if size(Y_hyper,1)/period == fix(size(Y_hyper,1)/period) 
                    distribution = func_runMAP(Y,J,Y_hyper,period);
                else
                    disp(' ')
                    disp('错误: 您输入的用于形成超参数的历史数据和时段没有形成整除关系，请重新输入！');
                    disp(' ')
                    distribution = [];
                    return
                end
            end

        case 'conditional'
            % 判断是否输入了给定值y
            y = varargin{1};
            if isempty(y)
                disp(' ')
                disp('错误: 您没有输入条件分布的给定值，请重新输入！');
                disp(' ')
                distribution = [];
                return

            % 判断给定值是否按照要求输入    
            elseif size(y,2) ~= size(Y,2) || size(y,1) ~= 1
                disp(' ')
                disp('错误: 您输入的条件分布的给定值不符合要求，请重新输入！');
                disp(' ')
                distribution = [];
                return

            % 如果给定值按照要求输入后，则平移Y和y，形成第一列为目标分布的格局    
            else
                varargout{1} = corr(Y);  % 输出相关性系数矩阵
                [~,index_0] = find(y==0);  % 寻找y中为0的列号，也就是目标分布
                Y(:, [1, index_0]) = Y(:, [index_0, 1]);  % 交换目标列和第一列
                y(:, [1, index_0]) = y(:, [index_0, 1]);  % 交换目标列和第一列
                y_given = y(2:end);  % 获得完整的给定值，不含0，维度为总维度-1
            
                % 按照平移后的Y形成联合分布
                Y_hyper = varargin{2};
                period = varargin{3};
                if size(Y_hyper,1)/period == fix(size(Y_hyper,1)/period) 
                    distribution = func_runMAP(Y,J,Y_hyper,period);
                else
                    disp(' ')
                    disp('错误: 您输入的用于形成超参数的历史数据和时段没有形成整除关系，请重新输入！');
                    disp(' ')
                    distribution = [];
                    return
                end

                % 按照平移后的y_given形成条件分布
                distribution.w = distribution.w';
                distribution.mu = distribution.mu';
                [distribution.cw,distribution.cmu,distribution.csigma] = func_generateConditional(distribution,y_given);
            
            end
    end
    
else
    disp(' ')
    disp('错误: 您输入的方法名称有误，请重新输入！');
    disp(' ')
    distribution = [];
    
end




 
    
    
    
    
    
    