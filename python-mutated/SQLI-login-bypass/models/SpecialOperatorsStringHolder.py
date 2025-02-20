class SpecialOperatorsStringHolder:

    def __init__(self, value=""):
        self.value = value
        self.index = 42

    def __getitem__(self, index):
        if index == self.index:
            return self.value
        else:
            return ""

    def __str__(self):
        return self.value

    def __pos__(self):
        return SpecialOperatorsStringHolder(self.value)

    def __neg__(self):
        return SpecialOperatorsStringHolder("")

    def __add__(self, other):
        return self

    def __sub__(self, other):
        return other