import discord
from discord import app_commands
import os
from dotenv import load_dotenv

from .ollama_client import OllamaClient
from .commands import ask, plot, analyze

load_dotenv()  # Load environment variables from .env file

class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
        self.ollama_client = OllamaClient()

    async def setup_hook(self):
        await self.tree.sync()

intents = discord.Intents.default()
client = MyClient(intents=intents)

client.tree.add_command(ask)
client.tree.add_command(plot)
client.tree.add_command(analyze)

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')

if __name__ == '__main__':
    client.run(os.getenv('DISCORD_TOKEN'))