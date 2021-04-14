# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 02:23:27 2021

@author: Sara
"""
from textblob import TextBlob

def check_spelling(text):
    check = TextBlob(text)         
    return str(check.correct())

def check_language(text):
    check = TextBlob(text) 
    return True if (check.detect_language() == 'en') else False
    #return (check.detect_language() == 'en')
 
