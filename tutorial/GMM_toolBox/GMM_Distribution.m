%%
% ����GMMģ��
%
% ���ܣ��������������ʷֲ���������
%    a) ����������������ı߼ʷֲ�-EM/MAP
%    b) ���������ά������������Ϸֲ�-EM/MAP
%    c) ���������ά��������������ֲ�-EM/MAP
% 
% ���룺��������������
%    a) Y: (��������) ѵ������n-by-d matrix, nΪѵ��������������dΪѵ����ά��/��������
%    b) J: (��������) ��˹����, int
%    c) method: (��������) ����ѡ��char��'EM'��ʾ����EM�㷨,'MAP'��ʾ����MAP�㷨
%    d) options: (��������) ���ѡ��,char,'marginal'��ʾ����߼ʷֲ���'joint'��ʾ������Ϸֲ���'conditional'��ʾ��������ֲ�
%    e) y: (ѡ������) �����ֲ��ĸ���ֵ, 1-by-d vector, ÿһԪ��Ϊ��Ӧ�����ĸ���ֵ��Ŀ��������ĸ���ֵ��Ϊ0
%    f) Y_hyper: (ѡ������) MAP�㷨�����ڼ��㳬������ѵ������N-by-d matrix��NΪѵ��������������dΪѵ����ά��/��������
%    g) period: (ѡ������) MAP�㷨�����ڼ��㳬�����Ķ������֣�int������Y_hyper��periodΪ���ȣ��ֳ�����Сѵ�������Ӷ��γɶ���GMM�������������㳬����
%
% ������ֲ����
%    a) distribution.w: ���Ϸֲ���߼ʷֲ�Ȩ��ϵ����1-by-J vector
%    b) distribution.mu: ���Ϸֲ���߼ʷֲ���ֵ��J-by-d matrix
%    c) distribution.sigma: ���Ϸֲ���߼ʷֲ�Э���d-by-d-by-J martix
%    d) distribution.cw: �����ֲ�Ȩ��ϵ����1-by-J vector
%    e) distribution.cmu: �����ֲ�Ȩ��ϵ����J-by-1 vector
%    f) distribution.csigma: �����ֲ�Ȩ��ϵ����1-by-1-by-J martix
%    g��correlation: �����ά������ѵ����ʱ����ͬʱ�����ά����֮�������Ծ���d-by-d matrix, ���е�m�������͵�n������֮��������Ϊcorrelation(m,n),ҲΪcorrelation(n,m)
%       e.g.: [distribution,correlation] = GMM_Distribution(Y,10,'EM','joint')
%
% ��ʽ��ȫ���� [distribution,correlation] = GMM_Distribution(Y,J,method,options,y,Y_hyper,period)
% ����ѡ�������y,Y_hyper,period���밴�վ���˳�����룬��ȱʡ��������˳�򲻱�



%% ����
function [distribution,varargout] = GMM_Distribution(Y,J,method,options,varargin)

warning off

% �ж�Y�Ƿ�Ϊ������
if size(Y,1) == 1
    disp(' ')
    disp('����: �������ѵ�����ݱ�������������������������룡');
    disp(' ')
    distribution = [];
    return
end

if strcmpi(method,'EM')  % ����EM�㷨
    
    % ����ѡ����м���
    switch options

        case 'marginal'
            % �ж������Y�Ƿ�Ϊ��ά����
            if size(Y,2) == 1
                [distribution.w,distribution.mu,distribution.sigma] = func_runEM(Y,J);

            % �ж������Y�Ƿ�Ϊ��ά����
            elseif size(Y,2) >= 2
                for n = 1:size(Y,2)
                    eval(['[distribution.w',num2str(n),',distribution.mu',num2str(n),',distribution.sigma',num2str(n),'] = func_runEM(Y(:,n),J);']);
                end

            end


        case 'joint'
            % �ж������Y�Ƿ�Ϊ��ά����
            if size(Y,2) <= 1
                disp(' ')
                disp('����: �������ѵ������ά�Ȳ���2ά�����������룡');
                disp(' ')
                distribution = [];
                return
            % ���ǣ�����м���
            else
                varargout{1} = corr(Y);  % ��������ϵ������
                [distribution.w,distribution.mu,distribution.sigma] = func_runEM(Y,J);
            end

        case 'conditional'
            % �ж��Ƿ������˸���ֵy
            y = varargin{1};
            if isempty(y)
                disp(' ')
                disp('����: ��û�����������ֲ��ĸ���ֵ�����������룡');
                disp(' ')
                distribution = [];
                return

            % �жϸ���ֵ�Ƿ���Ҫ������    
            elseif size(y,2) ~= size(Y,2) || size(y,1) ~= 1
                disp(' ')
                disp('����: ������������ֲ��ĸ���ֵ������Ҫ�����������룡');
                disp(' ')
                distribution = [];
                return

            % �������ֵ����Ҫ���������ƽ��Y��y���γɵ�һ��ΪĿ��ֲ��ĸ��    
            else
                varargout{1} = corr(Y);  % ��������ϵ������
                Y_original = Y;  % ����ԭʼ���룬�����γɰ���������ϰ�ߵ����Ϸֲ�
                [~,index_0] = find(y==0);  % Ѱ��y��Ϊ0���кţ�Ҳ����Ŀ��ֲ�
                Y(:, [1, index_0]) = Y(:, [index_0, 1]);  % ����Ŀ���к͵�һ��
                y(:, [1, index_0]) = y(:, [index_0, 1]);  % ����Ŀ���к͵�һ��
                y_given = y(2:end);  % ��������ĸ���ֵ������0��ά��Ϊ��ά��-1
            end

            % ����ƽ�ƺ��Y�γ����Ϸֲ�
            [distribution.w,distribution.mu,distribution.sigma] = func_runEM(Y,J);

            % ����ƽ�ƺ��y_given�γ������ֲ�
            [distribution.cw,distribution.cmu,distribution.csigma] = func_generateConditional(distribution,y_given);

            % ����ԭʼ�����Y_original�γ����Ϸֲ����������������Y����ƥ��
            [distribution.w,distribution.mu,distribution.sigma] = func_runEM(Y_original,J);
    end
    
