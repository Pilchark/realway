import logging
import sys,os
from datetime import datetime

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

logger = logging.getLogger(__name__)
log_path = datetime.now().strftime("%Y%m%d_%H%M%S") + ".log"
logger.setLevel(logging.DEBUG)
# fh = logging.FileHandler(log_path)
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter(
    "%(asctime)s:%(name)s:%(funcName)s:[%(levelname)s]:%(message)s"
)
handler.setFormatter(formatter)
# fh.setFormatter(formatter)
logger.addHandler(handler)
# logger.addHandler(fh)

# usage
# logger.debug('A debug message')
# logger.info('An info message')
# logger.warning('There is something wrong')
# logger.error('An error has happened.')
# logger.critical('Fatal error occured. Cannot continue')
