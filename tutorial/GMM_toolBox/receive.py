# coding=utf-8
import datetime
import json
import os
import time

import pika
from clickhouse_driver import Client

ABMQ_HOST = '10.112.10.24'
ABMQ_PORT = 5672
ABMQ_PASS = 'guest'
ABMQ_USER = 'guest'
VIRTUAL_HOST = '/'
credentials = pika.PlainCredentials(ABMQ_USER, ABMQ_PASS)
parameters = pika.ConnectionParameters(ABMQ_HOST, ABMQ_PORT, VIRTUAL_HOST, credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='siemense_queue')


def insert(table, column, value):
    client = Client('localhost')
    client.execute('INSERT INTO %s %s VALUES' % (table, column), value)
    print('INSERT INTO %s %s VALUES' % (table, column), value)


def save_data_to_clickhouse():
    def callback(ch, method, properties, body):
        data = json.loads(body)
        objlist = []
        for gmmobj in data['GmmobjList']:
            temp = [gmmobj['id'],gmmobj['desc'],gmmobj['power'],gmmobj['voltage'],gmmobj['electricity'],gmmobj['gmm_obligate1'],gmmobj['gmm_obligate2'],gmmobj['gmm_obligate3'],
                    gmmobj['gmm_obligate4'],gmmobj['gmm_obligate5'],gmmobj['gmm_obligate6'],gmmobj['gmm_obligate7'],gmmobj['gmm_obligate8'],gmmobj['gmm_obligate9'],gmmobj['gmm_obligate10']]
            temp.insert(0, datetime.datetime.strptime(data['TimeStamp'], "%Y-%m-%d %H:%M:%S"))
            objlist.append(tuple(temp))
        insert_data = tuple(objlist)
        table = 'siemense.siemense_objlist'
        column1 = '(TimeStamp,id,desc,power,voltage,electricity,gmm_obligate1,gmm_obligate2,gmm_obligate3,gmm_obligate4,gmm_obligate5,gmm_obligate6,gmm_obligate7,gmm_obligate8,gmm_obligate9,gmm_obligate10)'
        insert(table, column1, insert_data)

    channel.basic_consume(queue='siemense_queue',
                          auto_ack=True,
                          on_message_callback=callback)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
