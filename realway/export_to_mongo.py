import json, os, sys
from typing import List
from pymongo import MongoClient
import json
from rich import print

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
from realway.config import conf, year, today
from realway.logger import logger

mongo_url = os.getenv("MONGODB_URL")
if mongo_url == None:
    mongo_url = conf["mongo"]["url"]


def get_json_paths(date):
    data_dir = base_dir + "/data/"
    daily_dir = os.path.join(data_dir, date)
    if not os.path.exists(daily_dir):
        raise ValueError("Path not exists")
    else:
        all_json_file = os.listdir(daily_dir)
        data_list = []
        for i in all_json_file:
            data_list.append(os.path.join(daily_dir, i))
        return data_list

def get_all_data_paths():
    data_dir = base_dir + "/data/"
    if not os.path.exists(data_dir):
        raise ValueError("Path not exists")
    else:
        all_data_dirs = os.listdir(data_dir)
        return all_data_dirs

def json_to_dict(data):
    with open(data, "r") as f:
        data = json.load(f)
        if data.get("status", "None") == "203":
            return None
        return data


def insert_many_to_mongo(all_json_file: List):
    all_data = []
    if all_json_file != None:
        for i in all_json_file:
            data = json_to_dict(i)
            if data != None:
                all_data.append(data)
    else:
        logger.warning("No json files today.")

    if len(all_data) != 0:
        client = MongoClient(mongo_url)
        db = client["realway"]
        col = db[year]
        col.insert_many(all_data)
        logger.info("Insert daily data Success !")
    else:
        logger.warning("No valid data insert.")

def insert_all_data():
    all_data_dirs = get_all_data_paths()
    for i_day in all_data_dirs:
        all_json_file = get_json_paths(i_day)
        insert_many_to_mongo(all_json_file)

def insert_daily_data():
    all_json_file = get_json_paths(date=today)
    insert_many_to_mongo(all_json_file)

if __name__ == "__main__":
    insert_daily_data()
