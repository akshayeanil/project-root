import json
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tasks')

def lambda_handler(event, context):
    logger.info("Received event: %s", event)

    try:
        data = json.loads(event['body'])

        logger.info("Parsed task data: %s", data)

        table.put_item(Item={
            'taskId': data['taskId'],
            'title': data['title'],
            'status': data['status']
        })

        logger.info("Task inserted successfully into DynamoDB.")

        return {
            'statusCode': 201,
            'body': json.dumps({'message': 'Task created'})
        }

    except Exception as e:
        logger.error("Error occurred: %s", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Internal server error'})
        }
