import os,sys
from rich import print
import configparser
from dotenv import load_dotenv
from pymongo import MongoClient

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from realway.config import mongo_url, year

def test_insert_data():
    client = MongoClient(mongo_url)
    db = client["realway"]
    col = db['test']
    col.delete_many({})
    data = [
        {"test_name":1},
        {"test_name":2},
        {"test_name":3}]
    col.insert_many(data)
    count = col.count_documents({})
    assert count == 3
    
