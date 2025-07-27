import unittest
from unittest.mock import patch
import sys
import os

# Add lambda folder to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lambda'))

import createTask

class TestCreateTask(unittest.TestCase):

    @patch('createTask.table')
    def test_lambda_handler_success(self, mock_table):
        # Arrange
        event = {
            'body': '{"taskId": "1", "title": "Test Task", "status": "pending"}'
        }
        context = {}

        # Act
        response = createTask.lambda_handler(event, context)

        # Assert
        mock_table.put_item.assert_called_once()
        self.assertEqual(response['statusCode'], 201)
        self.assertIn('Task created', response['body'])

if __name__ == '__main__':
    unittest.main()
