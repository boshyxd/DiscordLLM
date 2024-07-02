from discord import app_commands
import discord

@app_commands.command()
async def ask(interaction: discord.Interaction, question: str):
    await interaction.response.defer()
    client = interaction.client
    response = await client.ollama_client.generate(question)
    
    full_response = f"Question: {question}\n\nAnswer: {response}"
    chunks = [full_response[i:i+1900] for i in range(0, len(full_response), 1900)]
    
    await interaction.followup.send(chunks[0])
    for chunk in chunks[1:]:
        await interaction.followup.send(chunk)