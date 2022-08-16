import os,sys
from rich import print
import configparser
from dotenv import load_dotenv

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def test_ini():
    config = configparser.ConfigParser()
    config.read('config.ini')
    ip = config.get('DATABASE','HOST')
    debug = config.getboolean('APP','DEBUG')

    assert all([
        debug is True,
        ip == '127.0.0.1'
    ])

def test_env():
    # Find .env file
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    env_conf = os.path.join(base_dir, '.env')
    load_dotenv(env_conf)

    # General Config
    FLASK_DEBUG = os.getenv('FLASK_DEBUG')
    FLASK_APP = os.getenv('FLASK_APP')
    assert all([
        FLASK_DEBUG == "1",
        FLASK_APP == 'realway.app'
    ])
