from ast import arg
from datetime import datetime
import json
import os, sys
from flask import Flask, request, render_template, url_for, redirect
from pymongo import MongoClient

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
from realway.config import Config
from realway.fetcher import Fetcher
from realway.model import ExampleForm

app = Flask(__name__)
app.config.from_object(Config)
fetcher = Fetcher()

# index
@app.route('/', methods=['POST','GET'])
def index():
    form = ExampleForm()
    if form.validate_on_submit():
        date = form.date.data.strftime('%Y-%m-%d')
        start_s = form.start_s.data
        end_s = form.end_s.data
        if end_s == "sss":
            return render_template("404.html")
        return redirect(url_for('test', date=date,start_s=start_s,end_s=end_s))
        
        
        # return f'''<h1> Welcome {form.username.data} </h1>'''
    return render_template('index.html', title="Home",form=form)

@app.route('/test', methods=['GET'])
def test():
    args = request.args
    date = args.get("date", None)
    start_s = args.get("start_s", None)
    end_s = args.get("end_s", None)

    return {
        "date" : date,
        "start_s" : start_s,
        "end_s" : end_s,
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
    title = data_all['start'] + '-' + data_all['end']
    l = []
    for d in data_all['list']:
        l.append((d['trainno'], d['station']+ '-' +d['endstation'], d['departuretime'], d['arrivaltime'], d['priceed']))
    # return render_template('bar_chart.html', title='test TITLE', values=l)
    return render_template('echart_sample.html', title=title, values=l)


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

@app.route('/chart_sample')
def chart_sample():
    return render_template('echart_sample.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
