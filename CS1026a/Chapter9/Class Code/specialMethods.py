#HOW WE OVERLOAD DIFFERNT OPERATORS
class Computer:
    def __init__(self, n, p):
        self._name = n
        self._price = p

    def __repr__(self):
        return 'I am a computer, my type is ' + self._name

    def __add__(self, other):
        if(isinstance(other, Computer)):
            return 'I added your computers'
        else:
            return 'Dude i am not killing your computer'

c1 = Computer('Lenovo', 1234)
print(c1)

c2 = Computer('Mac', 120034)
print(c2)

print(c1 + c2)

print( c1 + 5)
