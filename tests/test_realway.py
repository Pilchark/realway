from realway import __version__
from realway.config import conf
from realway.get_api_data import combination_all_city
from pypinyin import lazy_pinyin
from math import comb


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

