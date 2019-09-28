import json
import boto3
import urllib
import logging

# Create an S3 client
s3 = boto3.client('s3')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

logger.info("Loading function")

def main(event, context):
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    source_key = event['Records'][0]['s3']['object']['key']
    logger.info('Reading {} on {}'.format(source_key, source_bucket))
    copy_source = {'Bucket': source_bucket, 'Key': source_key}

    target_bucket = source_bucket
    target_key = source_key.replace("Incoming", "Processed")

    try:
        waiter = s3.get_waiter('object_exists')
        waiter.wait(Bucket=source_bucket, Key=source_key)
        s3.copy_object(Bucket=target_bucket, Key=target_key, CopySource=copy_source)
        logger.info('Copied {} on {}'.format(target_key, target_bucket))
    except Exception as e:
        logger.info(e)
