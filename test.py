from datetime import datetime
import json
import os
from flask import Flask
import sys
from pymongo import MongoClient
from flask import jsonify

def get_db():
    mongo_url = "mongodb://test:123456@localhost:27017/"
    client = MongoClient(mongo_url)
    db = client['realway']
    return db

today = datetime.now().strftime("%Y-%m-%d")

if __name__ == "__main__":
    db = get_db()
    res = db[today].find_one({"status":0})

    output = {
        "start":res["result"]["start"], 
        "end":res["result"]["end"], 
        "nums":len(res["result"]["list"])
        }
    print(output)
