# main entry in docker

import time,os, sys
import schedule
from rich import print
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from realway import get_api_data,export_to_mongo

def main():
    print("running get api..")
    get_api_data.main()
    print("running export to mongo..")
    export_to_mongo.main()

schedule.every().day.at("00:05").do(main)
while True:
    schedule.run_pending()
    time.sleep(1)
