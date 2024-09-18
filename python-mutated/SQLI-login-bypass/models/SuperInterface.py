from abc import ABC, abstractmethod
class SuperInterface(ABC):
    @abstractmethod
    def get_value(self, value):
        pass


from abc import ABC
class SubInterface1(SuperInterface, ABC):
    def get_value(self, value):
        return value


from abc import ABC
class SubInterface2(SuperInterface, ABC):
    def get_value(self, value):
        return ""