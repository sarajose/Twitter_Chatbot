# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 04:49:47 2021

@author: Sara
"""
import nltk
import pickle
import numpy as np
from keras.models import load_model
import json
from test_utils import predict_class

#Load model from relative path
model = load_model('applemodel')


#Load files words, docs, X_train, y_train
q_and_a = json.loads(open('Data/text_apple.json').read())
words = pickle.load(open('Data/words.pkl','rb'))
docs = pickle.load(open('Data/docs.pkl','rb'))

X_train = pickle.load(open('Data/X_train.pkl','rb'))
y_train = pickle.load(open('data/y_train.pkl','rb'))

#User inputs question
input_q = 'How long does it take to fix it'
#Text needs to be cleaned
# Add conditions that make the bot run while they arent met
predictions = predict_class(input_q, X_train, model)
print('Finished')

