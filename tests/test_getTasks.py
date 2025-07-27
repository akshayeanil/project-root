import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add lambda folder to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lambda'))

with patch('boto3.resource') as mock_dynamodb_resource:
    mock_table = MagicMock()
    mock_dynamodb_resource.return_value.Table.return_value = mock_table
    import getTasks

class TestGetTasks(unittest.TestCase):

    @patch.object(getTasks, 'table')
    def test_lambda_handler_success(self, mock_table):
        mock_table.scan.return_value = {
            'Items': [{'taskId': '1', 'title': 'Sample Task', 'status': 'pending'}]
        }
        event = {}
        context = {}
        response = getTasks.lambda_handler(event, context)
        self.assertEqual(response['statusCode'], 200)
        self.assertIn('Sample Task', response['body'])

if __name__ == '__main__':
    unittest.main()
