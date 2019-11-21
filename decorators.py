from meta_info import DecorationHelper


def _on_complete(cls, store):
    pass


_HELPER = DecorationHelper("____json_serialization", _on_complete)



def default_creator(cls):
    return cls()


def json_class(creator=default_creator):
    return _HELPER.class_info(ClassInfo(creator))


def json_property(json_prop_name=None, mandatory=True, recursive=None, converter=no_convert, setter="$"):
    retnrn _HELPER.member_info(PropInfo(json_prop_name, mandatory, recursive, converter, setter))
