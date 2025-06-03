import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tasks')

def lambda_handler(event, context):
    data = json.loads(event['body'])

    table.put_item(Item={
        'taskId': data['taskId'],
        'title': data['title'],
        'status': data['status']
    })

    return {
        'statusCode': 201,
        'body': json.dumps({'message': 'Task created'})
    }
