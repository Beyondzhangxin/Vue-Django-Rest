%%
% ����GMM�ܱ�
%
% ���ܣ��������������Ƹ��ʷֲ��ܱߵĹ���
%    a) ���Ƶ�һά�ȵĸ����ܶȺ���
%    b) ���Ʋ��Լ�ֱ��ͼ�͵�һά�ȵĸ����ܶȺ���
%    c) ���ƶ�ά�ȵĸ����ܶȺ���
%    d) ���Ƶ�һά�ȵĻ��۸��ʺ���
%    e) ���ƶ�ά�ȵĻ��۸��ʺ���
%    f) ���������ֲ�
% 
% ��������������
%    a) (��������) distribution:  GMMģ�ͣ�
%       1) distribution.w: ���Ϸֲ���߼ʷֲ�Ȩ��ϵ����1-by-J vector
%       2) distribution.mu: ���Ϸֲ���߼ʷֲ���ֵ��J-by-d matrix
%       3) distribution.sigma: ���Ϸֲ���߼ʷֲ�Э���d-by-d-by-J martix
%    b) (��������) options: ���ѡ��,char
%       1��'singlePDF': ���Ƶ�һά�ȵĸ����ܶȺ���/�����ֲ�
%       2��'multiPDF': ���ƶ�ά�ȵĸ����ܶȺ���
%       3��'testPDF':  ���Ʋ��Լ�ֱ��ͼ�͵�һά�ȵĸ����ܶȺ���
%       4��'singleCDF':  ���Ƶ�һά�ȵĻ��۸��ʺ���
%       5��'multiCDF': ���ƶ�ά�ȵĻ��۸��ʺ���
%    c) (��������) x: ���Ƶ�һpdf��һcdfʱ�����������Χ,n-by-1��vector
%       e.g.: GMM_plot(distribution,'singlePDF',x)
%       e.g.: GMM_plot(distribution,'singleCDF',x)
%    d) (ѡ������) y: ���ƶ�άpdfʱ���ڶ��������ķ�Χ��n-by-1��vector
%    e) (ѡ������) Y_test: ���ƺ����Լ�ֱ��ͼʱ�Ĳ��Լ�,n-by-1��matrix
%    f) (ѡ������) Y_tenum_intervalst: ���ƺ����Լ�ֱ��ͼʱ�Ĳ��Լ��ķ�����,int��matrix
%       e.g.: GMM_plot(distribution,'testPDF',x,Y_test,num_interval)
%
% �������������
%    a) single pdf figure: ���Ƶ�һά�ȵĸ����ܶȺ����������ֲ�
%    a) single cdf figure: ���Ƶ�һά�ȵĻ��۸��ʺ���
%    a) multi pdf figure: ���ƶ�ά�ȵĸ����ܶȺ���
%    a) multi cdf figure: ���ƶ�ά�ȵĻ��۸��ʺ���
%    a) test pdf figure: ���Ʋ��Լ�ֱ��ͼ�͵�һά�ȵĸ����ܶȺ���
%
% ע�⣺
%    ȫ������ʽ GMM_plot(distribution,options,x,y,Y_test,num_interval)
%    ����ѡ�������y,Y_test,num_interval���밴�վ���˳�����룬��ȱʡ��������˳�򲻱�
       

%% ����
function GMM_plot(distribution,options,x,varargin)

switch options
    
    case 'singlePDF'
        if size(distribution.sigma,1) ~= 1
            disp(' ')
            disp('����: ������ķֲ�Ϊ��ά�ֲ������������뵥ά�ֲ���');
            disp(' ')
            return
        else
            GMM = gmdistribution(distribution.mu,distribution.sigma,distribution.w');
            plot(x,pdf(GMM,x));
            saveas(gcf,'/gmm/result.png')

        end
        
    case 'multiPDF'
        if size(distribution.sigma,1) == 1
            disp(' ')
            disp('����: ������ķֲ�Ϊ��ά�ֲ��������������ά�ֲ���');
            disp(' ')
            return
        else
            y = varargin{1};
            GMM = gmdistribution(distribution.mu,distribution.sigma,distribution.w');
            N = length(x);
            [x,y] = meshgrid(x,y);
            X = [x(:) y(:)];
            Z = pdf(GMM,X);
            surf(x,y,reshape(Z,N,N));
            saveas(gcf,'/gmm/result.png')
        end
        
    case 'testPDF'
        if size(distribution.sigma,1) ~= 1
            disp(' ')
            disp('����: ������ķֲ�Ϊ��ά�ֲ������������뵥ά�ֲ���');
            disp(' ')
            return
        else
            Y_test = varargin{1};
            num_interval = varargin{2};
            func_plotHist(Y_test,num_interval);
            hold on
            GMM = gmdistribution(distribution.mu,distribution.sigma,distribution.w');
            plot(x,pdf(GMM,x));
            saveas(gcf,'/gmm/result.png')
        end
        
    case 'singleCDF'
        if size(distribution.sigma,1) ~= 1
            disp(' ')
            disp('����: ������ķֲ�Ϊ��ά�ֲ������������뵥ά�ֲ���');
            disp(' ')
            return
        else
            GMM = gmdistribution(distribution.mu,distribution.sigma,distribution.w');
            plot(x,cdf(GMM,x));
            saveas(gcf,'/gmm/result.png')
        end
        
    case 'multiCDF'
        if size(distribution.sigma,1) == 1
            disp(' ')
            disp('����: ������ķֲ�Ϊ��ά�ֲ��������������ά�ֲ���');
            disp(' ')
            return
        else
            y = varargin{1};
            GMM = gmdistribution(distribution.mu,distribution.sigma,distribution.w');
            N = length(x);
            [x,y] = meshgrid(x,y);
            X = [x(:) y(:)];
            Z = cdf(GMM,X);
            surf(x,y,reshape(Z,N,N));
            saveas(gcf,'/gmm/result.png')
        end
        
end
        
    