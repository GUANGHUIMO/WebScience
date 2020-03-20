# -*- coding: utf-8 -*-
import tweepy
import pymongo
import json
import _thread
import time

consumer_key = "Y345zWLi2FF8xDttedm4vdbL7"
consumer_secret = "QL08ZIt8O8PHda0IwjVSRtqxPBBYTHcXF6LY69ERejw1O9jesH"
access_token = "1220426840009052160-OffUEh7etAIzu8pkbVbrpEp0fa09ne"
access_token_secret = "ucvBZoiEScoIG5f4J17V7mhOpxjkRCJ93Apzd7h3xH1DI"
# setting API
auth =tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

def thread1():
    
    myclient = pymongo.MongoClient('localhost',27017) # create an instance of mongoclient fot communicating with database
    mydb = myclient['TwitterData'] # create a database named TwitterData
                   
    class StdOutListener(tweepy.streaming.StreamListener):
    
        def on_data(self, data):
            mydb['ExcitementClass'].insert_one(json.loads(data))#create a collection named Excitement
            # insert_one() method used to put the data into collections
            # json.loads（）decode json type into python, from object to dict
            print("Data loaded in Collection 1.")
            
        def on_error(self, status):
            print("Data loading failed in Collection 1:",status)

    listener1 = StdOutListener()  
    stream1 = tweepy.Stream(auth, listener1,tweet_mode='extended')
    stream1.filter(languages=["en"],track=['#excitement','#exciting','#excited','#enlighten','#fines','#interesting','#appealing','#adventure','#expected','#believing','#anticipating','#expectation','#unveiling','#ambition','#eager']) # the track parameter is an array of search terms to stream.

def thread2():
    
    myclient = pymongo.MongoClient('localhost',27017)
    mydb = myclient['TwitterData']

    class StdOutListener(tweepy.streaming.StreamListener):

        def on_data(self, data):
            mydb['HappyClass'].insert_one(json.loads(data))
            print("Data loaded in Collection 2.")

        def on_error(self, status):
            print("Data loading failed in Collection 2:",status)

    listener2 = StdOutListener()
    stream2 = tweepy.Stream(auth, listener2,tweet_mode='extended')
    stream2.filter(languages=["en"],track=['#happy','#joy','#love'])


def thread3():
    myclient = pymongo.MongoClient('localhost', 27017)
    mydb = myclient['TwitterData']

    class StdOutListener(tweepy.streaming.StreamListener):

        def on_data(self, data):
            mydb['PleasantClass'].insert_one(json.loads(data))
            print("Data loaded in Collection 3.")

        def on_error(self, status):
            print("Data loading failed in Collection 3:", status)

    listener3 = StdOutListener()
    stream3 = tweepy.Stream(auth, listener3)
    stream3.filter(languages=["en"], track=['#pleasant','#admiring','#admiration','#honor','#share','#confidence','#progress','#valued','#like','#admire','#samelove'])


def thread4():
    myclient = pymongo.MongoClient('localhost', 27017)
    mydb = myclient['TwitterData']

    class StdOutListener(tweepy.streaming.StreamListener):

        def on_data(self, data):
            mydb['SurpriseClass'].insert_one(json.loads(data))
            print("Data loaded in Collection 4.")

        def on_error(self, status):
            print("Data loading failed in Collection 4:", status)

    listener4 = StdOutListener()
    stream4 = tweepy.Stream(auth, listener4)
    stream4.filter(languages=["en"], track=['#surprise', '#sad', '#frustration','#noisy','#upset','#annoying','#dismay'])


def thread5():
    myclient = pymongo.MongoClient('localhost', 27017)
    mydb = myclient['TwitterData']

    class StdOutListener(tweepy.streaming.StreamListener):

        def on_data(self, data):
            mydb['FearClass'].insert_one(json.loads(data))
            print("Data loaded in Collection 5.")

        def on_error(self, status):
            print("Data loading failed in Collection 5:", status)

    listener5 = StdOutListener()
    stream5 = tweepy.Stream(auth, listener5)
    stream5.filter(languages=["en"], track=['#fear', '#disgust', '#depression','#angst','#despair','#horror','#antipathy','#distaste'])


def thread6():
    myclient = pymongo.MongoClient('localhost', 27017)
    mydb = myclient['TwitterData']

    class StdOutListener(tweepy.streaming.StreamListener):

        def on_data(self, data):
            mydb['AngryClass'].insert_one(json.loads(data))
            print("Data loaded in Collection 6.")

        def on_error(self, status):
            print("Data loading failed in Collection 6:", status)

    listener6 = StdOutListener()
    stream6 = tweepy.Stream(auth, listener6)
    stream6.filter(languages=["en"], track=['#ireful','#offended','#mad','#angry','#furious','#exasperated','#sullen','#resentful',
                                            '#fuckedoff',"#veryangry",'#hate','#damn','#agitated','#fury','#roar','#temper'])
    
if __name__ == "__main__":
       
    # _thread.start_new_thread(thread1,())
    # _thread.start_new_thread(thread3, ())
    # _thread.start_new_thread(thread4, ())
    _thread.start_new_thread(thread5, ())
    # _thread.start_new_thread(thread6, ())
    time.sleep(5000)