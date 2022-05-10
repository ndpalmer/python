# Import required modules
import json
import boto3
import os
from uuid import uuid4
import tweepy


def lambda_handler(event, context):
    # Twitter credentials
    CONSUMER_KEY = os.environ['CONSUMER_KEY']
    CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
    ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
    ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

    # Twitter authentication
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    
    # s3 client and bucket
    s3client = boto3.client('s3')
    s3 = boto3.resource('s3')
    bucket_name = os.environ['S3_BUCKET_NAME']
    s3bucket = s3.Bucket(bucket_name)
    
    # Get random image from s3 bucket
    list_response = s3client.list_objects_v2(
        Bucket=bucket_name,
        MaxKeys=1,
        StartAfter=str(uuid4().hex)
        )
        
    if 'Contents' in list_response:
        key = list_response['Contents'][0]['Key']
            
        # Download jpg from s3 and save to /tmp
        pic = s3.Bucket(bucket_name).download_file(key, '/tmp/local.jpg')
            
        # Tweet picture
        user = api
        user.update_with_media('/tmp/local.jpg')
            
        # Delete local image
        os.remove('/tmp/local.jpg')
    else:
        break

return {"statusCode": 200}