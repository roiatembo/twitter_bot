import tweepy
from fun import *

twitter = tweepy.Client(BEARER_TOKEN, CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET)

tweet = "I don't know whether its just me but, there is something about coding in the middle of the night, #pythondeveloper"

# twitter.create_tweet(text=tweet)