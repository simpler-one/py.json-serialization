from meta_info import DecorationHelper


def _on_complete(cls, store):
    pass


_HELPER = DecorationHelper("____json_serialization", _on_complete)



def default_creator(cls):
    return cls()


def json_class(creator=default_creator):
    pass


def json_property(json_prop_name=None, setter_name="$"):
    pass
