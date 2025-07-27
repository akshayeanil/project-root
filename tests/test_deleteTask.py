import unittest
from unittest.mock import patch, MagicMock
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lambda'))

with patch('boto3.resource') as mock_dynamodb_resource:
    mock_table = MagicMock()
    mock_dynamodb_resource.return_value.Table.return_value = mock_table
    import deleteTask

class TestDeleteTask(unittest.TestCase):

    @patch.object(deleteTask, 'table')
    def test_lambda_handler_success(self, mock_table):
        event = {
            'pathParameters': {'taskId': '1'}
        }
        context = {}
        mock_table.delete_item.return_value = {}

        response = deleteTask.lambda_handler(event, context)
        self.assertEqual(response['statusCode'], 200)
        self.assertIn('Task deleted', response['body'])

if __name__ == '__main__':
    unittest.main()
