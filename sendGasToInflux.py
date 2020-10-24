#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import csv
import sys
import influxdb

filename=sys.argv[1]

data = []
client = influxdb.InfluxDBClient('influxdb', 8086, 'admin', 'admin', 'iotdb')
with open(filename, 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        try:
            year=int(float(row[1]))
            month=int(float(row[2]))
            day=int(float(row[3]))
            gazIndex=row[4]
            epochDate=int(datetime.datetime(year,month,day,10,0).timestamp()*1000000000)
            try:
                gazDay = float(row[5])
            except ValueError:
                print("Empty index, set to 0")
                gazDay = float(0)
            data.append(
                {
                    "measurement": "Compteur",
                    "tags": { "energy": "gas" },
                    "time": epochDate,
                    "fields": {"value" : float(gazDay)}
                }
            )
        except ValueError:
            print("Sorry, that's not a valid float")
    if (client.write_points(data)):
        print("Inserted.")
    else:
        print("Insertion error !!!")
