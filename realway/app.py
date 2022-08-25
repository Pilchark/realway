from datetime import datetime
import os, sys
from flask import Flask, jsonify
from pymongo import MongoClient

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
from realway.config import conf

# today = datetime.now().strftime("%Y-%m-%d")


def get_db():
    # get mongo url in docker
    mongo_url = os.getenv("MONGODB_URL")
    if mongo_url == None:
        # get mongo url in local host
        mongo_url = conf["mongo"]["url"]
    client = MongoClient(mongo_url)
    db = client["realway"]
    return db


app = Flask(__name__)


class Config(object):
    JSON_AS_ASCII = conf["app"]["JSON_AS_ASCII"]


app.config.from_object(Config)

# app route


@app.route("/")
def index():
    return "Hello"


@app.route("/settings")
def get_settings():
    return {
        "JSON_AS_ASCII": app.config["JSON_AS_ASCII"],
    }


@app.route("/api/day/<datetime>/")
def api_day(datetime):
    try:
        db = get_db()
        results = db[datetime].find()
        l = []
        for res in results:
            output = {
                "start": res["result"]["start"],
                "end": res["result"]["end"],
                "lines": len(res["result"]["list"]),
            }
            l.append(output)
        return jsonify(l)
    except:
        return "fetch data failed!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
