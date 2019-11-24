from abc import abc, abstractmethod


class TypeProvider(ABC):
    @abstractmethod
    def get_type(self, self_cls, json_obj):
        raise NotImplementedError()


class SimpleType(TypeProvider):
    def __init__(self, obj_type):
        self.obj_type = obj_type

    def get_type(self, self_cls, json_obj):
        return self.obj_type


class SelfType(TypeProvider):
    def get_type(self, self_cls, json_obj):
        return self_cls


class ConditionalType(TypeProvider):
    @classmethod
    def by_type():
        pass
