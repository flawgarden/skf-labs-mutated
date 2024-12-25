from abc import ABC
class SuperInterface(ABC):
    pass


class SubInterface(SuperInterface):
    pass


class SideInterface(ABC):
    pass


class ImplementingSuperClass(SuperInterface):
    pass


class ImplementingSubClass(SubInterface):
    pass


class ImplementingSuperSideClass(SuperInterface, SideInterface):
    pass