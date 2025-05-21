const AWS = require('aws-sdk');
const dynamo = new AWS.DynamoDB.DocumentClient();
 
exports.handler = async (event) => {
  const { id } = event.pathParameters;
  const data = JSON.parse(event.body);
 
  const params = {
    TableName: 'ToDoTable',
    Key: { id },
    UpdateExpression: 'set task = :task, status = :status',
    ExpressionAttributeValues: {
      ':task': data.task,
      ':status': data.status
    },
    ReturnValues: 'UPDATED_NEW'
  };
 
  await dynamo.update(params).promise();
  return {
    statusCode: 200,
    body: JSON.stringify({ message: 'Task updated' })
  };
};
