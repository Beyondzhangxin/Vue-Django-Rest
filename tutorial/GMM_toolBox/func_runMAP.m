%% ����
%
% ���ܣ������������ʷֲ�

%% ����
function distribution = func_runMAP(Y,J,Y_hyper,period)

warning off

% ������ؼ������
d = size(Y_hyper,2);         % ��������
N = size(Y_hyper,1)/period;  % ������Ҳ��GMM����������
sigma_hyper = zeros(J*d,d,N);
w_hyper = zeros(J,1,N);
mu_hyper = zeros(J,d,N);

% �����ʱ�μ������GMM����
for n = 1:N

    % ����һ��
    [w,mu,sigma] = func_runEM(Y_hyper((n-1)*period+1:n*period,:),J);

    % ��¼����
    for j=1:J
        sigma_hyper((j-1)*size(sigma,1)+1:j*size(sigma,1),:,n)=sigma(:,:,j);   % ÿd�У�Ҳ����ÿnumRan�У���¼һ��Э�������
    end
    w_hyper(:,:,n) = w';
    mu_hyper(:,:,n) = mu;

end

% �γɳ�����
[v,mu,tau,alpha,u] = func_hyperparameter(w_hyper,mu_hyper,sigma_hyper);

% �γɷֲ�
Num = 1000;           % max iterative number
e = 10^(-3);          % convergent accuracy

% ��ʼ��
weight0 = (v-1)/(sum(v) - J);  % Ȩ��ϵ����ֵ  (v-1)/(sum(v) - J)
mean0 = mu;                    % ��ֵ��ֵ
cov0 = zeros(d,d,J);           % Э�����ֵ
for j = 1:J
    cov0(:,:,j) = u(:,:,j)/(alpha(j) - d);      % Э����
end

% ����
for n = 1 : Num
    [weight,mean,cov] = func_map(Y',J,v,mu,tau,alpha,u,weight0,mean0,cov0);        
    % �ж��Ƿ�����
    if norm(weight - weight0) <= e && norm(mean - mean0) <= e && max(max(max(cov - cov0))) <= e
        weight0 = weight;
        mean0 = mean;
        cov0 = cov;
        disp('������');
        break;
    else
        weight0 = weight;
        mean0 = mean;
        cov0 = cov;
    end
end

distribution.w = weight;
distribution.mu = mean';
distribution.sigma = cov;