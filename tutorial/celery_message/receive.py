# coding=utf-8
import json
import os
import time

import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='test_recv_queue')
def callback(ch, method, properties, body):

    data = json.loads(body)
    print(data['selectedmethod'] == 'em')
    print(data['x'])
    print(data['y'])
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(
    queue='test_recv_queue', on_message_callback=callback)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()