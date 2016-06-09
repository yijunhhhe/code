# TODO: type solution here
class Dinosaur:
    def __init__(self):
        self._type = ""

    def setType(self,type):
        self._type = type

    def getType(self):
        return self._type




d1= Dinosaur()
d2= Dinosaur()
d3 = Dinosaur()

d1.setType("T-Rex")
d2.setType("Velociraptor")
d3.setType("Stegosaurus")

print(d1.getType(),d2.getType(),d3.getType())
