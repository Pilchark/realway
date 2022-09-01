import json, os, sys
from pymongo import MongoClient
import json

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
from realway.config import conf, year, today

mongo_url = os.getenv("MONGODB_URL")
if mongo_url == None:
    mongo_url = conf["mongo"]["url"]


def get_json_files():
    data_dir = base_dir + "/data/" + today + "/"
    if not os.path.exists(data_dir):
        raise ValueError("Path not exists")
    else:
        all_json_file = os.listdir(data_dir)
        data_list = []
        for i in all_json_file:
            data_list.append(data_dir + i)
        return data_list


def json_to_dict(data):
    with open(data, "r") as f:
        data = json.load(f)
        if data.get("status", "None") == "203":
            return None
        return data


def insert_data_to_mongo(data):
    client = MongoClient(mongo_url)
    db = client["realway"]
    col = db[year]
    col.insert_one(data).inserted_id


def insert_multi_data_to_mongo(data):
    client = MongoClient(mongo_url)
    db = client["realway"]
    col = db[year]
    col.insert_many(data)


def main():
    try:
        all_json_file = get_json_files()
    except ValueError as e:
        print(e)
        all_json_file = None

    all_data = []
    if all_json_file != None:
        for i in all_json_file:
            data = json_to_dict(i)
            if data != None:
                all_data.append(data)
    if len(all_data) != 0:
        insert_multi_data_to_mongo(all_data)
    else:
        print("No valid data insert")


if __name__ == "__main__":
    main()
