from meta_info import 


class ClassInfo:
    def __init__(self, creator):
        self.creator = creator


class PropInfo():
    @classmethod
    def _get_getter(cls, prop_name):
        if prop_name.startswith("*"):
            return lambda obj: obj
        else:
            return lambda obj: obj[prop_name]

    def __init__(self, json_key, mandatory, recursive, converter, setter):
        self.prop_name = ""
        self.json_key = json_key
        self.mandatory = mandatory
        self.recursive = recursive
        self.converter = converter
        self.setter_name = ""
        self._setter_pattern = setter

    def on_decorate(cls, prop):
        self.prop_name = prop
        if self.json_key is None:
            self.json_key = prop

        self.setter_name = self._setter_pattern.replace("$", prop)
