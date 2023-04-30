import os
import random
from discord.ext import commands
from discord.ext import tasks
import discord
# from dotenv import load_dotenv


# load_dotenv()
# TOKEN = os.getenv('DISCORD_TOKEN')
TOKEN = 'NTk1ODIzNjM3Mzg3MjgwMzg0.GHxR_6.HxbdGOBJ9GK3e7bSnkJxup4ZAYFaADVCCMNIqI'

# intents = discord.Intents(messages=True)
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    if not test.is_running():
        test.start()


@bot.command(name='compliment')
async def compliment(ctx):
    compliments = [
        'You cute',
        'I wub u',
    ]

    response = random.choice(compliments)
    await ctx.send(response)


@tasks.loop(seconds=5.0, minutes=0, hours=0, count=None)
async def test():
    await bot.get_channel(1101983834523848705).send('test')

bot.run(TOKEN)
test.start()
