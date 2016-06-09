class Cream:
    def __init__(self):
        self.value = "um"
class Coffee:
    def __init__(self):
        self.value = "Y"
    def __add__(self, cream):
        return self.value + cream.value