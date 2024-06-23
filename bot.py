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
                    full_response = await response.text()
                    return self.parse_response(full_response)
                else:
                    return f"Error: {response.status}"

    def parse_response(self, response_text):
        lines = response_text.strip().split('\n')
        parsed_response = ""
        for line in lines:
            try:
                data = json.loads(line)
                if 'response' in data:
                    parsed_response += data['response']
            except json.JSONDecodeError:
                continue
        return parsed_response.strip()

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
    
    # Prepare the full response
    full_response = f"Question: {question}\n\nAnswer: {response}"
    
    # Split the response into chunks of 2000 characters or less
    chunks = [full_response[i:i+1900] for i in range(0, len(full_response), 1900)]
    
    # Send the first chunk
    await interaction.followup.send(chunks[0])
    
    # Send any remaining chunks
    for chunk in chunks[1:]:
        await interaction.followup.send(chunk)

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')

client.run('YOUR_DISCORD_BOT_TOKEN')