from ast import arg
from datetime import datetime
import json
import os, sys
import re
import numpy as np
import pandas as pd
from flask import Flask, request, render_template, url_for, redirect
from pymongo import MongoClient
from rich import print

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
from realway.config import Config
from realway.fetcher import Fetcher
from realway.model import ExampleForm

app = Flask(__name__)
app.config.from_object(Config)
fetcher = Fetcher()

# index
@app.route("/", methods=["POST", "GET"])
def index():
    form = ExampleForm()
    if form.validate_on_submit():
        date = form.date.data.strftime("%Y-%m-%d")
        start_s = form.start_s.data
        end_s = form.end_s.data
        if end_s == "sss":
            return render_template("404.html")
        return redirect(url_for("test", date=date, start_s=start_s, end_s=end_s))

        # return f'''<h1> Welcome {form.username.data} </h1>'''
    return render_template("index.html", title="Home", form=form)


@app.route("/test", methods=["GET"])
def test():
    args = request.args
    date = args.get("date", None)
    start_s = args.get("start_s", None)
    end_s = args.get("end_s", None)

    return {
        "date": date,
        "start_s": start_s,
        "end_s": end_s,
    }


@app.route("/api/day/<datetime>/")
def api_day(datetime):
    try:
        # db = get_db()
        # results = db[datetime].find()
        # l = []
        # for res in results:
        #     output = {
        #         "start": res["result"]["start"],
        #         "end": res["result"]["end"],
        #         "lines": len(res["result"]["list"]),
        #     }
        #     l.append(output)
        # return jsonify(l)
        return datetime
    except:
        return "fetch data failed!"


@app.route("/search_one_day", methods=["GET"])
def search_one_day():
    """
    search date from mongodb
    args:
        start (required): "北京"
        end (required): "上海"
        datetime (required): YYYY-MM-DD
    """
    args = request.args
    datetime = args.get("datetime", None)
    start = args.get("start", None)
    end = args.get("end", None)
    # res = fetcher.get_one_way_data(datetime=datetime, start=start, end=end)
    sample_data = os.path.join(base_dir, "data/sample.json")
    with open(sample_data, "r") as f:
        res = json.load(f)
    data_all = res["result"]
    title = data_all["start"] + "-" + data_all["end"]
    
    l = []
    for d in data_all["list"]:
        cost_time = d["costtime"]
        cost_time = re.findall("\d+",cost_time)
        cost_time = round(float(cost_time[0]) + float(cost_time[1])/60, 2)
        print(cost_time)
        l.append(
            (
                d["trainno"],
                d["station"] + "-" + d["endstation"],
                cost_time,
                d["priceed"],
                d["priceyd"],
                d["pricesw"],
            )
        )
        sorted_l = sorted(l, key=lambda k: k[2])
    # return render_template('bar_chart.html', title='test TITLE', values=l)
    return render_template("echart_sample.html", title=title, values=sorted_l)

@app.route("/api/search_one_day", methods=["GET"])
def api_search_one_day():
    """
    search date from mongodb
    args:
        start (required): "北京"
        end (required): "上海"
        datetime (required): YYYY-MM-DD
    """
    args = request.args
    datetime = args.get("datetime", None)
    start = args.get("start", None)
    end = args.get("end", None)
    # res = fetcher.get_one_way_data(datetime=datetime, start=start, end=end)
    sample_data = os.path.join(base_dir, "data/sample.json")
    with open(sample_data, "r") as f:
        res = json.load(f)
    res = res["result"]['list']
    length = len(res)
    width = 30
    np_data = np.full((length, width), np.NaN, dtype="U20")
    i,j=0,0
    col = [i for i in res[0].keys()]
    for i_train in res:
        for v in i_train.values():
            np_data[i][j] = v
            j+=1
        i+=1
        j=0
    df = pd.DataFrame(np_data, columns=col, index=[l for l in range(1,length+1)])
    print(df)
    return "200"
    df_html = df.to_html()
    print(df_html)
    return render_template('case.html', table=df_html)

@app.route("/search_one_way", methods=["GET"])
def search_one_way():
    """
    search date from mongodb
    args:
        start (required): "北京"
        end (required): "上海"
        datetime (optional): YYYY-MM-DD
    """
    args = request.args
    datetime = args.get("datetime", None)
    start = args.get("start", None)
    end = args.get("end", None)
    return fetcher.get_one_way_data(datetime=datetime, start=start, end=end)


@app.route("/chart_sample")
def chart_sample():
    return render_template("echart_sample.html")

@app.route("/element_sample")
def element_sample():
    return render_template("echart_sample.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
