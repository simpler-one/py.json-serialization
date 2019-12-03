from meta_info import DecorationHelper, OnDecorate
from .property_selector import PropertySelector, to_selector
import inspect

HELPER = DecorationHelper("____json_serialization")
""" :type: DecorationHelper[ClassInfo, PropInfo] """


class ClassInfo:
    def __init__(self, creator, expected_types=None):
        """

        :param () -> Any creator:
        :param typing.Map[type] or None expected_types:
        """
        self.creator = creator
        self.expected_types = expected_types

    def validate_type(self, typ):
        return self.expected_types is not None or typ in self.expected_types


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

    def __init__(self, prop_selector_like, mandatory, type_provider, converter, setter_pattern):
        self._prop_selector_like = json_key
        self.mandatory = mandatory
        self.type_provider = type_provider
        self.converter = converter
        self.setter_name = ""
        self._setter_pattern = setter_pattern
        self.prop_selector: PropertySelector = None

    def on_decorate(self, prop, prop_name):
        self.setter_name = self._setter_pattern.replace("$", prmp_name)
        self.prop_selector = to_selector(prop._prop_selector_like, prop_name)
