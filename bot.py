import discord
import asyncio
from discord.ext import commands
import os
from dotenv import load_dotenv

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("Bot is online")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command/s")
    except Exception as e:
        print(e)

@bot.tree.command(name="hello", description="Typical hello command, output only visible to you.")
async def hello(interaction: discord.Interaction):
    interaction.response.defer()
    asyncio.sleep(3000)
    await interaction.followup.send(f"Hey {interaction.user.mention}! Slash command done.", ephemeral=True)


load_dotenv()
bot.run(os.getenv('TOKEN'))
