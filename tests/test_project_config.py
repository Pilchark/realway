import os,sys
from rich import print
import configparser
from os import environ, path
from dotenv import load_dotenv

def test_get_ini():
    config = configparser.ConfigParser()
    config.read_file(open('config.ini'))
    a = config.get('DATABASE','HOST')
    debug = config.getboolean('APP','DEBUG')

    assert all([
        debug is False,
        a == '127.0.0.1'
    ])

def test_env():
    # Find .env file
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    env_conf = path.join(base_dir, '.env')
    load_dotenv(env_conf)

    # General Config
    FLASK_ENV = environ.get('FLASK_ENV')
    assert FLASK_ENV == "development"

