import unittest
from unittest.mock import patch, MagicMock
import json
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lambda'))

with patch('boto3.resource') as mock_dynamodb_resource:
    mock_table = MagicMock()
    mock_dynamodb_resource.return_value.Table.return_value = mock_table
    import updateTask

class TestUpdateTask(unittest.TestCase):

    @patch.object(updateTask, 'table')
    def test_lambda_handler_success(self, mock_table):
        event = {
            'body': json.dumps({
                'taskId': '1',
                'title': 'Updated Task',
                'status': 'completed'
            })
        }
        context = {}
        mock_table.update_item.return_value = {}

        response = updateTask.lambda_handler(event, context)
        self.assertEqual(response['statusCode'], 200)
        self.assertIn('Task updated', response['body'])

if __name__ == '__main__':
    unittest.main()
