import json

# import requests


def lambda_handler(event, context):

    print(json.dumps(event))

    record = event['Records'][0]

    s3bucket = record['s3']['bucket']['name']
    s3object = record['s3']['object']['key']

    print(s3bucket, s3object)
