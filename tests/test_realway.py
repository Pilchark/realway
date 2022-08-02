import pathlib,os
from realway import __version__
from config import conf
from realway.get_api_data import (
    combination_all_city,
    export_json_data,
    base_dir
    )
from pypinyin import lazy_pinyin
from math import comb
from datetime import datetime


def test_version():
    assert __version__ == '0.1.0'

def test_config_city_name():
    """test if city CN name equal to EN name
    """
    city = conf["city"]
    print(city.keys())

    for i in city.keys():
        name = city[i]["name"]
        check_name = "".join(lazy_pinyin(name))
        pinyin = str(city[i]["pinyin"]).lower()
        assert check_name == pinyin

def test_all_combination_num():
    """test if all combination number equal to C(city_num, 2)
    """
    city = conf["city"]
    city_len = len(city.keys())
    city_num = comb(city_len, 2) * 2

    all_list_len = len(combination_all_city())

    assert city_num  == all_list_len

def test_data_store_path():
    """test if data store path is "<project>/data/<date>/file.json"
    """
    time = datetime.now().strftime("%Y-%m-%d")
    valid_path = pathlib.Path(__file__).parent.parent / "data" / time
    file_format = time + "_a_b.json"
    valid_path = valid_path / file_format
    file_path = export_json_data("a","b","c")
    assert str(valid_path) == file_path
    os.remove(file_path)

def test_data_store_dir():
    """test if data store dir is "<project>/data/<date>/"
    """
    time = datetime.now().strftime("%Y-%m-%d")
    valid_path = pathlib.Path(__file__).parent.parent
    assert str(valid_path) == base_dir

