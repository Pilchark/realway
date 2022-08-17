# main entry in docker

import time,os, sys
import schedule
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

# import realway
from realway import get_api_data,export_to_mongo

def run():
    print("running get api..")
    get_api_data.main()
    print("running export to mongo..")
    export_to_mongo.main()

schedule.every().day.at("00:05").do(run)
while True:
    schedule.run_pending()
    time.sleep(1)
