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
import getpass  # For secure token input

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='ping')
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.send(f'Pong! Latency: {latency}ms')

def main():
    # Get token securely (input won't be visible in terminal)
    token = getpass.getpass("Enter your bot token: ")
    
    try:
        bot.run(token)
    except discord.LoginFailure:
        print("Invalid token! Please check your token and try again.")
