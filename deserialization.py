from typing import TypeVar
import json
from info import ClassInfo, PropInfo, HELPER

T = TypeVar("T")


def parse(text, cls, option):
    return _from_json_obj(json.parse(text), cls, option, cls.__name__)

def from_json_obj(obj, cls, option):
    return _from_json_obj(obj, cls, option, cls.__name__)

def _from_json_obj(obj, cls, option, path):
    store = HELPER.get_store(cls)
    if store is None:
        raise ValueError("cls must be decorated by json_class")
