# TODO
import json, os, sys
import pathlib
from pymongo import MongoClient
from rich import print
import json
from datetime import datetime

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
from realway.config import conf, year, today
from bson.objectid import ObjectId


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

    def get_one_way_data(self, start, end, datetime=None):
        try:
            if None in (start, end):
                return None

            col = self.db[year]
            
            if datetime is not None:
                res = col.find_one(
                    {
                        "result.date": datetime,
                        "result.start": start,
                        "result.end": end,
                    }
                )
                output = {
                    "start": res["result"]["start"],
                    "end": res["result"]["end"],
                    "results": res["result"]["list"],
                }
                return output
            elif (datetime is None) and (None not in (start, end)):
                res = col.find(
                    {
                        "result.start": start,
                        "result.end": end,
                    }
                )
                count = col.count_documents(
                    {
                        "result.start": start,
                        "result.end": end,
                    }
                )
                res_list = []
                for i in res:
                    output = {
                        "start": start,
                        "end": end,
                        "date": i["result"]["date"],
                        "results": i["result"]["list"],
                    }
                    res_list.append(output)
                print(f"all result counts = {count}")
                return res_list
            else:
                count = col.count_documents({})
                return count

        except Exception as e:
            raise Exception("date not found")


def main():
    pass
    # fetcher = Fetcher()
    # # print(fetcher.mongo_url)
    # res = fetcher.get_data_by_detail(
    #     datetime="2022-08-26",
    # )
    # print(res)
    # for i in res:
    # print(i)


if __name__ == "__main__":
    main()
