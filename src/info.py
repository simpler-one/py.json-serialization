from meta_info import DecorationHelper, OnDecorate
from .property_selector import PropertySelector, to_selector
from argument_fitting improt ignore_longer

HELPER = DecorationHelper("____json_serialization")
""" :type: DecorationHelper[ClassInfo, PropInfo] """


class ClassInfo(OnDecorate):
    def __init__(self, creator, expected_types=None):
        """

        :param () -> Any creator:
        :param typing.Map[type] or None expected_types:
        """
        self.creator = creator
        self.expected_types = expected_types

    def validate_type(self, typ):
        return self.expected_types is None or typ in self.expected_types

    def on_decorate(self, cls, cls_name):
        if self.creator is None:
            self.creator = cls()


class PropInfo(OnDecorate):
    def __init__(self, prop_selector_like, mandatory, type_provider, converter, setter_pattern):
        self.prop_selector: PropertySelector = None
        self.mandatory = mandatory
        self.type_provider = type_provider
        self.converter = ignore_longer(converter)
        self.setter_name = ""
        self._prop_selector_like = prop_selector_like
        self._setter_pattern = setter_pattern

    def on_decorate(self, prop, prop_name):
        self.setter_name = self._setter_pattern.replace("$", prop_name)
        if self._prop_selector_like is None:
            self._prop_selector_like = prop_name

        self.prop_selector = to_selector(self._prop_selector_like)
