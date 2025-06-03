import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tasks')

def lambda_handler(event, context):
    task_id = event['pathParameters']['taskId']
    data = json.loads(event['body'])

    table.update_item(
        Key={'taskId': task_id},
        UpdateExpression="set title = :t, #s = :s",
        ExpressionAttributeValues={
            ':t': data['title'],
            ':s': data['status']
        },
        ExpressionAttributeNames={
            '#s': 'status'
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Task updated'})
    }
