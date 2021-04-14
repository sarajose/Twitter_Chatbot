# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 03:51:48 2021
@author: sara-

Description: preprocess for the apple dataset only. 
"""
import json
import pickle
from train_utils import tokenize, remove_stopwords, lemmatizing
from preprocess_utils import check_spelling, check_language

# Load json file and saved it as a nested dictonary
with open('Data/text_apple.json', 'r') as f:
    q_and_a = json.load(f)

# Preprocess trainining data
words = []
docs = []
ids = 0
str_id = '0' 

#Tokenized questions
for question in q_and_a:
    #Only 200 entries are taken to reduce the computing time to create the bag of words and train the model
    while ids < 200:
        print(ids)
        if(check_language(q_and_a[str_id]['text_x'])):
            tok_q = tokenize(q_and_a[str_id]['text_x'])
            tok_q = check_spelling(tok_q)
            words.extend(tok_q)
            docs.append((str_id, tok_q, q_and_a[str_id]['text_y']))
        ids+= 1
        str_id = str(ids)
            
#Ignore words (stopwords)
# It will be lemmatized in train_model.py when the bag of words is created
ignore_words = remove_stopwords(words)

# Use a set to remove duplicates
words = set(words)
words = list(words)

pickle.dump(words,open('Data/split_words.pkl','wb'))
pickle.dump(docs,open('Data/split_docs.pkl','wb'))