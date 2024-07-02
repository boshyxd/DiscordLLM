import unittest
from unittest.mock import patch, MagicMock
from discord.ext import commands
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from bot import MyClient

class TestBot(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.bot = MyClient(intents=MagicMock())

    @patch('discord.Client.login')
    async def test_bot_login(self, mock_login):
        await self.bot.login('dummy_token')
        mock_login.assert_called_once_with('dummy_token')

    @patch('discord.Client.connect')
    async def test_bot_connect(self, mock_connect):
        await self.bot.connect()
        mock_connect.assert_called_once()

    async def test_on_ready(self):
        with patch('builtins.print') as mock_print:
            await self.bot.on_ready()
            mock_print.assert_called()

if __name__ == '__main__':
    unittest.main()