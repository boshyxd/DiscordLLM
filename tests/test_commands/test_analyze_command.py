import unittest
from unittest.mock import AsyncMock
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

from commands.analyze_command import analyze

class TestAnalyzeCommand(unittest.IsolatedAsyncioTestCase):
    async def test_analyze_command(self):
        interaction = AsyncMock()
        interaction.response.defer = AsyncMock()
        interaction.followup.send = AsyncMock()

        await analyze(interaction, "1,2,3,4,5")

        interaction.response.defer.assert_called_once()
        interaction.followup.send.assert_called_once()
        sent_message = interaction.followup.send.call_args[0][0]
        self.assertIn("Count: 5", sent_message)
        self.assertIn("Mean: 3.00", sent_message)
        self.assertIn("Median: 3.00", sent_message)

    async def test_analyze_command_invalid_input(self):
        interaction = AsyncMock()
        interaction.response.defer = AsyncMock()
        interaction.followup.send = AsyncMock()

        await analyze(interaction, "1,2,3,invalid,5")

        interaction.response.defer.assert_called_once()
        interaction.followup.send.assert_called_once()
        sent_message = interaction.followup.send.call_args[0][0]
        self.assertIn("An error occurred", sent_message)

if __name__ == '__main__':
    unittest.main()