import discord
from discord.ext import commands
import random

# Create an instance of the bot with a command prefix
bot = commands.Bot(command_prefix='!')

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Command: Love Calculator
@bot.command(name='lovecalc', aliases=['love'])
async def love_calc(ctx, *, couple):
    # Generate a random love percentage (0 to 100)
    love_percentage = random.randint(0, 100)

    # Respond with the love percentage
    response = f"Love percentage between {couple} is {love_percentage}% ❤️"
    await ctx.send(response)

# Replace 'YOUR_TOKEN' with your actual bot token
bot.run('YOUR_TOKEN')
