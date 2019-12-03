from abc import ABC, abstractmethod


class PropertySelector(ABC):
    @property
    def json_path(self):
        return f".{self.json_key}"

    def __init__(self, json_key):
        self.json_key = json_key

    @abstractmethod
    def get_from(self, json_obj):
        """

        :param list or dict json_obj:
        """
        raise NotImplementedError()


class IndexPropertySelector(PropertySelector):
    def __init__(self, key):
        self._key = key

    def get_from(self, json_obj):
        return json_obj[self._key] if self._key < len(json_obj) else None


class NamePropertySelector(PropertySelector):
    def __init__(self, key):
        self._key = key

    def get_from(self, json_obj):
        return json_obj.get(self._key)


class AllPropertySelector(PropertySelector):
    def get_from(self, json_obj):
        return json_obj


ALL = AllPropertySelector()


def to_selector(selector_like, prop_name):
    """

    :param str or int or PropertySelector selector_like:
    :param str prop_name:
    """
    if selector_like is None:
        return NamePropertySelector(prop_name)
    if isinstance(selector_like, int):
        return IndexPropertySelector(selector_like)
    if isinstance(selector_like, str):
        return NamePropertySelector(selector_like)
    if isinstance(selector_like, PropertySelector):
        return selector_like
    
    raise TypeError(f"selector must be int or str or PropertySelector but got: {type(selector_like)}")
