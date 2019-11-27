from meta_info import DecorationHelper, OnDecorate
from property_selector import PropertySelector, to_selector
import inspect

_HELPER = DecorationHelper("____json_serialization")


class ClassInfo:
    def __init__(self, creator):
        self.creator = creator


class PropInfo(OnDecorate):
    @classmethod
    def _normalize_converter(cls, converter):
        """

        :param ((list or dict) -> Any) or ((list or dict, Any) -> Any) converter:
        """
        arg_len = len(inspect.getfullargspec(converter))
        if hasattr(converter, "__self__"):
            arg_len = arg_len - 1

        if arg_len == 1:
            return lambda obj, _: converter(obj)
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
        self.getter: PropertySelector = None

    def on_decorate(self, prop):
        self.prop_name = prop
        if self.json_key is None:
            self.json_key = prop

        set.getter = self._get_getter(self.json_key)
        self.setter_name = self._setter_pattern.replace("$", prop)
        self.getter = to_selector(prop.json_key)
