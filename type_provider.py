from abc import abc, abstractmethod


class TypeProvider(ABC):
    @abstractmethod
    def get_type(self, current_type, json_obj):
        raise NotImplementedError()


class SimpleType(TypeProvider):
    def __init__(self, current_type):
        self._obj_type = obj_type

    def get_type(self, current_type, json_obj):
        return self._obj_type


class SelfType(TypeProvider):
    def get_type(self, current_type, json_obj):
        return current_type


class ConditionalType(TypeProvider):
    @classmethod
    def by_type():
        pass

    def __init__(self, type_selector):
        self._type_selector = type_selector

    def get_type(self, current_type, json_obj):
        type_like = self._type_selector(current_type, json_obj)
        return to_provider(type_like).get_type(current_type, json_obj)


class ContainerType(TypeProvider, ABC):
    def __init__(self, tyep_like):
        self._inner_provider = to_provider(type_like)

    def get_type(self, current_type, json_obj):
        type_like = self._type_selector(current_type, json_obj)
        return to_provider(type_like).get_type(current_type, json_obj)


class ListType(ContainerType):
    pass


class ListType(ContainerType):
    pass


def to_provider(type_like):
    if type_like is None or isinstance(type_like, type):
        return SimpleType(type_like)
    if callable(type_like):
        return ConditionalType(type_like)
    if isinstance(type_like, TypeProvider):
        return type_like
    
    raise TypeException("parameter must be type or callable or TypeProvider but got: {type(type_like)}")
