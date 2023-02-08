import os
import boto3
import logging
from dotenv import load_dotenv
import csv
from csv import writer
import sqlite3

load_dotenv() #loads all environment variables from .env file 


conn = sqlite3.connect('src/data/GEOSPATIAL_DATA.db')
c = conn.cursor()
c.execute('''DROP TABLE IF EXISTS nexradmeta''')
c.execute('''CREATE TABLE nexradmeta
                   (year INTEGER, month INTEGER, hour INTEGER, stationcode TEXT)''')



#establishing connection to s3 using boto3
s3client = boto3.client('s3',
                        region_name='us-east-1')

paginator = s3client.get_paginator('list_objects_v2')
pages = paginator.paginate(Bucket = "noaa-nexrad-level2")


for page in pages:
    # for obj in page['Contents']:
    #     print(obj)
    for content in page.get("Contents"):
        # print(content.get("Key"))
        val = content.get("Key").split("/")
        data_str = val[0:4]
        # print(data_str)
        
        c.execute("INSERT INTO nexradmeta (year, month, hour, stationcode) VALUES (?,?,?,?)", (val[0], val[1], val[2], val[3]))
        