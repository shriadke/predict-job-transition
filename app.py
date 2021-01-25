# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 15:06:43 2021

@author: shrin
"""
from flask import Flask, render_template, request, jsonify, abort
import requests
import pickle
import numpy as np
import sklearn
import time
app = Flask(__name__)

# Load the model in app
model = pickle.load(open('model.pkl', 'rb'))

@app.route("/predict", methods=['POST'])
def predict():
    start = time.time()
    
    if not request.json or not 'candidate_info' in request.json:
        print("Bad request")
        abort(400)
        
    # Prepare input data for model
    candidate_info = request.json['candidate_info']
    
    X_test = []
    example_ids = []
    y_test = []
    for exampleID, features in candidate_info.items():
        #print(exampleID,type(features))
        example_ids.append(exampleID)
        y_test.append(features.pop('target'))
        X_test.append([val for val in features.values()])
    
    # Predict the binary outputs for each input example
    y_pred = model.predict(X_test)
    
    results = dict(zip(example_ids,y_pred))
    
    response = {
        "output" : str(results),
        "time" : time.time() - start
        }
    
    return jsonify(response), 200

@app.route("/predict_proba", methods=['POST'])
def predict_proba():
    start = time.time()
    
    if not request.json or not 'candidate_info' in request.json:
        abort(400)
        
    candidate_info = request.json['candidate_info']
    
    X_test = []
    example_ids = []
    y_test = []
    for exampleID, features in candidate_info.items():
        print(exampleID,type(features))
        example_ids.append(exampleID)
        y_test.append(features.pop('target'))
        X_test.append([val for val in features.values()])
    
    # Predict the probability of each class for each input example
    y_pred = model.predict_proba(X_test)
    
    results = dict(zip(example_ids,y_pred))
    
    response = {
        "output" : str(results),
        "time" : time.time() - start
        }
    
    return jsonify(response), 200

if __name__=="__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)