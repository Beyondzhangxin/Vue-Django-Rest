%%
% 绘制GMM周边
%
% 功能：本函数包含绘制概率分布周边的功能
%    a) 绘制单一维度的概率密度函数
%    b) 绘制测试集直方图和单一维度的概率密度函数
%    c) 绘制多维度的概率密度函数
%    d) 绘制单一维度的积累概率函数
%    e) 绘制多维度的积累概率函数
%    f) 绘制条件分布
% 
% 本函数输入如下
%    a) (必须输入) distribution:  GMM模型，
%       1) distribution.w: 联合分布或边际分布权重系数，1-by-J vector
%       2) distribution.mu: 联合分布或边际分布均值，J-by-d matrix
%       3) distribution.sigma: 联合分布或边际分布协方差，d-by-d-by-J martix
%    b) (必须输入) options: 输出选择,char
%       1）'singlePDF': 绘制单一维度的概率密度函数/条件分布
%       2）'multiPDF': 绘制多维度的概率密度函数
%       3）'testPDF':  绘制测试集直方图和单一维度的概率密度函数
%       4）'singleCDF':  绘制单一维度的积累概率函数
%       5）'multiCDF': 绘制多维度的积累概率函数
%    c) (必须输入) x: 绘制单一pdf或单一cdf时的随机变量范围,n-by-1，vector
%       e.g.: GMM_plot(distribution,'singlePDF',x)
%       e.g.: GMM_plot(distribution,'singleCDF',x)
%    d) (选择输入) y: 绘制二维pdf时，第二个变量的范围，n-by-1，vector
%    e) (选择输入) Y_test: 绘制含测试集直方图时的测试集,n-by-1，matrix
%    f) (选择输入) Y_tenum_intervalst: 绘制含测试集直方图时的测试集的分区数,int，matrix
%       e.g.: GMM_plot(distribution,'testPDF',x,Y_test,num_interval)
%
% 本函数输出如下
%    a) single pdf figure: 绘制单一维度的概率密度函数、条件分布
%    a) single cdf figure: 绘制单一维度的积累概率函数
%    a) multi pdf figure: 绘制多维度的概率密度函数
%    a) multi cdf figure: 绘制多维度的积累概率函数
%    a) test pdf figure: 绘制测试集直方图和单一维度的概率密度函数
%
% 注意：
%    全参数形式 GMM_plot(distribution,options,x,y,Y_test,num_interval)
%    其中选择输入的y,Y_test,num_interval必须按照绝对顺序输入，可缺省，但绝对顺序不变
       

%% 函数
function GMM_plot(distribution,options,x,varargin)

switch options
    
    case 'singlePDF'
        if size(distribution.sigma,1) ~= 1
            disp(' ')
            disp('错误: 您输入的分布为多维分布，请重新输入单维分布！');
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
            disp('错误: 您输入的分布为单维分布，请重新输入多维分布！');
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
            disp('错误: 您输入的分布为多维分布，请重新输入单维分布！');
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
            disp('错误: 您输入的分布为多维分布，请重新输入单维分布！');
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
            disp('错误: 您输入的分布为单维分布，请重新输入多维分布！');
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
        
    