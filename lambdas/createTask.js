const AWS = require('aws-sdk');
const { v4: uuidv4 } = require('uuid'); // Install uuid locally if testing
 
const dynamo = new AWS.DynamoDB.DocumentClient();
 
exports.handler = async (event) => {
  const data = JSON.parse(event.body);
  const params = {
    TableName: 'ToDoTable',
    Item: {
      id: uuidv4(),
      task: data.task,
      status: data.status || 'pending'
    }
  };
 
  await dynamo.put(params).promise();
  return {
    statusCode: 201,
    body: JSON.stringify({ message: 'Task created' })
  };
};
