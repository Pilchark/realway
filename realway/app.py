from ast import arg
from datetime import datetime
import os, sys
from flask import Flask, jsonify, request
from pymongo import MongoClient

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
from realway.config import conf
from realway.fetcher import Fetcher

app = Flask(__name__)


def get_db():
    # get mongo url in docker
    mongo_url = os.getenv("MONGODB_URL")
    if mongo_url == None:
        # get mongo url in local host
        mongo_url = conf["mongo"]["url"]
    client = MongoClient(mongo_url)
    db = client["realway"]
    return db


class Config(object):
    JSON_AS_ASCII = False


app.config.from_object(Config)

fetcher = Fetcher()

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
        # db = get_db()
        # results = db[datetime].find()
        # l = []
        # for res in results:
        #     output = {
        #         "start": res["result"]["start"],
        #         "end": res["result"]["end"],
        #         "lines": len(res["result"]["list"]),
        #     }
        #     l.append(output)
        # return jsonify(l)
        return datetime
    except:
        return "fetch data failed!"


@app.route('/search', methods=['GET'])
def search():
    args = request.args
    datetime = args.get("datetime", None)
    start = args.get("start", None)
    end = args.get("end", None)
    return fetcher.get_data_by_detail(
            datetime=datetime,
            start=start,
            end=end)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
