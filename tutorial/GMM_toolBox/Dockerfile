FROM gmm/mq:v2
COPY . /usr/src/app/
WORKDIR  /usr/src/app
#RUN pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
CMD python gmm_mq.py $QUEUE $COUNTTYPE