# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 20:59:25 2021
@author: sara-
Concept: Downloads all tweets from specified keywords
Usage: Emptpy variable need to be declared before running the file: 
keys and tokens from Twitter, search keywords, the date period 
and the filename of the csv file.
"""
import tweepy as tw
import csv

#File name
filename = 'Filename.csv'

# App Auth
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

# Search words
search_words = ["MicrosoftHelps", "AmamzonHelps", "AskPayPal"]

found_words = []
date_since = "2016-01-01"

# Open/Create a file to append data
csvFile = open(filename, 'a') 

#Save tweets in csv file
csvWriter = csv.writer(csvFile)

for word in search_words:   
    found_words.append(word)
    for tweet in tw.Cursor(api.search,q= word,count=100,
                               lang="en",
                               since="2016-01-01").items():
        # favorite_count. Number of likes > 15
        for found_word in found_words:
            if tweet.favorite_count > 15:
                print (tweet.id, tweet.in_reply_to_status_id, tweet.created_at, tweet.text)
                csvWriter.writerow([tweet.id, tweet.in_reply_to_status_id, tweet.created_at, tweet.text.encode('utf-8')])