elseif strcmpi(method,'MAP')  % ����MAP�㷨
    
    % ����ѡ����м���
    switch options

        case 'marginal'
            % �ж������Y�Ƿ�Ϊ��ά����
            Y_hyper = varargin{1};
            period = varargin{2};
            if size(Y,2) == 1
                if size(Y_hyper,1)/period == fix(size(Y_hyper,1)/period) 
                    distribution = func_runMAP(Y,J,Y_hyper,period);
                else
                    disp(' ')
                    disp('����: ������������γɳ���������ʷ���ݺ�ʱ��û���γ�������ϵ�����������룡');
                    disp(' ')
                    distribution = [];
                    return
                end

            % �ж������Y�Ƿ�Ϊ��ά����
            elseif size(Y,2) >= 2
                disp(' ')
                disp('����: �������ѵ������ά�ȴ���1ά�����������룡');
                disp(' ')
                distribution = [];
                return
            end


        case 'joint'
            % �ж������Y�Ƿ�Ϊ��ά����
            if size(Y,2) <= 1
                disp(' ')
                disp('����: �������ѵ������ά�Ȳ���2ά�����������룡');
                disp(' ')
                distribution = [];
                return
            % ���ǣ�����м���
            else
                varargout{1} = corr(Y);  % ��������ϵ������
                Y_hyper = varargin{1};
                period = varargin{2};
                if size(Y_hyper,1)/period == fix(size(Y_hyper,1)/period) 
                    distribution = func_runMAP(Y,J,Y_hyper,period);
                else
                    disp(' ')
                    disp('����: ������������γɳ���������ʷ���ݺ�ʱ��û���γ�������ϵ�����������룡');
                    disp(' ')
                    distribution = [];
                    return
                end
            end

        case 'conditional'
            % �ж��Ƿ������˸���ֵy
            y = varargin{1};
            if isempty(y)
                disp(' ')
                disp('����: ��û�����������ֲ��ĸ���ֵ�����������룡');
                disp(' ')
                distribution = [];
                return

            % �жϸ���ֵ�Ƿ���Ҫ������    
            elseif size(y,2) ~= size(Y,2) || size(y,1) ~= 1
                disp(' ')
                disp('����: ������������ֲ��ĸ���ֵ������Ҫ�����������룡');
                disp(' ')
                distribution = [];
                return

            % �������ֵ����Ҫ���������ƽ��Y��y���γɵ�һ��ΪĿ��ֲ��ĸ��    
            else
                varargout{1} = corr(Y);  % ��������ϵ������
                [~,index_0] = find(y==0);  % Ѱ��y��Ϊ0���кţ�Ҳ����Ŀ��ֲ�
                Y(:, [1, index_0]) = Y(:, [index_0, 1]);  % ����Ŀ���к͵�һ��
                y(:, [1, index_0]) = y(:, [index_0, 1]);  % ����Ŀ���к͵�һ��
                y_given = y(2:end);  % ��������ĸ���ֵ������0��ά��Ϊ��ά��-1
            
                % ����ƽ�ƺ��Y�γ����Ϸֲ�
                Y_hyper = varargin{2};
                period = varargin{3};
                if size(Y_hyper,1)/period == fix(size(Y_hyper,1)/period) 
                    distribution = func_runMAP(Y,J,Y_hyper,period);
                else
                    disp(' ')
                    disp('����: ������������γɳ���������ʷ���ݺ�ʱ��û���γ�������ϵ�����������룡');
                    disp(' ')
                    distribution = [];
                    return
                end

                % ����ƽ�ƺ��y_given�γ������ֲ�
                distribution.w = distribution.w';
                distribution.mu = distribution.mu';
                [distribution.cw,distribution.cmu,distribution.csigma] = func_generateConditional(distribution,y_given);
            
            end
    end
    
else
    disp(' ')
    disp('����: ������ķ��������������������룡');
    disp(' ')
    distribution = [];
    
end




 
    
    
    
    
    
    