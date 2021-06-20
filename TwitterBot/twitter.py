# Replace your key values for <cunsumer_key>, <consumer_secret>, <access_token>, <access_token_secret>
# Invokation: python3 twitter.py


import tweepy
import time

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = api.me()
# print(user.name)
# print(user.screen_name)
# print(user.followers_count)


def limit_handle(cursor):
    '''
    Twitter API has a limit of calls we can make at a timeframe. So handling the error.
    '''
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)  # miliseconds
    except StopIteration:
        return None


# Generous BOt
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
    print(follower.name)
    if(follower.name == 'CloudOYE'):
        follower.follow()


# Like 2 tweets having 'python' in them
search_string = 'python'
numberOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
    try:
        # tweet.retweet()
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
