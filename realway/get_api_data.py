# realway/get_api_data.py

from cgitb import text
import requests
import json
from rich import print
from config import conf
import pathlib
from datetime import datetime

# config args
key = conf["server"]["key"]
url = conf["server"]["url"]
cities = conf["info"]["cities"]
city = conf["city"]

def get_api_data():
    
    BJ = city["BeiJing"]["name"]
    SH = city["ShangHai"]["name"]
    t_args = {f"start": BJ, "end": SH, "key": key}

    # r = requests.post(f'{url}', params=t_args)
    r = requests.get("https://binstd.apistd.com/train/line?trainno=G34&key=9U2cUUZhHEqLZx5cx5G2owkd7")
    text = r.text
    return text


def export_json_data(res = None):
    date_format = datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
    json_file = "data/" + date_format + ".json"
    path = pathlib.Path(__file__).parent / json_file
    # with path.open(mode="w") as fp:
    #     json.dump(res, fp)
    with open(path, "w",encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False)

if __name__ == "__main__":
    res = get_api_data()
    export_json_data(res)
