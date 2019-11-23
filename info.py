from meta_info import 


class ClassInfo:
    def __init__(self, creator):
        self.creator = creator


class PropInfo():
    @classmethod
    def _get_getter(cls, json_key):
        if json_key == property_selector.ALL:
            return lambda obj: obj
        else:
            return lambda obj: obj.get(json_key)

    def _normalize_converter(cls, converter):
        # TODO: check cls, self
        if len(inspect.get(converter)) == 2:
            return 
        else:
            return converter

    def __init__(self, json_key, mandatory, recursive, converter, setter):
        self.prop_name = ""
        self.json_key = json_key
        self.mandatory = mandatory
        self.recursive = recursive
        self.converter = converter
        self.setter_name = ""
        self._setter_pattern = setter
        self.getter = self._get_getter(json_key)

    def on_decorate(cls, prop):
        self.prop_name = prop
        if self.json_key is None:
            self.json_key = prop

        set.getter = self._get_getter(self.json_key)
        self.setter_name = self._setter_pattern.replace("$", prop)
