# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 05:11:36 2021

@author: Sara
"""
import nltk
import pickle
import numpy as np
from keras.models import load_model

ERR_THRESHOLD = 0.3

#Make a prediction
def predict_class(sentence, X_train, model):
    # Bag of words in X_train
    result = model.predict(np.array(X_train))[0]
    results = [[i,r] for i,r in enumerate(result) if r>ERR_THRESHOLD]
    # sort by higher probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"Ids": str[r[0]], "Probability": str(r[1])})
    return return_list
