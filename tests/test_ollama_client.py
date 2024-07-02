import unittest
from unittest.mock import patch, MagicMock
import sys
import os
import json

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from ollama_client import OllamaClient

class TestOllamaClient(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.client = OllamaClient()

    @patch('aiohttp.ClientSession.post')
    async def test_generate(self, mock_post):
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.text.return_value = json.dumps({"response": "Test response"})
        mock_post.return_value.__aenter__.return_value = mock_response

        response = await self.client.generate("Test prompt")
        self.assertEqual(response, "Test response")

    def test_parse_response(self):
        test_response = '{"response": "Hello"}\n{"response": " world!"}'
        parsed = self.client.parse_response(test_response)
        self.assertEqual(parsed, "Hello world!")

if __name__ == '__main__':
    unittest.main()