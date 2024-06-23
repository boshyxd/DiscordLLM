import discord
from discord import app_commands
import aiohttp
import asyncio
import json

class OllamaClient:
    def __init__(self, base_url="http://localhost:11434"):
        self.base_url = base_url

    async def generate(self, prompt, model="qwen2:1.5b"):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.base_url}/api/generate",
                json={"model": model, "prompt": prompt}
            ) as response:
                if response.status == 200:
                    return await response.text()
                else:
                    return f"Error: {response.status}"

class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
        self.ollama_client = OllamaClient()

    async def setup_hook(self):
        await self.tree.sync()

intents = discord.Intents.default()
client = MyClient(intents=intents)

@client.tree.command()
async def ask(interaction: discord.Interaction, question: str):
    await interaction.response.defer()
    response = await client.ollama_client.generate(question)
    await interaction.followup.send(f"Question: {question}\n\nAnswer: {response}")

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')

client.run('YOUR_DISCORD_BOT_TOKEN')