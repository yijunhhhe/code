#THIS FILE HAS A CLASS AS WELL AS HOW TO SORT SETS AND DICTIONARIES OF CLASSES
class Fruit:
    def __init__(self, num, name):
        self._size = num
        self._type = name

    def getSize(self):
        return self._size

    def getType(self):
        return self._type

    def __repr__(self):
        return self._type + " " +str(self._size)

f1 = Fruit(10, 'Mango')
f2 = Fruit(20, 'Pear')
f3 = Fruit(30, 'Grapes')

myDictionary = {}
myDictionary[f1.getType()] = f1
myDictionary[f2.getType()] = f2
myDictionary[f3.getType()] = f3

print(myDictionary)

for f in myDictionary:
    print(f)
    print(myDictionary[f])
    print(myDictionary[f].getSize())

x = sorted(myDictionary.values(), key=Fruit.getSize)
print(x[-1])

mySet = {f1,f2,f3}
print(mySet)
y = sorted(mySet, key=Fruit.getSize)
print(y[-1])


