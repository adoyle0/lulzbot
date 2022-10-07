motd ='''                              
 _          _         ____   ___  _    
| |   _   _| |    ___| __ ) / _ \| |_  
| |  | | | | |   |_  /  _ \| | | | __| 
| |__| |_| | |___ / /| |_) | |_| | |_  
|_____\__,_|_____/___|____/ \___/ \__| 
'''
menu = '''```
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

# Discord
import discord, datetime
import numpy as np
from fortune import fortune
from modules.ligma import ligma
from modules.limericks import limerick

TOKEN = open('.sekrit/discord_token').read()
chuck = open('chucknorris').read().split('\n%\n')
client = discord.Client(activity=discord.Game(name='with myself'))

# NLP
from transformers.models.auto.tokenization_auto import AutoTokenizer
from transformers.models.auto.modeling_auto import AutoModelForCausalLM
import torch

tokenizer = AutoTokenizer.from_pretrained('microsoft/DialoGPT-large')
model = AutoModelForCausalLM.from_pretrained('../southpark/output-medium')

# Twitter
import tweepy

twit_sekrit = open('.sekrit/twit_sekrit').read().split('\n')
api_key = twit_sekrit[0]
api_key_secret = twit_sekrit[1]
bearer_token = twit_sekrit[2]
access_token = twit_sekrit[3]
access_token_secret = twit_sekrit[4]
tclient = tweepy.Client(bearer_token,api_key,api_key_secret,access_token,access_token_secret)

# Functions
def user_tweet(twitter):
    statuses = tclient.get_users_tweets(twitter, exclude=['replies'], max_results=5)
    return statuses[0][0]

def cartman_speak(user_message):
    new_user_input_ids = tokenizer.encode(user_message + tokenizer.eos_token, return_tensors='pt')
    bot_output = new_user_input_ids
    bot_input_ids = torch.cat([new_user_input_ids, bot_output])
    bot_output = model.generate(
        bot_input_ids, max_length= 200,
        pad_token_id=tokenizer.eos_token_id,
        no_repeat_ngram_size=3,
        do_sample=True,
        top_k=100,
        top_p=0.7,
        temperature=.8
    )

    return '{}'.format(tokenizer.decode(bot_output[:,bot_input_ids.shape[-1]:][0], skip_special_tokens=True))

def message_handler(message):
    handler = {'musk': user_tweet(44196397),
               'lulzbot': menu,
               'deez': ligma(),
               'ligma': ligma(),
               'bofa': ligma(),
               'bopha': ligma(),
               'limerick': limerick(),
               'limrick': limerick(),
               'prost!': 'https://tenor.com/view/prost-christoph-waltz-django-bier-zum-wohle-gif-11041516',
               'fortune': fortune(),
               'chuck': np.random.choice(chuck),
               }

    if message in handler:
        return handler.get(message)
    else:
        return

# Main
@client.event
async def on_ready():
    print(motd+'\n'+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'\nLogged in as {0.user}'.format(client))
    return

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'cartman':
        async with message.channel.typing():
            await message.channel.send(cartman_speak(user_message))
            return

    if message.channel.name == 'shitposting':
        async with message.channel.typing():
            await message.channel.send(message_handler(user_message))
            return

client.run(TOKEN)
