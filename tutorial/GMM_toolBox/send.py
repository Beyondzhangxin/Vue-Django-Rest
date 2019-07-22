# coding=utf-8
import datetime
import json
import math
import os
import pickle

import random
import sys
import time

import pika

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

print(sys.path)


def send_data_to_clickhouse(period):
    endtime = datetime.datetime.now() + datetime.timedelta(seconds=period)
    with open(sys.path[0]+'/gmm_data.json','r',encoding='utf-8') as f:
        gmm_data = json.load(f)
    while datetime.datetime.now() < endtime:
        gmmobjList = gmm_data["GmmobjList"]
        gmm_data['TimeStamp']=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for item in gmmobjList:
            item['power'] = random.random() * 10000
            item['voltage'] = random.random() * 10000
            item['electricity'] = random.random() * 10000
            item['gmm_obligate1'] = random.random() * 10000
            item['gmm_obligate2'] = random.random() * 10000
            item['gmm_obligate3'] = random.random() * 10000
            item['gmm_obligate4'] = random.random() * 10000
            item['gmm_obligate5'] = random.random() * 10000
            item['gmm_obligate6'] = random.random() * 10000
            item['gmm_obligate7'] = random.random() * 10000
            item['gmm_obligate8'] = random.random() * 10000
            item['gmm_obligate9'] = random.random() * 10000
            item['gmm_obligate10'] = random.random() * 10000

        gmm_data['ENVObj']['daily_accumulate_amplitude'] = random.uniform(1, 50)
        gmm_data['ENVObj']['accumulate_amplitude'] = random.uniform(1, 50)
        gmm_data['ENVObj']['env_temperature'] = random.uniform(1, 50)
        gmm_data['ENVObj']['cell_temperature'] = random.uniform(1, 50)
        gmm_data['ENVObj']['wind_speed'] = random.uniform(1, 50)
        gmm_data['ENVObj']['wind_direction'] = random.uniform(1, 50)
        gmm_data['ENVObj']['GHI'] = random.uniform(1, 50)
        gmm_data['ENVObj']['DNI'] = random.uniform(1, 50)

        gmm_data['ENVObj']['env_obligate1'] = random.uniform(1, 50)
        gmm_data['ENVObj']['env_obligate2'] = random.uniform(1, 50)
        gmm_data['ENVObj']['env_obligate3'] = random.uniform(1, 50)
        gmm_data['ENVObj']['env_obligate4'] = random.uniform(1, 50)
        gmm_data['ENVObj']['env_obligate5'] = random.uniform(1, 50)
        gmm_data['ENVObj']['env_obligate6'] = random.uniform(1, 50)
        gmm_data['ENVObj']['env_obligate7'] = random.uniform(1, 50)
        gmm_data['ENVObj']['env_obligate8'] = random.uniform(1, 50)
        gmm_data['ENVObj']['env_obligate9'] = random.uniform(1, 50)
        gmm_data['ENVObj']['env_obligate10'] = random.uniform(1, 50)
        channel.basic_publish(exchange='', routing_key='siemense_queue', body=json.dumps(gmm_data))
        time.sleep(5)
    connection.close()