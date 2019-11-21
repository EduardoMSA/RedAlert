import tweepy
from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import twitter_credentials
import numpy as np
import pandas as pd

class StdOutListener(StreamListener):
    print("Waiting")

    def on_status(self, status):
        print(status.id)
        print(status.text)
        datos = status.id + "," + status.text
        print(datos)
        if status.retweeted:
            return




    def on_error(self, status_code):
        if status_code == 420:
            return False

if __name__ == "__main__":



    l =StdOutListener()

    auth = OAuthHandler(twitter_credentials.CONSUMER_KEY,twitter_credentials.CONSUMER_SECRET)
    auth.set_access_token(twitter_credentials.ACCESS_TOKEN,twitter_credentials.ACCESS_TOKEN_SECRET)

    print("Inicio")
    stream = Stream(auth, l)
    #stream.filter(follow=['4501789032'])
    stream.filter(follow=['2262123079'])





