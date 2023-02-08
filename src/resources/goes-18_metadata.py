import os
import boto3
import logging
from dotenv import load_dotenv
import csv
from csv import writer
import sqlite3

load_dotenv() #loads all environment variables from .env file 

#DB connection
conn = sqlite3.connect('src/data/GEOSPATIAL_DATA.db')
c = conn.cursor()
c.execute('''DROP TABLE IF EXISTS goes18meta''')
c.execute('''CREATE TABLE goes18meta
                   (year INTEGER, month INTEGER, hour INTEGER)''')


#establishing connection to s3 using boto3
s3client = boto3.client('s3',
                        region_name='us-east-1')

paginator = s3client.get_paginator('list_objects_v2')
pages = paginator.paginate(Bucket = "noaa-goes18")


for page in pages:
    # for obj in page['Contents']:
    #     print(obj)
    for content in page.get("Contents"):
        print(content.get("Key"))
        val = content.get("Key").split("/")
        
        if val[0] == "ABI-L1b-RadC":
             
            # data_str = val[1:4]

            c.execute("INSERT INTO goes18meta (year, month, hour) VALUES (?,?,?)", (val[1], val[2], val[3]))
    
