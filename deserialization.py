from typing import TypeVar
import json
from info import ClassInfo, PropInfo, HELPER

T = TypeVar("T")


def parse(text, cls, option):
    return _from_json_obj(json.parse(text), cls, option, cls.__name__)

def from_json_obj(json_obj, cls, option):
    return _from_json_obj(json_obj, cls, option, cls.__name__)

def _from_json_obj(src, cls, option, path):
    store = HELPER.get_store(cls)
    if store is None:
        raise ValueError("cls must be decorated by json_class")

    # if store.cls.expected_types is not None and type(src) not in store.cls.expected_types:
    #     raise ValueError(f"Unexpected JSON object expected: {}, actual: {}")

    dst = store.cls.creator()

    for key, member in store.members.items():
        json_key = member.json_key
        cur_path = "{path}.{json_key}"
        item = member.getter(src)
        if item is None:
            if member.mamdarory:
                raise VallueError(f"Property is mandatory but null or not found: {path}")
            else:
                continue

        if member.recursive is not None and  type(item) in CONTAINER_TYPES:
            item = _expand(item, member, cur_path)

        setattr(dst, member.setter_name, item)


def _expand(src, recursive, path):
    pass
