import unittest
from unittest.mock import AsyncMock, patch
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

from commands.ask_command import ask

class TestAskCommand(unittest.IsolatedAsyncioTestCase):
    async def test_ask_command(self):
        interaction = AsyncMock()
        interaction.response.defer = AsyncMock()
        interaction.followup.send = AsyncMock()
        interaction.client.ollama_client.generate = AsyncMock(return_value="Test response")

        await ask(interaction, "Test question")

        interaction.response.defer.assert_called_once()
        interaction.client.ollama_client.generate.assert_called_once_with("Test question")
        interaction.followup.send.assert_called_once()
        self.assertIn("Test response", interaction.followup.send.call_args[0][0])

if __name__ == '__main__':
    unittest.main()