class ImplementsEnterExit:
    def __init__(self, text):
        self.text = text

    def __enter__(self):
        return self.text

    def __exit__(self, *args):
        self.text = "42"