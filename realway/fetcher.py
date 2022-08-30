# TODO
import json, os, sys
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

class Fetcher(object):

    def __init__(self) -> None:
        self.mongo_url = os.getenv("MONGODB_URL")
        if self.mongo_url == None:
            # get mongo url in local host
            self.mongo_url = conf["mongo"]["url"]
        self.client = MongoClient(self.mongo_url)
        self.db = self.client["realway"]

    def get_data_by_status(self, stats=0):
        """status = 0 or status = "203" """
        res = self.db[today].find_one({"status": 0})
        output = {
            "start": res["result"]["start"],
            "end": res["result"]["end"],
            "nums": len(res["result"]["list"]),
        }
        return output


    def get_data_by_detail(self, datetime, start=None, end=None):
        try:
            q = self.db[datetime]
            if None not in (start, end):
                res = q.find_one(
                    {"result.start": start,
                    "result.end": end,
                    })
                output = {
                "start": res["result"]["start"],
                "end": res["result"]["end"],
                "results": res["result"]["list"],
            }
                return output
            elif start is not None:
                res = q.find(
                    {"result.start": start,
                    })
                count = q.count_documents({
                    "result.start": start,
                    })
                res_list = []
                for i in res:
                    output = {
                    "start": i["result"]["start"],
                    "end": i["result"]["end"],
                    "results": i["result"]["list"],
                    }
                    res_list.append(output)
                return res_list
            elif end is not None:
                res = q.find(
                    {"result.end": end,
                    })
                count = q.count_documents({
                    "result.end": end,
                    }) 
                res_list = []
                for i in res:
                    output = {
                    "start": i["result"]["start"],
                    "end": i["result"]["end"],
                    "results": i["result"]["list"],
                    }
                    res_list.append(output)
                return res_list
            else:
                res = q.find()
                count = q.count_documents({})
                return count

        except Exception as e:
            raise Exception("date not found")


def main():
    fetcher = Fetcher()
    # print(fetcher.mongo_url)
    res = fetcher.get_data_by_detail(datetime='2022-08-26',
    )
    print(res)
    # for i in res:
        # print(i)

if __name__ == "__main__":
    main()
