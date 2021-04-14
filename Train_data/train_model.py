# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 00:04:33 2021

@author: sara-
"""
#Needs tp be revised

import pickle
from train_utils import bag_of_words, word_frequency
import numpy as np
from snn_model import snn_model
import keras

#Unpickle words and classes
#words = pickle.load(open('Data/words.pkl','r'))
#docs = pickle.load(open('Data/docs.pkl','r'))
print("Libreries loaded")

with open('Data/split_words.pkl','rb') as f:
   words = pickle.load(f)

with open('Data/split_docs.pkl','rb') as f:
   docs = pickle.load(f)
   
print("Pickle loaded")   

# Training set
# bag of words per sentence

X_train = []
y_train = []

for (ids, question, answer) in docs:    
    word_freq = word_frequency(words)
    # X: bag of words for each pattern_sentence
    bog = bag_of_words(question, word_freq)
    X_train.append(bog)
    # y: ids
    #label = ids.index(ids)
    num = int(ids)
    y_train.append(num)

X_train = np.array(X_train)
y_train = np.array(y_train).reshape(194,1) #Change to 200 


pickle.dump(X_train,open('Data/X_train.pkl','wb'))
pickle.dump(y_train,open('Data/y_train.pkl','wb'))

print("Done")
# Instantiate model
model = snn_model(X_train, y_train, 'applemodel')
model.create_and_save(X_train, y_train, 'applemodel')

#Load model and train data
#model = keras.models.load_model("model.h5")