# coding=utf-8
import json

import pika

ABMQ_HOST = '10.111.10.18'
ABMQ_PORT = 5672
ABMQ_PASS = 'guest'
ABMQ_USER = 'guest'
VIRTUAL_HOST = '/'

param = {'data': 'power', 'n_components': 3, 'method': 'EM', 'options': 'marginal'}

credentials = pika.PlainCredentials(ABMQ_USER,ABMQ_PASS)
parameters = pika.ConnectionParameters(ABMQ_HOST, ABMQ_PORT, VIRTUAL_HOST, credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='test_recv_queue')
channel.basic_publish(exchange='', routing_key='test_recv_queue', body=json.dumps(param))

# channel.basic_publish(exchange='', routing_key='test_recv_queue', body='test GMM12345678')
connection.close()