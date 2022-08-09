#TODO
import json,os,sys
import pathlib
from unittest import result
from pymongo import MongoClient
from rich import print
import json
from datetime import datetime

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
from realway.config import conf
from bson.objectid import ObjectId

def get_data_from_mongo():
    mongo_url = conf['mongo']['url']
    client = MongoClient(mongo_url)
    db = client['realway']
    name_1 = db.list_collection_names()[0]
    # print(db[name_1].find_one({"msg":"没有信息"})["_id"])
    id = "62f1ddece2fd28b7d6465a59"
    print(db[name_1].find_one({"_id":ObjectId(id)}))
    
    new_posts = [{"author": "Mike",
              "text": "Another post!",
              "tags": ["bulk", "insert"],
              "date": datetime(2009, 11, 12, 11, 14)},
             {"author": "Eliot",
              "title": "MongoDB is fun",
              "text": "and pretty easy too!",
              "date": datetime(2009, 11, 10, 10, 45)}]
    result = db[name_1].insert_many(new_posts)
    # print(db.list_collection_names())
    # col = db.name_1
    # print(col.name)


def main():
    get_data_from_mongo()

if __name__ == "__main__":
    main()
