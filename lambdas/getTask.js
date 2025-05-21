const AWS = require('aws-sdk');
const dynamo = new AWS.DynamoDB.DocumentClient();
 
exports.handler = async () => {
  const params = {
    TableName: 'ToDoTable'
  };
 
  const result = await dynamo.scan(params).promise();
  return {
    statusCode: 200,
    body: JSON.stringify(result.Items)
  };
};
