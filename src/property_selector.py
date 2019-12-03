from abc import ABC, abstractmethod


class PropertySelector(ABC):
    @property
    def path(self):
        return f".{self.key}"

    def __init__(self, key):
        self.key = key

    @abstractmethod
    def get_from(self, json_obj):
        """

        :param list or dict json_obj:
        """
        raise NotImplementedError()


class ListPropertySelector(PropertySelector):
    def get_from(self, json_obj):
        return json_obj[self.key] if self.key < len(json_obj) else None


class MapPropertySelector(PropertySelector):
    def get_from(self, json_obj):
        return json_obj.get(self.key)


class AllPropertySelector(PropertySelector):
    @property
    def path(self):
        return ""

    def __init__(self):
        super().__init__(None)

    def get_from(self, json_obj):
        return json_obj


ALL = AllPropertySelector()


def to_selector(selector_like):
    """

    :param str or int or PropertySelector selector_like:
    """
    if selector_like is None:
        return None
    if isinstance(selector_like, int):
        return ListPropertySelector(selector_like)
    if isinstance(selector_like, str):
        return MapPropertySelector(selector_like)
    if isinstance(selector_like, PropertySelector):
        return selector_like
    
    raise TypeError(f"selector must be int or str or PropertySelector but got: {type(selector_like)}")
