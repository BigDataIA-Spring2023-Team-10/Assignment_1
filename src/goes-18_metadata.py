import os
import boto3
import logging
from dotenv import load_dotenv
import csv
from csv import writer


load_dotenv() #loads all environment variables from .env file 

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
             
            data_str = val[1:4]
            
            # Too large to write to csv 
            # with open("sql_data.csv",'a') as f_obj:
            #     writer_obj = writer(f_obj)
                
            #     writer_obj.writerow(data_str)
                
            #     f_obj.close()
    
            
        

        
