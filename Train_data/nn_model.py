# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 03:08:53 2021
@author: sara-

Description: This train model is not used used to train the model. 
It is for a better understanding of what is happening inside of a shallow NN as the one used in snn_model.py file
It creates a shallow neural network with with 2 intput features and 3 classes
2 dense layers and a forward pass only using python without any external library.
"""
import numpy as np

# Dense layer object
class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

#Activation functions
class Activation_ReLU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)
        
class Activation_Softmax:
    def forward(self, inputs):
        exp_values = np.exp(inputs- np.max(inputs, axis=1, keepdims=True))
        probalilites = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        self.output = probalilites

# 2 features, 3 neurons
dense1 = Layer_Dense(2, 3)
activation1 = Activation_ReLU()

#Last output num of classes
dense2 = Layer_Dense(3, 3)
activation2 = Activation_Softmax()
