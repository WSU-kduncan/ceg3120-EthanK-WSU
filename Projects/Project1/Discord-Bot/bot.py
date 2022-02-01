import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    hackers_quotes = [
        'There is no right or wrong, just fun and boring.',
		'Yo, check this out, guy. This is insanely great. It\'s got a 28.8 bps modem!',
		'Kid, don\'t threaten me. There are worse things than death, and uh, I can do all of them.',
		'Remember, hacking is more than just a crime. It\'s a survival trait.'
    ]

    gifs = [
		'https://i.imgur.com/5dpahn2.mp4',
		'https://i.imgur.com/y2HaS0v.mp4',
		'https://i.imgur.com/A8RBW7w.mp4',
		'https://pbs.twimg.com/media/FKC8dzXXoAE9O6O.jpg:large',
		'https://gfycat.com/unselfishblushingharvestmouse',
    ]


    if message.content == 'Hack the planet!':
        response = random.choice(hackers_quotes)
        await message.channel.send(response)

    elif message.content == '!gifme':
        response = random.choice(gifs)
        await message.channel.send(response)

client.run(TOKEN)
