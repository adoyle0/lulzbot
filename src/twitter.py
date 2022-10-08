import tweepy

twit_sekrit = open('.sekrit/twit_sekrit').read().split('\n')
api_key = twit_sekrit[0]
api_key_secret = twit_sekrit[1]
bearer_token = twit_sekrit[2]
access_token = twit_sekrit[3]
access_token_secret = twit_sekrit[4]
tclient = tweepy.Client(bearer_token,api_key,api_key_secret,access_token,access_token_secret)

def get_tweet(user_id):
    return tclient.get_users_tweets(user_id, exclude=['replies'], max_results=5)[0][0]
