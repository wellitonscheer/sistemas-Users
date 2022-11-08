import json
import boto3
import os
def lambda_handler(event, context):
  buidPut()
  return {
    'statusCode': 200,
    'body': json.dumps('Hello from Lambda!')
  }
def buidPut():
  client:botocore.client.DynamoDB = boto3.client('dynamodb')
  table = "SistemasUsersDyDB"
  cpf = "30"
  age = "17"
  name = "marin kitagawa from cloud"
  response = client.put_item(
    Item= {
        'CPF': {
              'N': cpf,
          },
          'Name': {
              'S': name,
          },
          'Age': {
              'N': age,
          },
      }, 
    TableName= table
  )
