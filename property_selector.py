from abc import ABC, abstractmethod


class PropertySelector(ABC):
    @abstractmethod
    def get_from(self, json_obj):
        """

        :param list or dict json_obj:
        """
        raise NotImplementedError()


class IndexPropertySelector:
    def __init__(self, key):
        self._key = key

    def get_from(self, json_obj):
        return json_obj[self._key] if self._key < len(json_obj) else None


class NamePropertySelector:
    def __init__(self, key):
        self._key = key

    def get_from(self, json_obj):
        return json_obj.get(self._key)


class AllPropertySelector:
    def get_from(self, json_obj):
        return json_obj


ALL = AllPropertySelector()


def to_selector(selector_like, prop_name):
    """

    :param str or int or PropertySelector selector_like:
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
