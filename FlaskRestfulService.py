# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 21:21:31 2019

@author: lippe
"""

from flask import Flask, redirect, render_template
from flask.helpers import url_for
from flask_restful import Api, Resource
from flask import jsonify, request
# Also deine a global variable by the name of
noOfVisitors = 0

webapp = Flask(__name__)
api=Api(webapp)

@api.resource('/hello')
def get(self):
    return 'Hello - this is GET'
def post(self):
    #Retrieve the JSON data from the Request and store it in local variable
    jsonData = request.get_json(cache=False)
    #Iterate over the JSON Data and print the data on console
    for key in jsonData:
        import json
        print(json.dumps(jsonData, indent=2, sort_keys=True) )
    #reference to Global Variable
    global noOfVisitors
    #Adding 1 to the global Variable
    noOfVisitors = noOfVisitors + 1
    #Converting the response to JSON and returning back to user
    return jsonify(totalVisits = noOfVisitors)

def put(self):
    return 'Hello - this is PUT'
def delete(self):
    return 'Hello - this is DELETE'


if __name__ == '__main__':
    webapp.run(host='0.0.0.0',port=8999,debug=True)