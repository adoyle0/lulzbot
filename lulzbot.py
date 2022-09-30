l1gmab0t ='                             \n\
 _          _         ____   ___  _     \n\
| |   _   _| |    ___| __ ) / _ \| |_   \n\
| |  | | | | |   |_  /  _ \| | | | __|  \n\
| |__| |_| | |___ / /| |_) | |_| | |_   \n\
|_____\__,_|_____/___|____/ \___/ \__|  \n\
'
# Discord Bot
import discord
import datetime
import time
from fortune import fortune

TOKEN = open('discord_token').read()
chuck = open('chucknorris').read().split('\n%\n')
client = discord.Client(activity=discord.Game(name='with myself'))

# NLP
import numpy as np
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import asyncio

tokenizer = AutoTokenizer.from_pretrained('microsoft/DialoGPT-large')
model = AutoModelForCausalLM.from_pretrained('../southpark/output-small')

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

ligma = [
    'https://tenor.com/view/ligma-ligma-balls-atomicrops-gif-24996966',
    'https://tenor.com/view/ligma-balls-gif-12236083',
    'https://tenor.com/view/will-smith-ligma-funny-gif-25108308',
    'https://tenor.com/view/racoon-wiggle-nuts-balls-gif-8085185',
    'https://tenor.com/view/jesus-biglebowski-balls-gif-9633055',
    'https://tenor.com/view/big-black-fuzzy-balls-fuzzy-balls-big-balls-eddie-griffin-undercover-brother-gif-5548455',
    'https://tenor.com/view/ballcrushing-bust-ballbusting-balls-gif-14635943',
    'https://tenor.com/view/cup-check-balls-ouch-sack-gif-10728090',
    'https://tenor.com/view/xie-lian-ligma-balls-ligma-tgcf-tian-gua-ci-fu-gif-21869659',
    'https://tenor.com/view/lick-taste-tongue-out-gif-16957327',
    'https://tenor.com/view/rickandmorty-lick-lickballs-gif-9913722',
    'https://tenor.com/view/ligma-balls-gif-12236636',
    'https://tenor.com/view/ligma-balls-gif-22082587',
    'https://tenor.com/view/its-all-free-free-no-charge-free-of-charge-naughty-teddy-gif-19338184',
    'https://tenor.com/view/ligma-balls-sonic-act-lick-gif-21274274',
    'https://tenor.com/view/balls-dance-rotate-beating-gif-17433105',
    'https://tenor.com/view/david-bowie-labyrinth-balls-magic-balls-magic-gif-16043363',
    'https://tenor.com/view/kawaii-muski-muski-omori-ligma-balls-gif-21138025',
    'https://tenor.com/view/ligma-ligamab-alls-tower-of-babel-gaming-tobg-riamu-yumemi-gif-24359574',
    'https://tenor.com/view/goat-lick-tongue-tongue-out-tongue-wiggle-gif-16390888',
    'https://tenor.com/view/bleh-tongue-out-lickitung-pokemon-detective-pikachu-gif-15798020',
    'https://tenor.com/view/deez-nuts-wheel-of-fortune-gif-15264920',
    'https://tenor.com/view/hello-chat-deez-nuts-hello-chat-deez-nuts-gif-25294032',
    'https://tenor.com/view/deez-nuts-troll-troll-face-troll-face-smile-dark-gif-23624288',
    'https://tenor.com/view/deez-nuts-gif-22383209',
    'https://tenor.com/view/deez-nutz-deez-nuts-deez-nutz-heart-locket-gif-22497345',
    'https://tenor.com/view/ball-inspection-balls-inspection-football-bobux-gif-19234883',
    'https://tenor.com/view/sesame-street-proud-hug-puppet-yay-gif-19663674',
    'https://tenor.com/view/deez-deez-nuts-initial-d-ligma-steve-jobs-gif-23065842',
    'https://tenor.com/view/testing-new-deez-nuts-ha-teeth-gif-15758045',
    'https://tenor.com/view/longest-drive-gif-20862347',
    'https://tenor.com/view/deez-deez-nuts-discord-gif-20296574',
    'https://tenor.com/view/these-nuts-deez-gif-13388028',
    'https://tenor.com/view/pepe-deez-nuts-pepe-the-frog-pepe-holding-sign-deez-nuts-gif-deez-nuts-ha-gif-22618462',
    'https://tenor.com/view/squirrel-i-have-got-words-for-you-you-want-deez-nuts-gif-15404415',
    'https://tenor.com/view/deez-nuts-are-you-ready-gif-20161550',
    'https://tenor.com/view/deez-nuts-nutz-deez-gif-18259525',
    'https://tenor.com/view/dee-gif-4387670',
    'https://tenor.com/view/omori-deez-nuts-so-funny-funny-joke-right-guys-gif-21468920',
    'https://tenor.com/view/deeznuts-gif-5578640',
    'https://tenor.com/view/dznutz-gif-7146897',
    'https://tenor.com/view/deez-nut-deez-nuts-gobble-gobble-deez-nuts-gif-25294130',
    'https://tenor.com/view/deez-nuts-gif-22383209',
    'https://tenor.com/view/guilty-gear-strive-happy-chaos-deez-nuts-gif-guilty-gear-gif-23786775',
    'https://tenor.com/view/mouth-full-my-nuts-squirrel-mine-get-away-gif-14154065',
    'https://tenor.com/view/friday-night-funkin-deez-nuts-hop-on-gif-22197266',
    'https://tenor.com/view/deez-nuts-cookie-deez-nutz-deez-nuts-nft-gif-23901553',
    'https://tenor.com/view/homare-arisugawa-a3-deez-nuts-gif-22718748',
    'https://tenor.com/view/cope-deez-cope-on-deez-colossalcraft-coping-gif-23556695',
    'https://tenor.com/view/hug-kiss-gif-23992029',
    'https://tenor.com/view/deez-nutz-deez-nuts-gif-22037745',
    'https://tenor.com/view/deez-nuts-nft-deez-nuts-gif-deez-nuts-deez-big-nuts-deez-gif-23605637',
    'https://tenor.com/view/deez-deez-nuts-gif-25652186',
    'https://tenor.com/view/gulpin-deeznuts-gif-21798060',
    'https://tenor.com/view/deez-nuts-deez-burger-king-burger-king-crown-airplane-gif-21978215',
    'https://tenor.com/view/deez-nuts-rap-john-oh-you-really-like-deez-nut-up-in-your-face-gif-22744730',
    'https://tenor.com/view/hop-on-deez-nuts-gif-25437799',
    'https://tenor.com/view/h3-h3podcast-5percent-five-percent-h3five-percent-gif-24149085',
    'https://tenor.com/view/youre-sucking-deez-nuts-gif-21505910',
    'https://tenor.com/view/eokel-valorant-youtube-gif-22895296',
    'https://tenor.com/view/fortune-cooke-deez-nuts-lmao-cookie-fortune-gif-21740031',
    'https://tenor.com/view/deez-nuts-takemichi-feet-gif-22705365',
    'https://tenor.com/view/deez-nuts-dana-gif-19615763',
    'https://tenor.com/view/smg4-gif-23834017',
    'https://tenor.com/view/urmom-hololive-gif-21993936',
    'https://tenor.com/view/deez-nuts-paradise-pd-crabbage-gif-21925327',
    'https://tenor.com/view/willem-dafoe-insane-insanity-crazy-nuts-gif-20731647',
    'https://tenor.com/view/yogi-bear-yogi-bear-doughnuts-deez-nuts-gif-gif-23782410',
    'https://tenor.com/view/dane-cook-carpe-deez-nuts-floyd-waiting-gif-17393528',
    'https://tenor.com/view/what-are-you-putting-on-your-wiener-what-is-on-your-wiener-what-do-you-put-on-your-wiener-on-your-wiener-your-wiener-gif-18064519',
    'https://tenor.com/view/king-kong-deez-nuts-meme-kong-king-gif-21432884',
    'https://tenor.com/view/bangbang-gun-shot-powpow-pow-gif-21746849',
    'https://tenor.com/view/mcdonalds-meme-gif-mickey-deez-gif-9926547',
    'https://tenor.com/view/deez-nuts-spongebob-gif-5267436',
    'https://tenor.com/view/hangover-nuts-chow-ken-jeong-the-hangover-gif-13028372',
    'https://tenor.com/view/snl-natalie-portman-jiggle-nuts-lonely-gif-15048024',
    'https://tenor.com/view/omegalul-deez-deez-nuts-twitch-clips-gif-22601733',
    'https://tenor.com/view/you-ready-deez-nuts-gif-18188433',
    'https://media.giphy.com/media/jt3R5veCXNM1jJ183A/giphy-downsized-large.gif',
]

