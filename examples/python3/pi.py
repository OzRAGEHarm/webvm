"""from decimal import Decimal, getcontext
getcontext().prec=60
summation = 0
for k in range(50):
	summation = summation + 1/Decimal(16)**k * (
		Decimal(4)/(8*k+1)
		- Decimal(2)/(8*k+4)
		- Decimal(1)/(8*k+5)
		- Decimal(1)/(8*k+6)
		)
	print(summation)
"""

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
TOKEN = 'MTA4MzYyODEwNDQ5MDE3MjQyOA.GFCWPh.-ld0MRJk6HwyexBfo7ieJBPaK9to7SPnoNTFos'

# Run the bot with the specified token
bot.run(TOKEN)
