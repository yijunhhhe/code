#1	Toronto	Ontario	city	630.21	2,615,060	2,503,281	2,481,494	2,385,421	4.5	9.6

class City:
    def __init__(self, name, province, citytype, area, population):
        self._name = name
        self._cityType = citytype
        self._population = population
        self._area = area
        self._province = province

    def getPopulation(self):
        return self._population

    def getName(self):
        return self._name

    def getArea(self):
        return self._area

    def __repr__(self):
        return self._name + "-"+self._cityType + "-" + self._province + '-'+ str(self._area) + '-' +str(self._population)
#JUST TO SEE IF THE CLASS WORKS
c1 = City('London','Ontario' ,'city', 456.72, 4560643)
print(c1)
print(c1.getPopulation())

#CREATE DICTIONARY
popDictionary = {}
inf = open("pop3.txt", "r")
for line in inf:
   parts = line.strip().split("\t")
   #remove commas
   parts[5] = int(parts[5].replace(',',''))
   parts[4] = float(parts[4].replace(',',''))
   # Add the city to the dictionary.
   #ALT 1
   popDictionary[parts[1]] = City(parts[1], parts[2], parts[3], parts[4], parts[5])
   #you can do this in two parts. first create a city and then add the city to the dictionary
   #ALT 2
   c = City(parts[1], parts[2], parts[3], parts[4], parts[5])
   popDictionary[c.getName()] = c

#NOW THAT ALL THE DATA IS ADDED WE CAN WRITE FUNCTIONS THAT USE THE DICTIONARY
def printAllInformation():
    for city in popDictionary:
        print(popDictionary[city])

def findCityWithLargestArea():
    y = sorted(popDictionary.values(), key = City.getArea)
    return y[-1]  #this returns the whole City if you just want the name then call getName

printAllInformation()
print(findCityWithLargestArea())