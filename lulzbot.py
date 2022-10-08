motd ='''                              
 _          _         ____   ___  _    
| |   _   _| |    ___| __ ) / _ \| |_  
| |  | | | | |   |_  /  _ \| | | | __| 
| |__| |_| | |___ / /| |_) | |_| | |_  
|_____\__,_|_____/___|____/ \___/ \__| 
'''
menu ='''```
Commands:
  fortune: tell a fortune
  chuck: give a Chuck Norris quote
  ligma: LIGMA BALLS
  bofa: deez
  deez: nutz
  limerick: tell a limerick
  prost!: prost!

Contribute!
    https://github.com/adoyle0/lulzbot```'''

import discord, datetime
import numpy as np
from fortune import fortune
from src.twitter import get_tweet
from src.cartman import cartman_speak
from src.limericks import limerick

chuck_quotes = open('src/chuck_quotes').read().split('\n%\n')
ligma_list = open('src/ligma_list').read().split('\n')

def show_menu():
    return menu

def musk():
    return get_tweet(44196397)

def ligma():
    return np.random.choice(ligma_list)

def prost():
    return 'https://tenor.com/view/prost-christoph-waltz-django-bier-zum-wohle-gif-11041516'

def chuck():
    return np.random.choice(chuck_quotes)

message_handler = {'lulzbot': show_menu, # these need to be functions
                      'musk': musk,
                      'deez': ligma,
                     'ligma': ligma,
                      'bofa': ligma,
                     'bopha': ligma,
                  'limerick': limerick,
                   'limrick': limerick,
                    'prost!': prost,
                   'fortune': fortune,
                     'chuck': chuck,
                   }

TOKEN = open('.sekrit/discord_token').read()
client = discord.Client(activity=discord.Game(name='with myself'))

@client.event
async def on_ready():
    print(motd+'\n'+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'\nLogged in as {0.user}'.format(client))
    return

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} ({channel}) {username}: {user_message}')

    if message.author == client.user:
        return

    elif message.channel.name == 'cartman':
        async with message.channel.typing():
            await message.channel.send(cartman_speak(user_message))

    elif message.channel.name == 'shitposting':
         if user_message in message_handler:
            await message.channel.send(message_handler[user_message]())
    return

client.run(TOKEN)
