# coding=utf-8
import datetime
import json
import numpy as np
import sys
import time

from clickhouse_driver import Client

client = Client(host='localhost')

create_sql = ['use siemense',
              'create table  IF NOT EXISTS siemense_data (date Date default now(), TimeStamp String, GmmobjList Nested( '
              'id Array(String), desc Array(String), power Array(String) , voltage Array(String), electricity Array(String),'
              'gmm_obligate1 Array(Float32),'
              'gmm_obligate2 Array(Float32),'
              'gmm_obligate3 Array(Float32),'
              'gmm_obligate4 Array(Float32),'
              'gmm_obligate5 Array(Float32),'
              'gmm_obligate6 Array(Float32),'
              'gmm_obligate7 Array(Float32),'
              'gmm_obligate8 Array(Float32),'
              'gmm_obligate9 Array(Float32),'
              'gmm_obligate10 Array(Float32)'
              ')'
              ',ENVObj Nested('
              'daily_accumulate_amplitude String,'
              'accumulate_amplitude String,'
              'env_temperature String,'
              'cell_temperature String,'
              'wind_speed String,'
              'wind_direction String,'
              'GHI String,'
              'DNI String,'
              'longitude String,'
              'latitude String,'
              'direction_angle String,'
              'pitch_angle String,'
              'env_obligate1 String,'
              'env_obligate2 String,'
              'env_obligate3 String,'
              'env_obligate4 String,'
              'env_obligate5 String,'
              'env_obligate6 String,'
              'env_obligate7 String,'
              'env_obligate8 String,'
              'env_obligate9 String,'
              'env_obligate10 String'
              ')) ENGINE = MergeTree(date,(TimeStamp),8192)']
create_sql1 = ['use siemense', 'create table IF NOT EXISTS siemense_objlist ('
                               'date Date default now(),'
                               'TimeStamp Datetime,'
                               'id String,'
                               'desc String,'
                               'power Float32,'
                               'voltage Float32,'
                               'electricity Float32,'
                               'gmm_obligate1 Float32,'
                               'gmm_obligate2 Float32,'
                               'gmm_obligate3 Float32,'
                               'gmm_obligate4 Float32,'
                               'gmm_obligate5 Float32,'
                               'gmm_obligate6 Float32,'
                               'gmm_obligate7 Float32,'
                               'gmm_obligate8 Float32,'
                               'gmm_obligate9 Float32,'
                               'gmm_obligate10 Float32'
                               ') ENGINE =MergeTree(date,(TimeStamp,id),8192)','create table if not exists siemense_envobj('
                                    'date Date default now(),'
                                    'TimeStamp Datetime,'
                                    'daily_accumulate_amplitude Float32,'
                                    'accumulate_amplitude Float32,'
                                    'env_temperature Float32,'
                                    'cell_temperature Float32,'
                                    'wind_speed Float32,'
                                    'wind_direction String,'
                                    'GHI String,'
                                    'DNI String,'
                                    'longitude Float32 ,'
                                    'latitude Float32,'
                                    'direction_angle Int8 ,'
                                    'pitch_angle Int8 ,'
                                    'env_obligate1 Float32,'
                                    'env_obligate2 Float32,'
                                    'env_obligate3 Float32,'
                                    'env_obligate4 Float32,'
                                    'env_obligate5 Float32,'
                                    'env_obligate6 Float32,'
                                    'env_obligate7 Float32,'
                                    'env_obligate8 Float32,'
                                    'env_obligate9 Float32,'
                                    'env_obligate10 Float32'
                                    ')ENGINE =MergeTree(date,(TimeStamp),8192)']
# tables_sql = ['use siemense', 'show tables']
# test_sql = ['use siemense',
#             'create table if not exists test1 ( id String, env Array(Float32)) ENGINE = MergeTree().MergeTree']
# drop_sql = ['use siemense', 'drop table if exists siemense_objlist ']
#
# column_sql=['use siemense','desc siemense_objlist','desc siemense_envobj']
#
insert_data=[[datetime.datetime.now(),'0000000000000001', '35KV变电室35KV侧光伏', 0.4381068062949367, 8.57836574531886, 8.166177512367858, 1.735798046957192, 4.554073785826963, 6.8600725881115965, 3.3288826507160607, 0.40873888552199866, 1.1479763083709849, 5.733573961460834, 9.49443775781264, 2.839208555874931, 1.1063010134441076],
             [datetime.datetime.now(),'0000000000000002', '员工发展中心光伏', 9.453112953133564, 3.5975050737919023, 7.9988066459363925, 6.5008492661562665, 3.635803486098329, 4.940415755354665, 9.44285262803977, 7.467832033413747, 0.09444744152322437, 5.832209602811902, 8.226794235741442, 2.402255768403827, 2.430649159126074]]
table='siemense.siemense_objlist'
column=('TimeStamp','id','desc','power','voltage','electricity','gmm_obligate1','gmm_obligate2','gmm_obligate3','gmm_obligate4','gmm_obligate5','gmm_obligate6','gmm_obligate7','gmm_obligate8','gmm_obligate9','gmm_obligate10')
column1='(TimeStamp,id,desc,power,voltage,electricity,gmm_obligate1,gmm_obligate2,gmm_obligate3,gmm_obligate4,gmm_obligate5,gmm_obligate6,gmm_obligate7,gmm_obligate8,gmm_obligate9,gmm_obligate10)'
def insert(table, column, insert_data):
    client = Client('localhost')
    client.execute('INSERT INTO %s %s VALUES' % (table, column1), insert_data)
    print('INSERT INTO %s %s VALUES' % (table, column1), insert_data)
# insert(table,column,insert_data)
UTC_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
searchList=['power','voltage','electricity']
print(','.join(searchList)
search_sql="select "+','.join(searchList)+" from siemense.siemense_objlist where TimeStamp between '"+str(datetime.datetime.strptime('2019-06-30T16:00:00.000Z',UTC_FORMAT))+ "' AND '"+str(datetime.datetime.strptime('2019-07-30T16:00:00.000Z',UTC_FORMAT))+"'"
print(search_sql)
res=client.execute(search_sql)
print(res)
print(datetime.datetime.strptime('2019-06-30T16:00:00.000Z',UTC_FORMAT))


temp=[(5.820516586303711, 8.149868965148926, 3.7297847270965576), (8.451325416564941, 2.6761202812194824, 5.890068531036377), (0.43810680508613586, 8.578365325927734, 8.166177749633789), (9.453112602233887, 3.5975050926208496, 7.998806476593018)]
power=np.array(temp)

print(power)

print(str(datetime.datetime.now()))


def load_data_to_clickhouse():
    file = open(sys.path[0]+'\_tbea-gmmwapper_v2.json', 'r')
    data = json.load(file)
    obj1 = []
    obj2 = []
    obj3 = []
    obj4 = []
    for item in data:
        obj1.append([item['GMMObjs'][0]['power'], item['GMMObjs'][0]['electricity'], item['GMMObjs'][0]['voltage']])
        obj2.append([item['GMMObjs'][1]['power'], item['GMMObjs'][1]['electricity'], item['GMMObjs'][1]['voltage']])
        obj3.append([item['GMMObjs'][2]['power'], item['GMMObjs'][2]['electricity'], item['GMMObjs'][2]['voltage']])
        obj4.append([item['GMMObjs'][3]['power'], item['GMMObjs'][3]['electricity'], item['GMMObjs'][3]['voltage']])
    return [obj1, obj2, obj3, obj4]

# a=load_data_to_clickhouse()


mock_data_from_clickhouse()