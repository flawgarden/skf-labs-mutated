class ReflectionHelper:

    value: str

    def __init__(self, value: str):
        self.value = value

    def get_value(self) -> str:
        return self.value