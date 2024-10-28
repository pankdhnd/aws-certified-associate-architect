# You need to create a Role with access to SSM Parameter Store and KMS decrypt permission to run this code

import json
import boto3
import os

ssm = boto3.client('ssm', region_name="ap-south-1")

def lambda_handler(event, context):
    db_url = ssm.get_parameters(Names=["/my_app/dev/database_url"])
    print(db_url)   
    db_password = ssm.get_parameters(Names=["/my_app/dev/database-password"], WithDecryption=True)
    print(db_password)
    return "It works!"