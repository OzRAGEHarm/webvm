import discord
from discord.ext import commands

# Create a new bot instance with a specified prefix
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)

# Event to indicate the bot is ready
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

# Command to respond with the bot's latency
@bot.command(name='ping')
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.send(f'Pong! Latency: {latency}ms')

# Token for your bot (replace with your own token)
TOKEN = 'MTA4MzYyODEwNDQ5MDE3MjQyOA.Gd1afX.kV6Z-sCtytEpzXoZt3cM0m-oU1m6tubZoXJ8qM'

# Run the bot with the specified token
bot.run(TOKEN)
