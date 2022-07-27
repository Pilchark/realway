from realway import __version__
from realway.config import conf
from pypinyin import lazy_pinyin

def test_version():
    assert __version__ == '0.1.0'

def test_config_city_name():
    """
    test if city CN name equal to EN name
    """
    
    city = conf["city"]
    
    print(city.keys())

    for i in city.keys():
        name = city[i]["name"]
        check_name = "".join(lazy_pinyin(name))
        pinyin = str(city[i]["pinyin"]).lower()
        assert check_name == pinyin

