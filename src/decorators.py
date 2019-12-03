from info import ClassInfo, PropInfo, HELPER
from type_provider import to_provider 


def _on_complete(cls, store):
    for key, prop_info in store.members.items():
        prop_info.on_complete(cls, key)


def no_convert(obj, *_):
    return obj


def json_class(*, creator=None, expected_types=None):
    return HELPER.class_info(ClassInfo(creator, expected_types))


def json_property(json_prop_name=None, mandatory=True, recursive=None, *, converter=no_convert, setter="$"):
    type_provider = to_provider(recursive)
    return HELPER.member_info(PropInfo(json_prop_name, mandatory, type_provider, converter, setter))
