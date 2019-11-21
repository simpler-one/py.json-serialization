from abc import abc, abstractmethod


class TypeProvider(ABC):
    @abstractmethod
    def get_type():
        raise NotImplementedError()


class SimpleType(TypeProvider):
    def __init__(self, obj_type):
        self.obj_type = obj_type

    def get_type():
        return self.obj_type


class WrappingType(TypeProvider, ABC):
    @classmethod
    def by_type():
        pass
