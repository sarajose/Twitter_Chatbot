# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 03:15:43 2021
@author: sara-

Description: Shallow Neural Network model with 3 layers, adam optimizer,
softmax activation function and L2 regularization.
"""

import pickle
import numpy as np
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD

from tensorflow.keras import layers, regularizers

class snn_model:
    
        def __init__(self, train_x, train_y, filename):
            self.train_x = train_x 
            self.train_y = train_y
            self.filename = filename + '.h5'
        
        def create_and_save(self, train_x, train_y, filename):
              
            # Create a shallow NN model - 3 layers: 128, 64 and the num of neuronsof the num of intents
            
            model = Sequential()
            model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu', kernel_regularizer=regularizers.l2(l=0.1)))
            model.add(Dropout(0.2))
            model.add(Dense(64, activation='relu', kernel_regularizer=keras.regularizers.l2(l=0.1)))
            model.add(Dropout(0.1))
            model.add(Dense(len(train_y[0]), activation='softmax'))
            
            # Compile model. With cross-entropy and adam optimizer/ Stochastic gradient descent
            #sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9)
            opt_adam = keras.optimizers.Adam(clipnorm=1, learning_rate=0.0001)
            model.compile(loss='categorical_crossentropy', optimizer=opt_adam)
            
            #Fitting and saving the model 
            h_fit = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1) 
            
            model.save(filename, h_fit)
            print("Model sucesfully saved")
