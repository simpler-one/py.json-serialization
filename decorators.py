from meta_info import DecorationHelper
from info import ClassInfo, PropInfo, HELPER


def _on_complete(cls, store):
    for key, prop_info in store.members.items():
        prop_info.on_complete(cls, key)


def default_creator(cls):
    return cls()


def json_class(creator=default_creator):
    return HELPER.class_info(ClassInfo(creator))


def json_property(json_prop_name=None, mandatory=True, recursive=None, converter=no_convert, setter="$"):
    return HELPER.member_info(PropInfo(json_prop_name, mandatory, recursive, converter, setter))
