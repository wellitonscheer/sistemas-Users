import json
import boto3
import os
def lambda_handler(event, context):
    buidPut(event)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
def buidPut(event: dict):
    client:botocore.client.DynamoDB = boto3.client('dynamodb')
    table = 'whizlabdemo'
    id = 30
    idade = 17
    nome = "marin from cloud"
    response = client.put_item(
        Item= {
            'id': {
                'S': id,
            },
            'Idade': {
                'S': idade,
            },
            'Name': {
                'S': nome,
            },
        }, 
        TableName= table
    )
