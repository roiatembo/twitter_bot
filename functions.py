import tweepy
from fun import *

twitter = tweepy.Client(BEARER_TOKEN, CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET)
class SendTweet():
    def post_status(self, tweet):
        twitter.create_tweet(text=tweet)