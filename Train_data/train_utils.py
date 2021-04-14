# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 02:49:23 2021
@author: sara-

"""
import numpy as np
import re
import nltk
import heapq 
# To be downloaded only once
# nltk.download('stopwords') 
# nltk.download('wordnet')
# nltk.download('punkt')

# Tokenize words
def tokenize(text):
    return nltk.word_tokenize(text)
    
#Stemming
st = nltk.PorterStemmer()
def stem(word):
    return st.stem(word.lower())

# Remove stopwords
stopwords = nltk.corpus.stopwords.words('english') 

def remove_stopwords(tokenized_list):
    wh_stopwords = [word for word in tokenized_list if word not in stopwords]
    return wh_stopwords

# Lemmatize words (similar to stemming but in a more dictionary way approach)
lem = nltk.WordNetLemmatizer()

def lemmatizing(tokenized_text):
    text = [lem.lemmatize(word) for word in tokenized_text]
    return text

#Word frequency of a text
def word_frequency(words):
    word_freq = {}
    for word in words:
        if word not in word_freq.keys():
            word_freq[word] = 1
        else:
            word_freq[word] += 1                
    most_freq = heapq.nlargest(130, word_freq, key=word_freq.get)
    return most_freq
    
def bag_of_words(tokenized_sentence, words):
    sentence_words = [stem(word) for word in tokenized_sentence]
    bag = np.zeros(len(words), dtype=np.float64)
    for i, w in enumerate(words):
        if w in sentence_words: 
            bag[i] = 1
    return bag
    
    