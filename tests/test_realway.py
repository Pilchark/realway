from realway import __version__
from realway.config import conf
from pypinyin import pinyin, lazy_pinyin, Style

def test_version():
    assert __version__ == '0.1.0'

def test_config_city_name():
    """
    test if city CN name equal to EN name
    """
    
    cities = conf["info"]["cities"]

    for i in cities:
        name = i["name"]
        check_name = "".join(lazy_pinyin(name))
        pinyin = str(i["pinyin"]).lower()
        assert check_name == pinyin

