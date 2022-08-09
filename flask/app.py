import os
from flask import Flask
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
from realway.config import conf

class Config(object):
    MESSAGE = conf['mongo']['url']

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/settings")
def get_settings():
    return { "message": app.config["MESSAGE"] }

if __name__ == "__main__":
    print(sys.path)
    app.run()
