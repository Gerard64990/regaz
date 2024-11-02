#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import datetime
import sys
import influxdb

url="https://www.myregaz.com/api/login_check"
headers = {'content-type': 'application/json'}
payload = '{"username":"leboncoin33700+regaz@gmail.com","password":"drogba64Regaz"}'
r = requests.post(url, data=payload, headers=headers)
token=r.json()

url="https://www.myregaz.com/api/consumption/183109/statistics/level/day"
headers = {'content-type': 'application/json', "Authorization": "Bearer "+token["token"] }
payload = '{"month":"'+sys.argv[2]+'","year":"'+sys.argv[1]+'"}'
r = requests.post(url, data=payload, headers=headers)
res=r.json()

data = []
client = influxdb.InfluxDBClient('influxdb', 8086, 'admin', 'admin', 'iotdb')
for i in res:
    epochDate=int(datetime.datetime(i["DG_ANNEE"], i["DG_MOIS"], i["DG_JOUR"], 10, 0).timestamp()*1000000000)
    data.append(
    {
        "measurement": "Compteur",
        "tags": { "energy": "gas" },
        "time": epochDate,
        "fields": {"value" : float(i["DG_VALEUR"])*0.1}
    })
if (client.write_points(data)):
    print("Inserted.")
else:
    print("Insertion error !!!")