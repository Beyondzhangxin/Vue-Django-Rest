# coding=utf-8
import sys

import pika
import json


from GMM_Calculation import GMM_calculation,gmm_cal,siemense_cal

ABMQ_HOST = '10.112.10.24'
ABMQ_PORT = 5672
ABMQ_PASS = 'guest'
ABMQ_USER = 'guest'
VIRTUAL_HOST = '/'


class gmm(object):

    def __init__(self):
        self.mqHost = ABMQ_HOST
        self.mqPort = ABMQ_PORT
        self.mqUser = ABMQ_PASS
        self.mqPassWord = ABMQ_USER
        self.exchange = ''
        self.virtual_host = VIRTUAL_HOST
        credentials = pika.PlainCredentials(self.mqUser, self.mqPassWord)
        parameters = pika.ConnectionParameters(self.mqHost, self.mqPort, self.virtual_host, credentials)
        self.con = pika.BlockingConnection(parameters)
        self.close = False
        self.valuuid = ''

    def connectClose(self):
        self.close = True
        self.con.close()

    def sendMsg(self, message, queue, exchange=''):
        channel = self.con.channel()
        channel.queue_declare(queue=queue)
        channel.basic_publish(exchange=exchange, routing_key=queue, body=message)

    def receive_msg(self, queue):
        channel = self.con.channel()
        self.queue = queue

        def callback(ch, method, properties, body):
            self.message = bytes.decode(body)
            ch.close()

        channel.basic_consume(on_message_callback=callback,
                              queue=self.queue,
                              auto_ack=True)
        channel.start_consuming()
        return self.message


def main(queue, ret_queue, countType):
    rbmq = gmm()

    # 从rbmq接收数据，参数顺序 队列名称，路由名称（可以不填默认为''） 返回接收到的数据
    message = rbmq.receive_msg(queue)
    # 统计算法函数表
    # message='{"name":"0718","selectedout":"kl","dateto":"2019-07-17T16:00:00.000Z","selectedmethod":"em","linear_a":1,"datefrom":"2019-07-16T16:00:00.000Z","period":0,"n_max":1,"linear_b":1,"n_min":0,"device":[{"factories":[{"note":"","guid":"{6c7f6258-4918-4d6b-8462-344b4e9c5222}","type":"Analog","name":"\u9635\u5217\u7535\u6d41","id":"116603"}],"name":"1\u533a\u5149\u4f0f\u9006\u53d8\u56681","note":"","guid":"{646baf41-d7b7-43e1-9afc-66b5e795e70a}","type":"Bay","id":"116598"},{"factories":[{"note":"","guid":"{38e43ae6-ceca-47da-80e7-788a99b73da3}","type":"Analog","name":"\u9635\u5217\u7535\u6d41","id":"116915"}],"name":"1\u533a\u5149\u4f0f\u9006\u53d8\u56682","note":"","guid":"{9f608deb-7989-459a-8f77-a714e464bb06}","type":"Bay","id":"116761"}],"real_time":false,"id":23}'
    fucTable = {
        'GMM_calculation': GMM_calculation,
        'gmm': siemense_cal,
        'siemense_cal':siemense_cal,
    }
    # 根据计算类型查表调用算法，返回结果
    # message=''
    if countType in fucTable:
        fucTable[countType](message,rbmq,ret_queue)
    else:
        pass

    # print result
    # 将结果提供rbmq返回到平台 参数顺序 结果 队列名称，路由名称（可以不填默认为''）
    # rbmq.sendMsg(json.dumps(result), ret_queue)


if __name__ == '__main__':
    print(sys.argv)
    queue = '_recv_queue'
    ret_queue = '_count_queue'
    if len(sys.argv) > 1:
        queue = sys.argv[1] + queue
        ret_queue = sys.argv[1] + ret_queue
        countType = sys.argv[2]
    print('run ', ret_queue, countType)
    # ret_queue='test_count_queue'
    # queue='test_recv_queue'
    # countType='test_GMM'
    main(queue, ret_queue, countType)
    # main('test_recv_queue', 'test_count_queue', 'gmm')
