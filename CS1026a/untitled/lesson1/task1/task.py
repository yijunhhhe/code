# TODO: type solution here
class Fruit:
    def __init__(self, shape, colour):
        self._shape = shape
        self._colour = colour

    def canBePhone(self):
        return "fruits can't be phones"

class Banana(Fruit):
    def __init__(self, shape, colour):
        super().__init__(shape, colour)

    def canBePhone(self):
        return "Ring ring ring ring ring ring ring banana phone\nBoop-boo-ba-doo-ba-doop"

banana = Fruit("triangle", "yellow")
print(banana.canBePhone())
banana = Banana("square", "yellow")
print(banana.canBePhone())

