import os,sys
from rich import print
import configparser

# config = configparser.ConfigParser()
# config.read_file(open('config.ini'))
# a = config.get('DATABASE','HOST')
# b = config.getboolean('APP','DEBUG')

# print(a)
# print(b)

"""App configuration."""
from os import environ, path
from dotenv import load_dotenv

# Find .env file
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_conf = path.join(base_dir, '.env')
load_dotenv(env_conf)

# General Config
SECRET_KEY = environ.get('SECRET_KEY')
FLASK_APP = environ.get('FLASK_APP')
FLASK_ENV = environ.get('FLASK_ENV')

print(SECRET_KEY)
print(FLASK_APP)
print(FLASK_ENV)

