#TODO
import json,os,sys
import pathlib
from pymongo import MongoClient
from rich import print
import json
from datetime import datetime

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

today = datetime.now().strftime("%Y-%m-%d")

def get_json_files():
    data_dir = base_dir +  "/data/" + today + "/"
    all_json_file = os.listdir(data_dir)
    l = []
    for i in all_json_file:
        l.append(data_dir + i)
    return l

def json_to_dict(data):
    with open(data, "r") as f:
        data = json.load(f)
        return data

def insert_data_to_mongo(data):
    client = MongoClient('mongodb://test:123456@localhost:27017/')
    db = client['realway']
    col = db[today]
    col.insert_one(data).inserted_id

def main():
    all_json_file = get_json_files()
    for i in all_json_file:
        data = json_to_dict(i)
        insert_data_to_mongo(data)

if __name__ == "__main__":
    main()
