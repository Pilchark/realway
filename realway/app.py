from datetime import datetime
import json
import os
from flask import Flask
import sys
from pymongo import MongoClient
from flask import jsonify

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
from realway.config import conf

today = datetime.now().strftime("%Y-%m-%d")

def get_db():
    mongo_url = conf['mongo']['url']
    client = MongoClient(mongo_url)
    db = client['realway']
    return db

app = Flask(__name__)

class Config(object):
    MESSAGE = conf['mongo']['url']
    JSON_AS_ASCII = conf['app']['JSON_AS_ASCII']

app.config.from_object(Config)

# app route

@app.route("/")
def index():
    return "Hello"

@app.route("/settings")
def get_settings():
    return {
        "message": app.config["MESSAGE"],
        "json_format": app.config['JSON_AS_ASCII'],
    }

@app.route('/today')
def get_one():
    db = get_db()
    res = db[today].find_one({"status":0})
    output = {
        "start":res["result"]["start"], 
        "end":res["result"]["end"], 
        "nums":len(res["result"]["list"])
        }
    # return jsonify(output)
    return output


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
