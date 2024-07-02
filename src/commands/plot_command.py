import discord
from discord import app_commands
import pandas as pd
import matplotlib.pyplot as plt
import io

@app_commands.command()
async def plot(interaction: discord.Interaction, x_data: str, y_data: str, plot_type: str = 'line'):
    await interaction.response.defer()
    
    try:
        x = [float(x) for x in x_data.split(',')]
        y = [float(y) for y in y_data.split(',')]
        
        df = pd.DataFrame({'x': x, 'y': y})
        
        plt.figure(figsize=(10, 6))
        if plot_type == 'line':
            plt.plot(df['x'], df['y'])
        elif plot_type == 'scatter':
            plt.scatter(df['x'], df['y'])
        elif plot_type == 'bar':
            plt.bar(df['x'], df['y'])
        else:
            await interaction.followup.send("Invalid plot type. Supported types are 'line', 'scatter', and 'bar'.")
            return
        
        plt.title(f"{plot_type.capitalize()} Plot")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        
        await interaction.followup.send(file=discord.File(buf, filename='plot.png'))
    except Exception as e:
        await interaction.followup.send(f"An error occurred: {str(e)}")