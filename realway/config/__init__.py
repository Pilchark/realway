# __init__.py
import pathlib
import tomli
import os


path = pathlib.Path(__file__).parent / "config.toml"
with path.open(mode="rb") as fp:
    conf = tomli.load(fp)
