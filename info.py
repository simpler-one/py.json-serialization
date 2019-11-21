class ClassInfo:
    def __init__(self, creator):
        self.creator = creator


class PropInfo:
    def __init__(self, json_key, mandatory, recursive, converter, setter)
        self.json_key = json_key
        self.mandatory = mandatory
        self.recursive = recursive
        self.converter = converter
        self.setter = setter

    def on_complete(cls, prop):
        if self.json_key is None:
            self.json_key = prop
