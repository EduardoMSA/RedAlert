import tweepy
from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import twitter_credentials
import numpy as np
import pandas as pd

class StdOutListener(StreamListener, file):
    print("Waiting")

    def on_status(self, status):
        print(status.id)
        print(status.text)
        datos = status.id + "," + status.text
        print(datos)
        if status.retweeted:
            return

        file.write(datos)
        file.write('/n')




    def on_error(self, status_code):
        if status_code == 420:
            return False

if __name__ == "__main__":


    saveFile = open('911.csv', 'w+')

    l =StdOutListener(StreamListener,saveFile)

    auth = OAuthHandler(twitter_credentials.CONSUMER_KEY,twitter_credentials.CONSUMER_SECRET)
    auth.set_access_token(twitter_credentials.ACCESS_TOKEN,twitter_credentials.ACCESS_TOKEN_SECRET)

    print("Inicio")
    stream = Stream(auth, l)
    #stream.filter(follow=['4501789032'])
    stream.filter(follow=['2262123079'])

    close(saveFile)







    #print(tweets[0].id)
    #print(tweets[0].retweet_count)


    #df.to_json('ejemplo.json')
