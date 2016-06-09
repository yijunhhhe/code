class Country:
    def __init__(self, name, pop, area, continent):
        self._name = name
        self._pop = pop
        self._area = area
        self._continent = continent
    def getName(self):
        return self._name
    def getPopulation(self):
        return self._pop
    def getArea(self):
        return self._area
    def getContinent(self):
        return self._continent
    def getPopDensity(self):
        popDensity = self._pop / self._area
        return popDensity
    def setPopulation(self,pop):
        self._pop = pop
    def __repr__(self):
        return (self._name + " in " + self._continent)
    def save(self):
        outputFile = ("outputfile.txt", "w")
        popDensity = self.getPopDensity()
        outputFile.write("{}|{}|{}|{}|{}".format(self._name, self._continent, self._pop, popDensity))


class CountryCatalogue:
    def __init__(self, filename):
        file = open(filename, "r")
        self._cDic = {}
        self._catalogue = set()
        for line in file:
            line = file.rstrip().split(",")
            if line[0] == "Country":
                continue
            self._cDic[line[0]] = line[1]
            self._catalogue.add(line[0])

    def addCountry(self, name, population, area, continent):
        if name in self._cDic:
            



