import discord
from discord.ext import commands

# Create an instance of the bot with a command prefix
bot = commands.Bot(command_prefix='!')

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Command: Ping
@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')

# Command: Hello
@bot.command(name='hello')
async def hello(ctx):
    await ctx.send('Hello!')

# Replace 'YOUR_TOKEN' with your actual bot token
bot.run('YOUR_TOKEN')
