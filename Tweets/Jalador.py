import tweepy
from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import pymongo
from pymongo import MongoClient

import twitter_credentials
import numpy as np
import pandas as pd
client = pymongo.MongoClient('mongodb://admin:eduardo@redalert-shard-00-00-v3xd5.mongodb.net:27017,redalert-shard-00-01-v3xd5.mongodb.net:27017,redalert-shard-00-02-v3xd5.mongodb.net:27017/test?ssl=true&replicaSet=RedAlert-shard-0&authSource=admin&retryWrites=true&w=majority')
db = client['RedAlet']
collection = db['Tweets']




class StdOutListener(StreamListener):

    print("Waiting")

    def on_status(self, status):
        print(status.id)
        print(status.text)
        print(status.created_at)
        print(status.in_reply_to_status_id)
        post = {'id':status.id,'text':status.text,'date':status.created_at,"is_replay":status.in_reply_to_status_id}
        if status.retweeted:
            return
        posts = db.Jalisco911
        post_id = posts.insert_one(post).inserted_id



    def on_error(self, status_code):
        if status_code == 420:
            return False

if __name__ == "__main__":



    l =StdOutListener()

    auth = OAuthHandler(twitter_credentials.CONSUMER_KEY,twitter_credentials.CONSUMER_SECRET)
    auth.set_access_token(twitter_credentials.ACCESS_TOKEN,twitter_credentials.ACCESS_TOKEN_SECRET)

    print("Inicio")
    stream = Stream(auth, l)
    stream.filter(follow=['4501789032'])
    #stream.filter(follow=['2262123079'])
