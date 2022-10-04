motd ='                                 \n\
 _          _         ____   ___  _     \n\
| |   _   _| |    ___| __ ) / _ \| |_   \n\
| |  | | | | |   |_  /  _ \| | | | __|  \n\
| |__| |_| | |___ / /| |_) | |_| | |_   \n\
|_____\__,_|_____/___|____/ \___/ \__|  \n\
'
# Discord Bot
import discord, datetime, time
from fortune import fortune
from ligma import ligma
from limericks import limerick

TOKEN = open('discord_token').read()
chuck = open('chucknorris').read().split('\n%\n')
client = discord.Client(activity=discord.Game(name='with myself'))

# NLP
import numpy as np
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

tokenizer = AutoTokenizer.from_pretrained('microsoft/DialoGPT-large')
model = AutoModelForCausalLM.from_pretrained('../southpark/output-medium')

# Twitter
import tweepy

twit_sekrit = open('twit_sekrit').read().split('\n')
api_key = twit_sekrit[0]
api_key_secret = twit_sekrit[1]
bearer_token = twit_sekrit[2]
access_token = twit_sekrit[3]
access_token_secret = twit_sekrit[4]
tclient = tweepy.Client(bearer_token,api_key,api_key_secret,access_token,access_token_secret)

def user_tweet(twitter):
    statuses = tclient.get_users_tweets(44196397, exclude=['replies'], max_results=5)
    return statuses[0][0]

menu = '```\n\
Commands:\n\
  fortune: tell a fortune\n\
  chuck: give a Chuck Norris quote\n\
  ligma: LIGMA BALLS\n\
  bofa: deez\n\
  deez: nutz\n\
  limerick: tell a limerick\n\
  prost!: prost!\n\
  \n\
Contribute!\
    https://github.com/adoyle0/lulzbot```'

# Init
@client.event
async def on_ready():
    print(motd+'\n'+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'\nLogged in as {0.user}'.format(client))

# Monitor Incoming
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
            await message.channel.send('{}'.format(tokenizer.decode(bot_output[:,bot_input_ids.shape[-1]:][0], skip_special_tokens=True)))
            return

    if message.channel.name == 'shitposting':
        if user_message.lower().count('musk') > 0:
            await message.channel.send(user_tweet('elonmusk'))
            return

        elif user_message.lower() == 'lulzbot' or user_message == 'ligmabot' or user_message == 'L1gMaB0t' or user_message == 'help':
            await message.channel.send(menu)
            return

        elif user_message.lower().count('deez') > 0 or user_message.lower().count('bofa') > 0 or user_message.lower().count('ligma') > 0 or user_message.lower().count('l1gma') > 0 or user_message.lower().count('l1gm4') > 0 or user_message.lower().count('ligm4') > 0:
            await message.channel.send(ligma())
            return

        elif user_message.lower().count('limerick') > 0 or user_message.lower().count('limrick') > 0:
            await message.channel.send(limerick())
            return

        elif user_message.lower().count('prost!') > 0:
            await message.channel.send('https://tenor.com/view/prost-christoph-waltz-django-bier-zum-wohle-gif-11041516')
            return

        elif user_message.lower() == 'fortune':
            await message.channel.send(fortune())
            return

        elif user_message.lower().count('chuck') > 0:
            await message.channel.send(np.random.choice(chuck))
            return

        elif user_message.lower().count('lulzbot tell me about yourself') > 0:
            await message.channel.send(\
'In west Philadelphia born and raised\n\
On the playground was where I spent most of my days')
            time.sleep(4.6)
            await message.channel.send('\
Chillin\' out maxin\' relaxin\' all cool\n\
And all shooting some b-ball outside of the school')
            time.sleep(4.6)
            await message.channel.send('\
When a couple of guys who were up to no good\n\
Started making trouble in my neighborhood')
            time.sleep(4.6)
            await message.channel.send('\
I got in one little fight and my mom got scared\n\
She said, "You\'re movin\' with your auntie and uncle in Bel-Air"')
            time.sleep(5)
            await message.channel.send('\
I begged and pleaded with her day after day\n\
But she packed my suitcase and sent me on my way')
            time.sleep(4.6)
            await message.channel.send('\
She gave me a kiss and then she gave me my ticket\n\
I put my Walkman on and said\n\
"I might as well kick it"')
            time.sleep(4.5)
            await message.channel.send('\
First class, yo, this is bad\n\
Drinking orange juice out of a champagne glass')
            time.sleep(4.5)
            await message.channel.send('\
Is this what the people of Bel-Air living like?\n\
Hmm, this might be alright')
            time.sleep(4.5)
            await message.channel.send('\
I whistled for a cab and when it came near\n\
The license plate said "Fresh" and it had dice in the mirror')
            time.sleep(4.5)
            await message.channel.send('\
If anything I could say that this cab was rare\n\
But I thought, "Nah, forget it"\n\
– "Yo, homes to Bel-Air"')
            time.sleep(4.5)
            await message.channel.send('\
I')
            time.sleep(.5)
            await message.channel.send('\
pulled')
            time.sleep(.5)
            await message.channel.send('\
up to the house about 7 or 8\n\
And I yelled to the cabbie\n\
"Yo homes smell ya later"')
            time.sleep(4.5)
            await message.channel.send('\
I looked at my kingdom\n\
I was finally there\n\
To sit on my throne as the Prince of Bel-Air')
            return

client.run(TOKEN)
