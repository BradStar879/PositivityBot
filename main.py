import os
import random
from discord.ext import commands
from discord.ext import tasks
import discord

TOKEN = os.getenv('TOKEN')

# intents = discord.Intents(messages=True)
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

greetings = [
    "Hey there",
    "Hey"
    "Hi",
    "Hi there",
    "Hello",
    "Greetings",
    "Hiya",
    "Yo",
]

openers = [
    "I just wanted to say",
    "Can I just say",
    "I've been meaning to tell you",
    "I couldn't help but notice",
    "I just have to say",
    "I wanted to take a moment to remind you",
    "You know I just noticed",
    "You deserve to hear",
    "I wanted to share with you",
    "I've been waiting to tell you",
    "Every time I see you I'm reminded",
]

compliments = [
    "how cute you are",
    "how stylish you always look",
    "how impressed I am by your dedication",
    "that I always appreciate the time I spend talking with you",
    "that your sense of humor never fails to brighten my day",
    "that it's always nice to be around you",
    "that you have a natural gift for making people feel welcomed and appreciated",
    "that your positive attitude is absolutely infectious",
    "that your generosity knows no bounds",
    "that I am continuously inspired by your determination",
    "that you have remarkable artistic talent",
    "that doing anything with you makes it so much better",
    "that your energy is contagious",
    "that your inner beauty shines brighter than any star",
    "that your grace and poise are only matched by splendid charm",
    "that you have an effortless elegance wherever you go",
    "that your passion is evident in everything that you do",
    "that you always know how to make me laugh",
    "that your sense of adventure always keeps me on my toes",
    "that you have a genuine warmth and kindness that radiates from within",
    "that you have a beautiful soul that can be seen miles away",
    "that you have an infectious enthusiasm for life that's impossible to ignore",
    "that you have the invaluable ability to comfort people in their times of need",
]

features = [
    "talent",
    "smile",
    "eyes",
    "personality",
    "creativity",
    "kindness",
    "laugh",
    "sense of humor",
    "heart",
    "generosity",
    "caring nature",
    "attention to detail",
    "voice",
    "energy",
    "compassion",
    "passion",
    "determination",
]

adjectives = [
    "amazing",
    "wonderful",
    "beautiful",
    "jaw-dropping",
    "incredible",
    "awe-inspiring",
    "impeccable",
    "second-to-none",
    "radiant",
    "charming",
    "captivating",
    "elegant",
    "enchanting",
    "exquisite",
    "alluring",
    "graceful",
    "magnetic",
    "delightful",
    "breathtaking",
    "glorious",
    "endearing",
    "glowing",
]

appreciations = [
    "You are truly inspiring",
    "You brighten up my day",
    "You are a joy to be around",
    "You are an amazing person",
    "I'm grateful to have you in my life",
    "Your presence makes everything better",
    "I appreciate everything you do",
    "Thanks for being you",
    "I'm lucky to know you",
    "You are truly a blessing",
    "I'm thankful to be around you",
    "You make the world a better place",
    "You exude such natural beauty inside and out",
]

feature_appreciations = [
    "It's truly inspiring",
    "It brightens up my day",
    "It's a joy to see",
    "It truly is wonderful",
    "It's like no other",
    "It's hard to describe with words",
    "It is an absolute honor to see it",
    "It lights up the room",
    "It brings a smile to peoples' faces",
    "It spreads happiness wherever you go",
    "It makes you stand out in the best way possible",
]

closers = [
    "It's always nice to see you",
    "I can't wait to see you again",
    "It's been a pleasure as always",
    "Keep shining bright",
    "Stay awesome",
    "Take care",
    "Til next time",
    "See you later",
    "Keep on keeping on",
    "Wishing you the best",
    "Goodbye for now",
    "See you soon",
]


def generate_full_compliment():
    return generate_opener() + generate_compliment() + generate_closer()


def generate_opener():
    return random.choice(greetings) + "! " + random.choice(openers) + " "


def generate_compliment():
    if random.randint(1, 10) <= 3:
        return random.choice(compliments) + "! " + random.choice(appreciations) + ". "
    else:
        return "that your " + random.choice(features) + " is " + random.choice(adjectives) + "! " + \
                            random.choice(feature_appreciations) + ". "


def generate_closer():
    return random.choice(closers) + "!"


@bot.event
async def on_ready():
    print("online")


@bot.command(name='compliment')
async def compliment(ctx):
    response = generate_full_compliment()
    await ctx.send(response)


@tasks.loop(seconds=5.0, minutes=0, hours=0, count=None)
async def test():
    await bot.get_channel(1101983834523848705).send('test')


bot.run(TOKEN)
test.start()
