%%
% ����GMM�ܱ�
%
% ���ܣ�����������������ʷֲ��ܱߵĹ���
%    a) �����ڸ�����ĸ����ܶȺ���ֵ
%    b) �����ڸ�����Ļ��۸��ʺ���ֵ
%    c) �������������ֲ�֮���KLɢ��
%    d) �������������߼ʷֲ�֮���RMSE
%    e) ����������������Ժ����ķֲ�
% 
% ��������������
%    a) (��������) distribution:  GMMģ�ͣ�
%       1) distribution.w: ���Ϸֲ���߼ʷֲ�Ȩ��ϵ����1-by-J vector
%       2) distribution.mu: ���Ϸֲ���߼ʷֲ���ֵ��J-by-d matrix
%       3) distribution.sigma: ���Ϸֲ���߼ʷֲ�Э���d-by-d-by-J martix
%    b) (��������) options: ���ѡ��,char
%       1��'pdf': �����ڸ�����ĸ����ܶȺ���ֵ
%       2��'cdf': �����ڸ�����Ļ��۸��ʺ���ֵ
%       3) 'quantile': ��������ֲ���10%-100%��λ��
%       4��'KL':  �������������ֲ�֮���KLɢ��
%       5��'RMSE':  �������������ֲ�֮���RMSEɢ��
%       6��'linear':  ����������������Ժ����ķֲ�
%    c) (ѡ������) y: ����pdf��cdfʱ�ĸ�����,1-by-d vector
%       e.g.: pdf = GMM_calculation(distribution,'pdf',y)
%       e.g.: cdf = GMM_calculation(distribution,'cdf',y)
%    d) (ѡ������) distribution_other: ����KL��RMSEʱ��������һ��GMMģ��
%       1) distribution_other.w: ���Ϸֲ���߼ʷֲ�Ȩ��ϵ����1-by-J vector
%       2) distribution_other.mu: ���Ϸֲ���߼ʷֲ���ֵ��J-by-d matrix
%       3) distribution_other.sigma: ���Ϸֲ���߼ʷֲ�Э���d-by-d-by-J martix
%       e.g.: KL = GMM_calculation(distribution,'KL',distribution_other)
%    e) (ѡ������) x: ����RMSEʱ�����ķ�Χ,N-by-d matrix
%       e.g.: RMSE = GMM_calculation(distribution,'RMSE',distribution_other,x)
%    f) (ѡ������) A: ��������������Ժ����ķֲ�ʱ���������ϵ������, d-by-d matrix
%    g) (ѡ������) b: ��������������Ժ����ķֲ�ʱ��������ĳ�������, d-by-1 matrix
%       e.g.: distribution_AXplusb = GMM_calculation(distribution,'linear',A,b)
%    h) (ѡ������) n_min,n_max: ��������ֲ���10%-100%��λ��ʱ��������ķ�Χ��float
%
% �������������
%    a) pdf: �ڸ�����ĸ����ܶȺ���ֵ��float
%    b) cdf: �ڸ�����Ļ��۸��ʺ���ֵ��float
%    c) quantile:��������ֲ���1%-100%��λ����float
%    d) KL: ���������ֲ�֮���KLɢ��, float
%    e) RMSE: ���������ֲ�֮���RMSE, float
%    f) distribution_AXplusb: ����������Ժ����ķֲ���GMMģ�ͣ�AXplusb -> Ax+b
%       1) distribution_AXplusb.w: ���Ϸֲ���߼ʷֲ�Ȩ��ϵ����1-by-J vector
%       2) distribution_AXplusb.mu: ���Ϸֲ���߼ʷֲ���ֵ��J-by-d matrix
%       3) distribution_AXplusb.sigma: ���Ϸֲ���߼ʷֲ�Э���d-by-d-by-J martix
%
% ע�⣺
%    ȫ������ʽ [pdf,cdf,KL,RMSE,distribution] = GMM_calculation(distribution,options,y,distribution_other,x,A,b,n_min,n_max)
%    ����ѡ�������y,distribution_other,x,A,b,n_min,n_max���밴�վ���˳�����룬��ȱʡ��������˳�򲻱�

%% ����
function varargout = GMM_calculation(distribution,options,varargin)

switch options
    
    case 'pdf'
        y = varargin{1};
        GMM = gmdistribution(distribution.mu,distribution.sigma,distribution.w');
        varargout{1} = pdf(GMM,y);
        
    case 'cdf'
        y = varargin{1};
        GMM = gmdistribution(distribution.mu,distribution.sigma,distribution.w');
        varargout{1} = cdf(GMM,y);
        
    case 'KL'
        distribution_other = varargin{1};
        GMM1 = gmdistribution(distribution.mu,distribution.sigma,distribution.w');
        GMM2 = gmdistribution(distribution_other.mu,distribution_other.sigma,distribution_other.w');
        varargout{1} = func_calculateKL(GMM1,GMM2);
        
    case 'RMSE'
        distribution_other = varargin{1};
        x = varargin{2};
        GMM1 = gmdistribution(distribution.mu,distribution.sigma,distribution.w');
        GMM2 = gmdistribution(distribution_other.mu,distribution_other.sigma,distribution_other.w');
        varargout{1} = func_calculateRMSE(GMM1,GMM2,x);
        
    case 'linear'
        A = varargin{1};
        b = varargin{2};
        J = size(distribution.mu,1);
        d = size(distribution.mu,2);
        varargout{1}.w =zeros(1,J);
        varargout{1}.mu = zeros(J,d);
        varargout{1}.sigma = zeros(d,d,J);
        for j = 1:J
            varargout{1}.w(j) = distribution.w(j);
            varargout{1}.mu(j,:) = (A*distribution.mu(j,:)'+b)';
            varargout{1}.sigma(:,:,j) = A*distribution.sigma(:,:,j)*A';
        end
        
    case 'quantile'
        [varargout{1},~] = func_quantile(distribution,varargin{1},varargin{2});
        
        
end
        
        
        
        
