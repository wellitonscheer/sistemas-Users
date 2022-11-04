import json
import boto3
import os

def lambda_handler(event, context):
    buidPut(event)
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

def buidPut(event: dict):
    client:botocore.client.DynamoDB = boto3.client('dynamodb')
    table = 'whizlabdemo'
    """ pegando dados do evento
    id = event['id']
    idade = event['Idade']
    nome = event['Name']
    """
    """ pegando dados das variaveis de ambiente
    id = os.environ['id']
    idade = os.environ['Idade']
    nome = os.environ['Name']
    """
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
    #print("type response: ", type(response))
