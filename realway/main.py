# main entry in docker
import time,os, sys
import schedule
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
from realway import get_api_data,export_to_mongo
from realway.logger import logger

def run():
    logger.info("running get api..")
    get_api_data.main()
def save():
    logger.info("running export to mongo..")
    export_to_mongo.main()

schedule.every().day.at("00:05").do(run)
schedule.every().day.at("10:05").do(save)
while True:
    schedule.run_pending()
    time.sleep(1)
