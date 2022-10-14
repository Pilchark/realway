from ast import arg
import json
import os, sys
import re
import numpy as np
import pandas as pd
from datetime import datetime
from flask import Flask, request, render_template, url_for, redirect
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
        data = {
            "date": date,
            "start_s": start_s,
            "end_s": end_s,
        }
        print(data)
        # return redirect(
        #     url_for("test", data)
        # )
        return redirect(
            url_for("api_search_one_day", datetime=date, start=start_s, end=end_s)
        )

    return render_template("index.html", title="Home", form=form)

@app.route("/test", methods=["GET"])
def test():
    args = request.args
    return args.get("data",None)

@app.route("/api/search", methods=["GET"])
def api_search_one_day():
    """
    search date from mongodb
    args:
        start (required): "北京"
        end (required): "上海"
        datetime (required): YYYY-MM-DD
    """
    args = request.args
    if args:
        datetime = args.get("datetime", None)
        start = args.get("start", None)
        end = args.get("end", None)
        if None in (start, end):
            return {"status": 400, "msg": "start or end should not be Empty !"}
        res = fetcher.get_one_way_data(datetime=datetime, start=start, end=end)
        if res is None:
            return {"status": 400, "msg": "Data not Found !"}
        else:
            # return {"status": 200, "data": res}
            pass
    else:
        sample_data = os.path.join(base_dir, "sample.json")
        with open(sample_data, "r") as f:
            res = json.load(f)

    res = res["result"]["list"]
    length = len(res)
    width = 30
    np_data = np.full((length, width), np.NaN, dtype="U20")
    i, j = 0, 0
    col = [i for i in res[0].keys()]
    for i_train in res:
        for v in i_train.values():
            np_data[i][j] = v
            j += 1
        i += 1
        j = 0

    df = pd.DataFrame(np_data, columns=col)
    df = df.drop(df.columns[[8, 9, 10, 11, 12]], axis=1)
    # return df.to_dict()
    df_html = df.to_html(classes="ui celled table", table_id="data")
    return render_template("table.html", table=df_html, title="test Title")


@app.route("/chart_sample")
def chart_sample():
    return render_template("echart_sample.html")


@app.route("/element_sample")
def element_sample():
    return render_template("element_sample.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
