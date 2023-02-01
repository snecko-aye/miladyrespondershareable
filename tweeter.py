from constants import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET
import tweepy
from twython import Twython

client = tweepy.Client(
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET,
    wait_on_rate_limit=True
)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True)

twython = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

RESPONDER_ID = 1582399201148915712

def check_user_follows(user_id):
    status = api.get_friendship(source_id=user_id,target_id=RESPONDER_ID)
    follows = status[0].following
    return follows

def tweet_custom(text, id): 
    status = twython.show_status(id=id)
    user_id = status['user']['id']
    screen_name = status['user']['screen_name']
    user_follows = check_user_follows(user_id)
    if user_id != RESPONDER_ID and user_follows:
        print(f'{screen_name}, {screen_name} follows {user_follows}')
        client.create_tweet(text=text, in_reply_to_tweet_id=id)
        client.like(tweet_id=id)
    
def tweet(text, id): 
    status = twython.show_status(id=id)
    user_id = status['user']['id']
    screen_name = status['user']['screen_name']
    user_follows = check_user_follows(user_id)
    if user_id != RESPONDER_ID and user_follows:
        print(f'{screen_name}, {screen_name} follows {user_follows}')
        if text == '420':
            media = api.media_upload(f'memes/miladyblunt.jpeg')
            client.create_tweet(text='BLAZE IT', media_ids=[media.media_id], in_reply_to_tweet_id=id)
        else:
            client.create_tweet(text=text, in_reply_to_tweet_id=id)
        client.like(tweet_id=id)