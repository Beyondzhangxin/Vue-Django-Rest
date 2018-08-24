%% ����
%
% ���ܣ���������GMM֮�����ϲ���
% ���룺����GMM��ģ��
% ���������EMD��KLD����ϲ���ֵ��ԽֵԽ��˵������GMM֮��ľ���ԽԶ����������ԽС; ��֮��ֵԽС��������Խ��
% ���ߣ�JMS
% ʱ�䣺2018-07-07

%% ����
function KLDEMD = func_calculateKL(GMMp,GMMq)

% ������ȡ
Num_J = size(GMMp.ComponentProportion,2);  % component����
d = size(GMMp.Sigma,1);

% ���Թ滮��������
D = zeros(Num_J,Num_J);    % ���������ʵû��Ҫ�洢
f = zeros(Num_J*Num_J,1);  % Ŀ�꺯��ϵ��������
A_up = zeros(Num_J,Num_J*Num_J);  % ����ʽԼ��ϵ������,�ϰ벿��
A_down = zeros(Num_J,Num_J*Num_J);  % ����ʽԼ��ϵ������,�°벿�֣����ߴ���Ϊ���յ�A
b = zeros(2*Num_J,1);    % ����ʽԼ��������
lb = zeros(Num_J*Num_J,1);  % �½�Լ��
Aeq = ones(1,Num_J*Num_J);  % ��ʽԼ��ϵ������
beq = 1;                    % ��ʽԼ��������

% �γ�Ŀ�꺯��ϵ��������f
m = 1; % ������
for i = 1:Num_J
    for j = 1:Num_J
        KLDij = 0.5* (...
                log(det(GMMq.Sigma(:,:,j))/det(GMMp.Sigma(:,:,i))) + ...
                trace(inv(GMMq.Sigma(:,:,j))*GMMp.Sigma(:,:,i)) + ...
                (GMMp.mu(i,:) - GMMq.mu(j,:))*inv(GMMq.Sigma(:,:,j))*(GMMp.mu(i,:) - GMMq.mu(j,:))' - d ...
                );
        KLDji = 0.5* (...
                log(det(GMMp.Sigma(:,:,i))/det(GMMq.Sigma(:,:,j))) + ...
                trace(inv(GMMp.Sigma(:,:,i))*GMMq.Sigma(:,:,j)) + ...
                (GMMq.mu(j,:) - GMMp.mu(i,:))*inv(GMMp.Sigma(:,:,i))*(GMMq.mu(j,:) - GMMp.mu(i,:))' - d ...
                );
        D(i,j) = 0.5*(KLDij+KLDji);
        % ��Dֱ���γ����Թ滮�е�Ŀ�꺯��ϵ��������
        f(m) = D(i,j);
        m = m + 1;
    end
end

% �γɲ���ʽԼ��ϵ������A
for n = 1:Num_J
    A_up(n,(n-1)*Num_J+1:n*Num_J) = 1;
    A_down(n,n:Num_J:(Num_J-1)*Num_J+n) = 1;
end
A = [A_up;A_down];

% �γɲ���ʽԼ��������
b_up = GMMp.ComponentProportion';
b_down = GMMq.ComponentProportion';
b = [b_up;b_down];

% ������Թ滮
[~,KLDEMD] = linprog(f,A,b,Aeq,beq,lb,[],[]);
    
