import os
import json
import uuid
import boto3

def lambda_handler(event, context):
    # Define s3 client and bucket names
    s3client = boto3.client('s3')
    s3 = boto3.resource('s3')
    source_bucket = os.environ['S3_SOURCE_BUCKET']
    dest_bucket = os.environ['S3_DEST_BUCKET']
    s3bucket = s3.Bucket(source_bucket)
    
    # Create list of objects in source bucket
    objects = s3client.list_objects_v2(Bucket=source_bucket)
    
    # For each item in source bucket object list, copy to destination and rename. 
    for obj in objects['Contents']:
        copy_source = {'Bucket': source_bucket, 'Key': obj['Key']}
        
        # Generate a random name and append appropriate file extension.
        if obj['Key'].lower.endswith('.jpg'):
            new_key = str(uuid.uuid4().hex) + ".jpg"
        elif obj['Key'].lower.endswith('.jpeg'):
            new_key = str(uuid.uuid4().hex) + ".jpeg"
        elif obj['Key'].lower.endswith('.png'):
            new_key = str(uuid.uuid4().hex) + ".png"
        elif obj['Key'].lower.endswith('.webp'):
            new_key = str(uuid.uuid4().hex) + ".webp"
        else
            print("Uknown file format.")
        
        # Copy file to destination bucket and rename it.
        s3.Object(dest_bucket,new_key).copy_from(CopySource=copy_source)
        
        # Delete file in source bucket.
        s3.Object(source_bucket,obj['Key']).delete()

    return {
        'statusCode': 200,
        'body': json.dumps('Rename complete.')
    }