# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 04:49:47 2021
@author: Sara
Description: bot program, uploads the saved model makes predictions and outputs results
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
input_q = 'None'
bot = "Apple bot"

print(f"\nSupport bot\n{bot}: Hi, ask me your question (type 'exit' to quit)")
while input_q != 'exit':
    input_q = input("You: ")   
    if check_language(input_q):
            tok_q = tokenize(input_q)
            tok_q = check_spelling(str(tok_q))
            
    predictions = predict_class(tok_q, X_train, a_model)
    result= 'None'
    tag = predictions
    for item in docs:
            #item[0]: ids item[2]: answers
            if(item[0]== tag):
                result = item[2]
         
    if result == 'None' and input_q != 'exit': print(f"{bot}: I do not understand...")
    elif input_q == 'exit': print(f"{bot}: Thanks, Good bye!")
    else:  print(f"{bot}: {result}")
