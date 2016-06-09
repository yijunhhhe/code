# TODO: type solution here
class Cream:
    def __init__(self):
        self.value = "um"

class Coffee:
    def __init__(self):
        self.value = "Y"
    def __add__(self, other):
        if isinstance(other,Cream):
             return self.value + cream.value
        else:
            return "yack"




coffee = Coffee()
cream = Cream()
z="sugur"
print(coffee+cream)
print(coffee+z)