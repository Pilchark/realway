# realway/get_api_data.py

import requests
import json
import pathlib
import os,sys
from datetime import datetime
from rich import print

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
from realway.config import conf

# config args
key = conf["server"]["key"]
url = conf["server"]["url"]
city = conf["city"]

def combination_all_city():
    """Show all combination among all cities
    """
    all_list = []
    for i in iter(city):
        start = city[i]["name"]
        for j in iter(city):
            end = city[j]["name"]
            if not start == end:
                all_list.append((start, end))
    return all_list


def get_api_data(start, end):
    """get all trips from start to end(single json string)
    """
    t_args = {f"start": start, "end": end, "key": key}
    r = requests.post(f'{url}', params=t_args)
    text = r.text
    res = json.loads(text)
    return res

def export_json_data(start, end, res):
    """export api data to json file
    """
    data_format = datetime.now().strftime("%Y-%m-%d")
    folder = base_dir + "/data/" + data_format + "/"
    if not os.path.exists(folder):
        os.mkdir(folder)
    else:
        pass
    file_path = folder + data_format + "_" + start + "_" + end +".json"
    with open(file_path, "w",encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False)
    return file_path

def main():
    all_trip = combination_all_city()
    for start, end in all_trip:
        res = get_api_data(start, end)
        export_json_data(start, end, res)

if __name__ == "__main__":
    main()