limericks = [
    'Limericks I cannot compose,\n\
    With noxious smells in my nose.\n\
    But this one was easy,\n\
    I only felt queasy,\n\
    Because I was sniffing my toes.',
\
    'There was a young woman named Bright,\n\
    Whose speed was much faster than light.\n\
    She set out one day,\n\
    In a relative way,\n\
    And returned on the previous night.',
\
    'There was an odd fellow named Gus,\n\
    When traveling he made such a fuss.\n\
    He was banned from the train,\n\
    Not allowed on a plane,\n\
    And now travels only by bus.',
\
    'There once was a fly on the wall,\n\
    I wonder, why didn’t it fall?\n\
    Because its feet stuck? Or was it just luck?\n\
    Or does gravity miss things so small?',
\
    'There once was a man from Tibet,\n\
    Who couldn’t find a cigarette\n\
    So he smoked all his socks,\n\
    and got chicken-pox,\n\
    and had to go to the vet.',
\
    'There was a young woman named Bright,\n\
    Whose speed was much faster than light.\n\
    She set out one day,\n\
    In a relative way,\n\
    And returned on the previous night.',
\
    'I need a front door for my hall,\n\
    The replacement I bought was too tall.\n\
    So I hacked it and chopped it,\n\
    And carefully lopped it,\n\
    And now the dumb thing is too small',
\
    'There once was a boy named Dan,\n\
    who wanted to fry in a pan.\n\
    He tried and he tried,\n\
    and eventually died,\n\
    that weird little boy named Dan.',
\
    'A newspaperman named Fling,\n\
    Could make “copy” from any old thing.\n\
    But the copy he wrote,\n\
    Of a five-dollar note,\n\
    Was so good he now wears so much bling.',
\
    'I know an old owl named Boo,\n\
    Every night he yelled Hoo,\n\
    Once a kid walked by,\n\
    And started to cry,\n\
    And yelled I don’t have a clue!',
\
    'I once fell in love with a blonde,\n\
    But found that she wasn’t so fond.\n\
    Of my pet turtle named Odle,\n\
    whom I’d taught how to Yodel,\n\
    So she dumped him outside in the pond.',
\
    'I’d rather have Fingers than Toes,\n\
    I’d rather have Ears than a Nose.\n\
    And as for my Hair,\n\
    I’m glad it’s all there,\n\
    I’ll be awfully sad, when it goes.',
\
    'There was a Young Lady whose chin\n\
    Resembled the point of a pin:\n\
    So she had it made sharp,\n\
    And purchased a harp,\n\
    And played several tunes with her chin. (Edward Lear)',
\
    'Hickory Dickory dock,\n\
    the mouse ran up the clock;\n\
    the clock struck one\n\
    and down he run;\n\
    hickory Dickory dock. (Charles Perrault)',
\
    'There was a faith-healer of Deal,\n\
    Who said: “Although pain isn’t real,\n\
    If I sit on a pin\n\
    And it punctures my skin,\n\
    I dislike what I fancy I feel.',
\
    'My dog is really quite hip,\n\
    Except when he takes a cold dip.\n\
    He looks like a fool,\n\
    when he jumps in the pool,\n\
    and reminds me of a sinking ship.',
\
    'A painter, who lived in Great Britain,\n\
    Interrupted two girls with their knitting,\n\
    He said, with a sigh,\n\
    That park bench–well I,\n\
    Just painted it, right where you’re sitting.',
\
    'There is a young schoolboy named Mason,\n\
    Whose mom cuts his hair with a basin.\n\
    When he stands in one place,\n\
    With a scarf round his face,\n\
    It’s a mystery which way he’s facing.',
\
    'There was a young schoolboy of Rye,\n\
    Who was baked by mistake in a pie.\n\
    To his mother’s disgust,\n\
    He emerged through the crust,\n\
    And exclaimed, with a yawn, Where am I?',
\
    'An elderly man called Keith,\n\
    Mislaid his set of false teeth.\n\
    They’d been laid on a chair,\n\
    He’d forgot they were there,\n\
    Sat down, and was bitten beneath.',
\
    'There was an old man of Peru,\n\
    Who dreamt he was eating his shoe.\n\
    He woke in the night,\n\
    With a terrible fright,\n\
    And found it was perfectly true.',
\
    'The incredible Wizard of Oz,\n\
    Retired from his business becoz.\n\
    Due to up-to-date science,\n\
    To most of his clients,\n\
    He wasn’t the Wizard he woz.',
\
    'Once I visited France,\n\
    And learned a new, awesome dance.\n\
    I twirled,\n\
    And I swirled,\n\
    And Is it me or the nature of money,\n\
    That’s odd and particularly funny.\n\
    But when I have dough,\n\
    It goes quickly, you know,\n\
    And seeps out of my pockets like honey.\n\
    I lost my pants.',
\
    'Is it me or the nature of money,\n\
    That’s odd and particularly funny.\n\
    But when I have dough,\n\
    It goes quickly, you know,\n\
    And seeps out of my pockets like honey.',
\
    'There once was a farmer from Leeds,\n\
    Who swallowed a packet of seeds.\n\
    It soon came to pass,\n\
    He was covered with grass,\n\
    But has all the tomatoes he needs.',
\
    'A fellow jumped off a high wall,\n\
    And had a most terrible fall.\n\
    He went back to bed,\n\
    With a bump on his head,\n\
    That’s why you don’t jump off a wall.',
\
    'A man and his lady-love, Min,\n\
    Skated out where the ice was quite thin.\n\
    Had a quarrel, no doubt,\n\
    For I hear they fell out,\n\
    What a blessing they didn’t fall in!',
\
    'There was a young lady of Cork,\n\
    Whose Pa made a fortune in pork.\n\
    He bought for his daughter,\n\
    A tutor who taught her,\n\
    To balance green peas on her fork.',
\
    'There once was a Martian called Zed\n\
    With antennae all over his head.\n\
    He sent out a lot\n\
    Di-di-dash-di-dot\n\
    But nobody knew what he said!',
\
    'There once was a girl named Sam\n\
    Who did not eat roast beef and ham\n\
    She ate a green apple\n\
    Then drank some Snapple\n\
    Some say she eats like a lamb.',
\
    'Said the man with a wink of his eye\n\
    ‘But I love you‘ and then the reply\n\
    From the girl, it was heard\n\
    ‘You are truly absurd!\n\
    I have only this moment walked by!’',
\
    'A wonderful bird is the Pelican.\n\
    His beak can hold more than his belly can.\n\
    He can hold in his beak\n\
    Enough food for a week!\n\
    But I’ll be darned if I know how the hellican?',
\
    'There was once a great man in Japan\n\
    Whose name on Tuesday began,\n\
    It lasted through Sunday\n\
    Till twilight on Monday\n\
    And it sounded like stones in a can.',
\
    'There was a young man so benighted\n\
    He never knew when he was slighted;\n\
    He would go to a party\n\
    And eat just as hearty,\n\
    As if he’d been really invited.',
\
    'There was an old man from Sudan,\n\
    Whose limericks never would scan.\n\
    When told this was so,\n\
    He said, ‘yes, I know.\n\
    ‘But I always try to get as many syllables into the last line as I possibly can.’',
\
    'A maiden at college, Miss Breeze,\n\
    Weighed down by B.A.s and Lit.D’s,\n\
    Collapsed from the strain,\n\
    Said her doctor, “It’s plain\n\
    You are killing yourself—by degrees!”',
\
    'A canner, exceedingly canny,\n\
    One morning remarked to his granny,\n\
    “A canner can can\n\
    Anything that he can;\n\
    But a canner can’t can a can, can he?”',
\
    'A mouse in her room woke Miss Dowd\n\
    She was frightened—it must be allowed.\n\
    Soon a happy thought hit her—\n\
    To scare off the critter,\n\
    She sat up in bed and meowed.',
\
    'There was a young woman named Kite,\n\
    Whose speed was much faster than light,\n\
    She set out one day,\n\
    In a relative way,\n\
    And returned on the previous night.',
\
    'A flea and a fly in a flue,\n\
    Were imprisoned, so what could they do?\n\
    Said the fly, “Let us flee!”\n\
    “Let us fly,” said the flea,\n\
    And they flew through a flaw in the flue.',
\
    'A major, with wonderful force,\n\
    Called out in Hyde Park for a horse.\n\
    All the flowers looked round,\n\
    But no horse could be found;\n\
    So he just rhododendron, of course.',
\
    'A nifty young flapper named Jane\n\
    While walking was caught in the rain.\n\
    She ran–almost flew,\n\
    Her complexion did too,\n\
    And she reached home exceedingly plain.',
\
    '“There’s a train at 4:04,” said Miss Jenny.\n\
    “Four tickets I’ll take; have you any?”\n\
    Said the man at the door,\n\
    “Not four for 4:04,\n\
    For four for 4:04 is too many.”',
\
    'A canny young fisher named Fisher\n\
    Once fished from the edge of a fissure.\n\
    A fish with a grin\n\
    Pulled the fisherman in—\n\
    Now they’re fishing the fissure for Fisher.',
\
    'Here’s to the chigger,\n\
    The bug that’s no bigger\n\
    Than the point of an undersized pin;\n\
    But the welt that he raises\n\
    Sure itches like blazes,\n\
    And that’s where the rub comes in!',
\
    'A cheerful old bear at the Zoo\n\
    Could always find something to do.\n\
    When it bored him, you know,\n\
    To walk to and fro,\n\
    He reversed it and walked fro and to.',
\
    'The bottle of perfume that Willie sent\n\
    Was highly displeasing to Millicent;\n\
    Her thanks were so cold\n\
    They quarreled, I’m told,\n\
    Through that silly scent Willie sent Millicent.',
\
    'I bought a new Hoover today,\n\
    Plugged it in in the usual way,\n\
    Switched it on – what a din;\n\
    It sucked everything in,\n\
    Now I’m homeless with no place to stay.',
\
    'A crossword compiler named Moss\n\
    Who found himself quite at a loss\n\
    When asked, ‘Why so blue?’\n\
    Said, ‘I haven’t a clue\n\
    I’m 2 Down to put 1 Across.’',
\
    'I’m papering walls in the loo\n\
    And quite frankly I haven’t a clue;\n\
    For the pattern’s all wrong\n\
    (Or the paper’s too long)\n\
    And I’m stuck to the toilet with glue.',
\
    'There once was an old man of Esser,\n\
    Whose knowledge grew lesser and lesser,\n\
    It at last grew so small\n\
    He knew nothing at all\n\
    And now he’s a college professor.',
\
    'To compose a sonata today,\n\
    Don’t proceed in the old-fashioned way:\n\
    With your toes on the keys,\n\
    Bang the floor with your knees:\n\
    “Oh how modern!” the critics will say.',
\
    'There was a young lady named Perkins,\n\
    Who just simply doted on gherkins.\n\
    In spite of advice,\n\
    She ate so much spice,\n\
    That she pickled her internal workins’.',
\
    'There was an old man of Nantucket\n\
    Who kept all his cash in a bucket;\n\
    But his daughter, named Nan\n\
    Ran away with a man —\n\
    And as far as the bucket, Nantucket.',
\
    'There was a young lady of Kent,\n\
    Whose nose was most awfully bent.\n\
    She followed her nose\n\
    One day, I suppose —\n\
    And no one knows which way she went.',
\
    'There was a young lady named Hannah,\n\
    Who slipped on a peel of banana.\n\
    As she lay on her side,\n\
    More stars she espied\n\
    Than there are in the Star-Spangled Banner.',
\
    'There was a dear lady of Eden,\n\
    Who on apples was quite fond of feedin’;\n\
    She gave one to Adam,\n\
    Who said, “Thank you, Madam,”\n\
    And then both skedaddled from Eden.',
\
    'A certain young fellow named Bee-Bee\n\
    Wished to wed a woman named Phoebe.\n\
    “But,” he said, “I must see\n\
    What the clerical fee\n\
    Be before Phoebe be Phoebe Bee-Bee',
\
    'Remember when nearly sixteen\n\
    On your very first date as a teen\n\
    At the movies? If yes,\n\
    Then I bet you can’t guess\n\
    What was shown on the cinema screen.',
\
    'There was an old person of Fratton\n\
    Who would go to church with his hat on.\n\
    ‘If I wake up,’ he said,\n\
    ‘With a hat on my head,\n\
    I will know that it hasn’t been sat on.’',
\
    'My neighbor came over to say\n\
    (Although not in a neighborly way)\n\
    That he’d knock me around\n\
    If I didn’t curb the sound\n\
    Of the classical music I play.',
\
    'I told him, “Get out of my place\n\
    You’re an utter uncultured disgrace;\n\
    You’re a simpleton loon.\n\
    Don’t you know a good tune?”\n\
    Then he walloped me square in the face.',
\
    'There was a young man from Dealing\n\
    Who caught the bus for Ealing.\n\
    It said on the door\n\
    ‘Don’t spit on the floor’\n\
    So he jumped up and spat on the ceiling',
\
    'As 007 walked by\n\
    He heard a wee spider say, “Hi.”\n\
    But shaken, he shot\n\
    It right there on the spot\n\
    As it tried to explain, “I’m a spi …”',
\
    'A tutor who tooted the flute\n\
    Tried to tutor two tooters to toot\n\
    Said the two to the tutor\n\
    “Is it tougher to toot or\n\
    To tutor two tooters to toot?”',
\
    'No woodsman would cut a wood, would he\n\
    If woods would be woodless – nor should he.\n\
    Yet no woodcutter would\n\
    Cut a woody-wood wood\n\
    If no woodsmen cut woody woods, would he?',
\
    'There once was a man from the sticks\n\
    Who loved to compose limericks\n\
    But he failed at his sport\n\
    They were always too short\n\
    Parade Daily\n\
    Celebrity interviews, recipes and health tips delivered to your inbox.',
\
    'A poet whose friends called him Steve\n\
    Once showed quite a will to achieve\n\
    His skill grew so strong\n\
    That his poems grew long\n\
    And he sadly was forced to abbrev.',
\
    'If you catch a chinchilla in Chile\n\
    And cut off its beard, willy-nilly\n\
    You can honestly say\n\
    That you have just made\n\
    A Chilean chinchilla’s chin chilly',
\
    'There once was a man named Muvett\n\
    Who lived in the city of Lovett\n\
    But his car broke down\n\
    Two miles out of town\n\
    And Muvett had to shove it to Lovett!',
\
    'There once was a beautiful nurse\n\
    Who carried an ugly old purse\n\
    But she tripped on the door\n\
    And fell on the floor\n\
    And they both went away in the hearse.',
\
    'There was a young girl from Flynn\n\
    Who was so terribly thin\n\
    When she sipped lemonade\n\
    Through a straw in the shade\n\
    She slipped through the straw and fell in!',
\
    'There once was a man from Gorem\n\
    Had a pair of tight pants and he wore ’em\n\
    When he bowed with a grin\n\
    A draft of air rushed in\n\
    And he knew by the sound that he tore ’em!',
\
    'There once was a man from the city\n\
    Stooped to pat what he thought was a kitty\n\
    He gave it a pat\n\
    But it wasn’t a cat-\n\
    They buried his clothes – what a pity!',
\
    'There once was a gal from Decatur\n\
    Who went to sing in a the-a-ter\n\
    But the poor little thing\n\
    When she started to sing\n\
    Got hit by a rotten termater! (tomato)',
\
    'What happens when you retire?\n\
    You really don’t have to inquire –\n\
    No job and no phone\n\
    There’s no place but home,\n\
    And your checkbook’s about to expire!',
\
    'At times I’m so mad that I’m hopping.\n\
    My angriness sets my veins popping.\n\
    I yell and I curse,\n\
    With swear words diverse,\n\
    But my wife does much worse: she goes shopping',
\
    'One Saturday morning at three,\n\
    A cheese monger’s shop in Paree.\n\
    Collapsed to the ground,\n\
    With a thunderous sound,\n\
    Leaving only a pile of de brie.'
]

# Init
@client.event
async def on_ready():
    print(l1gmab0t+'\n'+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'\nLogged in as {0.user}'.format(client))

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
            await message.channel.send(np.random.choice(ligma))
            return

        elif user_message.lower().count('limerick') > 0 or user_message.lower().count('limrick') > 0:
            await message.channel.send(np.random.choice(limericks))
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
