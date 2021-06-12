import json

import boto3

from dummy_layer import call_dummy

s3 = boto3.client("s3")


def lambda_handler(event, context):
    print(call_dummy())
    print(s3.list_buckets())
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
