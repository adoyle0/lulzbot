import numpy as np

def limerick():
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
    return np.random.choice(limericks)
