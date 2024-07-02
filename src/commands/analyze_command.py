import discord
from discord import app_commands
import pandas as pd

@app_commands.command()
async def analyze(interaction: discord.Interaction, data: str):
    await interaction.response.defer()
    
    try:
        numbers = [float(x) for x in data.split(',')]
        df = pd.DataFrame(numbers, columns=['Value'])
        
        analysis = f"""
        Data Analysis:
        Count: {df['Value'].count()}
        Mean: {df['Value'].mean():.2f}
        Median: {df['Value'].median():.2f}
        Standard Deviation: {df['Value'].std():.2f}
        Min: {df['Value'].min():.2f}
        Max: {df['Value'].max():.2f}
        """
        
        await interaction.followup.send(analysis)
    except Exception as e:
        await interaction.followup.send(f"An error occurred: {str(e)}")