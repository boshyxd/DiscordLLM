import unittest
from unittest.mock import AsyncMock, patch
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

from commands.plot_command import plot

class TestPlotCommand(unittest.IsolatedAsyncioTestCase):
    @patch('matplotlib.pyplot.savefig')
    async def test_plot_command(self, mock_savefig):
        interaction = AsyncMock()
        interaction.response.defer = AsyncMock()
        interaction.followup.send = AsyncMock()

        await plot(interaction, "1,2,3", "4,5,6", "line")

        interaction.response.defer.assert_called_once()
        mock_savefig.assert_called_once()
        interaction.followup.send.assert_called_once()
        self.assertIsInstance(interaction.followup.send.call_args[1]['file'], object)

    async def test_plot_command_invalid_type(self):
        interaction = AsyncMock()
        interaction.response.defer = AsyncMock()
        interaction.followup.send = AsyncMock()

        await plot(interaction, "1,2,3", "4,5,6", "invalid_type")

        interaction.response.defer.assert_called_once()
        interaction.followup.send.assert_called_once_with("Invalid plot type. Supported types are 'line', 'scatter', and 'bar'.")

if __name__ == '__main__':
    unittest.main()