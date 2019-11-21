import tweepy
from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import pymongo
from pymongo import MongoClient

import twitter_credentials

import geopy
from geopy import geocoders

client = pymongo.MongoClient('mongodb://admin:eduardo@redalert-shard-00-00-v3xd5.mongodb.net:27017,redalert-shard-00-01-v3xd5.mongodb.net:27017,redalert-shard-00-02-v3xd5.mongodb.net:27017/test?ssl=true&replicaSet=RedAlert-shard-0&authSource=admin&retryWrites=true&w=majority')
db = client['RedAlert']
collection = db['Tweets']
g = geocoders.GoogleV3(api_key='AIzaSyBJmUUp9gyMwgEkD2niujeUZAGClRfsOYc')




class StdOutListener(StreamListener):

    print("Inicio")

    def on_status(self, status):
        if(status.in_reply_to_status_id!=None):
            return
        if status.retweeted:
            returns
        print(status.id)
        txt = status.text
        print(status.created_at)
        print(txt)
        x = txt.split(" en ")
        y = x[1].split(". tome precauciones")
        calle = y[0]
        aType = x[0]
        location = g.geocode(calle, timeout=20)
        #post = {'tweet_id':status.id,'description':status.text,'latitude':location.latitude,'longitude':location.longitude,'date':status.created_at,"title":aType}
        post = {
            'type':'Feature',
            'geometry':{
                'Type':'Point',
                'coordinates':[location.latitude, location.longitude]
            },
            'properties':{
                'id':status.id,
                'description':calle,
                'Latitude':location.latitude,
                'Longitude':location.longitude,
                'date':status.created_at,
                'title':aType
            }

        }
        posts = db.Alertas
        post_id = posts.insert_one(post).inserted_id



    def on_error(self, status_code):
        if status_code == 420:
            return False

if __name__ == "__main__":



    l =StdOutListener()

    auth = OAuthHandler(twitter_credentials.CONSUMER_KEY,twitter_credentials.CONSUMER_SECRET)
    auth.set_access_token(twitter_credentials.ACCESS_TOKEN,twitter_credentials.ACCESS_TOKEN_SECRET)

    stream = Stream(auth, l)

    #JALISCO911
    stream.filter(follow=['4501789032'])
    #stream.filter(follow=['2262123079'])
