class SuperClass:
    def __init__(self, value: str):
        self.v = value


class SubClass(SuperClass):
    pass


from typing import final


@final
class SubSubClass(SubClass):
    pass


class SiblingClass(SuperClass):
    pass