# __init__.py
import pathlib
import tomli
import os
from datetime import datetime


path = pathlib.Path(__file__).parent / "config.toml"
with path.open(mode="rb") as fp:
    conf = tomli.load(fp)

mongo_url = os.getenv("MONGODB_URL")
if mongo_url == None:
    mongo_url = conf["mongo"]["url"]

year = datetime.now().strftime("%Y")
today = datetime.now().strftime("%Y-%m-%d")
