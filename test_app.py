# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 15:12:06 2021

@author: shrin
"""
import requests
import json
host = "http://localhost:9000"

print(host)
with open('candidates.json') as f:
    data = json.load(f)

request = {'candidate_info':data}

## Testing predict() method
print("****Testing predict() method****")
r = requests.post(f"{host}/predict", json=request)
print(r.text)

print("****Testing predict_proba() method****")
r = requests.post(f"{host}/predict_proba", json=request)
print(r.text)
