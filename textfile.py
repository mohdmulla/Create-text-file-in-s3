import json
import base64
import boto3

BUCKET_NAME = 'enteryourbucketname'
def lambda_handler(event, context):
    string = event['content']
    file_content = string.encode("utf-8")
    file_path = 'enteryourfilename'
    s3 = boto3.client('s3')
    
    try:
        s3_response = s3.put_object(Bucket=BUCKET_NAME, Key=file_path, Body=file_content)
    except Exception as e:
        raise IOError(e)
        
    return {
        'statusCode': 200,
        'body': {
            'file_path': file_path
        }
    }
