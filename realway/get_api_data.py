# realway/get_api_data.py

import time
import requests
import json
from rich import print
from config import conf
import pathlib
from datetime import datetime

# config args
key = conf["server"]["key"]
url = conf["server"]["url"]
city = conf["city"]

def combination_all_city():
    for i in iter(city):
        start = city[i]["name"]
        for j in iter(city):
            end = city[j]["name"]
            if not start == end:
                start, end, res = get_api_data(start, end)
                export_json_data(start, end, res)
            else:
                pass

def get_api_data(start, end):
    """
    get all trips from start to end 
    """
    t_args = {f"start": start, "end": end, "key": key}
    r = requests.post(f'{url}', params=t_args)
    text = r.text
    res = json.loads(text)
    return start, end, res


def export_json_data(start, end, res):
    date_format = datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
    json_file = "data/" + date_format + "_" + start + "_" + end +".json"
    path = pathlib.Path(__file__).parent / json_file
    with open(path, "w",encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False)

def show_api_data():
    json_file = "data/" + "2022-07-27_16_10_14" + ".json"
    path = pathlib.Path(__file__).parent / json_file
    with open(path, "r",encoding="utf-8") as f:
        data = json.load(f)
        print(data["result"]["start"])
        print(data["result"]["end"])


def main():
    for i in iter(city):
        start = city[i]["name"]
        for j in iter(city):
            end = city[j]["name"]
            if not start == end:
                print(f"{start} -> {end}")
                start, end, res = get_api_data(start, end)
                export_json_data(start, end, res)
            else:
                pass

if __name__ == "__main__":
    main()
