import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add lambda folder to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lambda'))

with patch('boto3.resource') as mock_dynamodb_resource:
    mock_table = MagicMock()
    mock_dynamodb_resource.return_value.Table.return_value = mock_table
    import createTask

class TestCreateTask(unittest.TestCase):

    @patch.object(createTask, 'table')
    def test_lambda_handler_success(self, mock_table):
        # Arrange
        event = {
            'body': '{"taskId": "1", "title": "Test Task", "status": "pending"}'
        }
        context = {}

        # Set up mock return value
        mock_table.put_item.return_value = {}

        # Act
        response = createTask.lambda_handler(event, context)

        # Assert
        mock_table.put_item.assert_called_once()
        self.assertEqual(response['statusCode'], 201)
        self.assertIn('Task created', response['body'])

if __name__ == '__main__':
    unittest.main()
