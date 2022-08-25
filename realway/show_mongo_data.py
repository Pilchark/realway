# TODO
import json, os, sys
from operator import eq
import pathlib
from pymongo import MongoClient
from rich import print
import json
from datetime import datetime

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
from realway.config import conf
from bson.objectid import ObjectId

today = datetime.now().strftime("%Y-%m-%d")


def get_data_by_status(stats=0):
    """status = 0 or status = "203" """
    mongo_url = conf["mongo"]["url"]
    client = MongoClient(mongo_url)
    db = client["realway"]
    res = db[today].find_one({"status": 0})
    # print(db[today].find_one({"status":stats}))
    # for r in db[today].find({"status":stats}):
    #     print(r)
    output = {
        "start": res["result"]["start"],
        "end": res["result"]["end"],
        "nums": len(res["result"]["list"]),
    }
    print(output)


def get_data_by_s_city():
    mongo_url = conf["mongo"]["url"]
    client = MongoClient(mongo_url)
    db = client["realway"]
    result = db[today].find_one({"result.start": "上海"})
    print(type(result))
    print(result["_id"])


def main():
    get_data_by_status("203")
    # get_data_by_s_city()


if __name__ == "__main__":
    main()
