#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 15:44:34 2021
@author: sara-
Concept: Downloads all tweets from a specified user account
Usage mode: python twitter_data_scraping.py <twitter_user> (without @)

Due to Twitter API limitations it does not dowload more than 3200 tweets.   
"""
import tweepy as tw
import csv
import sys
#import os

def get_tweets(screen_name):
    
    #File name
    filename = screen_name + '.csv'
    #dirname = os.path.dirname(__file__)
    #filename = os.path.join(dirname, '/Data/' + screen_name + '.csv')
    
    # App Auth credentials
    consumer_key = 'XXXXXX'
    consumer_secret = 'XXXXXX'
    access_token = 'XXXXXX'
    access_token_secret = 'XXXXXX'
        
    # Initialize API
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)
    
    # Test authentication
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")
        
    
    #Initial request (200 is the maximum)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    
    #Inititialize list and save tweets
    tweets = []  
    tweets.extend(new_tweets)
    
    # Id of the oldest tweet
    max_id = tweets[-1].id - 1
    
    #Fetch all tweets
    while len(new_tweets) > 0:
        print(f" Getting tweets before {max_id}\n")
        
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id= max_id)
        tweets.extend(new_tweets)
        max_id = tweets[-1].id - 1
        
        print(f"Number of dowloaded tweets: {len(tweets)}")
    
    #Parameters needed:
    #Relevance (tweet has at least 2 likes)
    alltweets = [[tweet.id, tweet.created_at, tweet.text.encode('utf-8'), tweet.in_reply_to_status_id,
                   tweet.in_reply_to_user_id, tweet.in_reply_to_screen_name] 
                 for tweet in tweets if tweet.favorite_count > 3]
    
    #Write all tweets in csv file
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "created_at", "text", "in_reply_to_status_id",
                   "in_reply_to_user_id", "in_reply_to_screen_name"])
        writer.writerows(alltweets)
        
    print ("Done. All tweets have been saved.")


if __name__ == '__main__':
	get_tweets(sys.argv[1])