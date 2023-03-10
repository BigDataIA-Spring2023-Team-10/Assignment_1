import boto3
import time
from dotenv import load_dotenv
import os

#loading env variables
load_dotenv()

# Define the AWS access key and secret
aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
logGroupName=os.environ.get('LOG_GROUP_NAME')
logStreamName=os.environ.get('LOG_STREAM_NAME_AWS')
bucket_name=os.environ.get('MY_BUCKET_NAME')

# Create an S3 client using the access key and secret
def init_resources():
    s3 = boto3.resource(
        "s3",
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name='us-east-1'
    )
    cloudwatch = boto3.client('logs', 
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name='us-east-1')
    return cloudwatch,s3

def creat_logs(cloudwatch,msg):
    cloudwatch.put_log_events(
                logGroupName=logGroupName,
                logStreamName=logStreamName,
                logEvents=[
                        {
                            'timestamp': int(time.time() * 1000),
                            'message': msg
                        },
                    ]
            )
# Write a file to an S3 bucket
def copy_file_into_s3(source_bucket,key):
    cloudwatch,s3=init_resources()
    copy_source = {
        'Bucket': source_bucket,
        'Key': key
        }
    try:  
        bucket = s3.Bucket(bucket_name)
        bucket.copy(copy_source, key)
        creat_logs(cloudwatch=cloudwatch,msg="Copy succes for file: "+ str(key))
        return True
    except Exception as e:
        creat_logs(cloudwatch=cloudwatch,msg="Exception "+ str(e))
        return False