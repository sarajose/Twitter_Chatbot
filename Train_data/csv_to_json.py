# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 20:39:00 2021
@author: sara-
Description: simple csv to json converter
"""
import csv
import json
import pandas as pd

df_text = pd.read_csv('Data/text_apple.csv')
df_text.to_json (r'Data/text_apple.json')

csvFilePath = r'Data/text_apple.csv'
jsonFilePath = r'Data/text_apple.json'

data = {}
ids = 0
 
#Csv reader
with open(csvFilePath, encoding='utf-8') as csvf:
    csvReader = csv.DictReader(csvf)

    for rows in csvReader:        
        key = ids
        data[key] = rows
        ids +=1
        
 
# Json writer
with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
    jsonf.write(json.dumps(data, indent=4))
    
print("Json saved sucesfully")
     

