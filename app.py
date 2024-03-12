import discord
from discord.ext import commands
import requests
from io import BytesIO

# Bot token
TOKEN = "" # Your bot token go here

# Animated pfp link
animated_pfp_url = "https://media1.tenor.com/m/JS3CHwyWNiYAAAAd/lola-bunny-space-jam.gif" # Your new pfp link go here

# Create bot instance with intents
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

    # Change bot's profile picture
    await change_pfp(bot.user, animated_pfp_url)
    print('Profile picture changed successfully!')

async def change_pfp(user, pfp_url):
    # Download image
    response = requests.get(pfp_url)
    pfp_data = BytesIO(response.content)

    # Change profile picture
    await user.edit(avatar=pfp_data.read())

# Run the bot
bot.run(process.env.TOKEN)
