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
    def save(self, outputFile):
        popDensity = self.getPopDensity()
        outputFile.write("{}|{}|{}|{}\n".format(self._name, self._continent, self._pop, popDensity))

class CountryCatalogue:
    def __init__(self, filename):
        file = open("continent.txt","r")
        datafile = open(filename, "r")
        self._cDic = {}
        self._catalogue = set()
        for line in file:
            line = line.rstrip().split(",")
            if line[0] == "Country":
                continue
            self._cDic[line[0]] = line[1]
        for line in datafile:
            line = line.rstrip().split("|")
            if line[0] == "Country":
                continue
            line[1] = int(line[1].replace(",",""))
            line[2] = float(line[2].replace(",",""))
            country = Country(line[0], line[1], line[2], self._cDic[line[0]])
            self._catalogue.add(country)

    def addCountry(self):
        name = input("Please enter the country name you want to add: ")
        while name in self._cDic:
            print("This country has already existed, please reenter a new one")
            name = input("Please enter the country name: ")
        population = int(input("Please enter the population: "))
        continent = input("Please enter the continent: ")
        area = float(input("Please enter the area: "))
        country = Country(name, population, area, continent)
        self._catalogue.add(country)
        self._cDic[country.getName()] = continent
        if country in self._catalogue:
            print("The country has been successfully added to catalogue")
        else:
            print("The country has not been added to catalogue")

    def deleteCountry(self):
        name = input("Please enter the country you want to delete: ")
        isDelete = False
        for country in self._catalogue:
            if name == country.getName():
                self._catalogue.discard(country)
                self._cDic.pop(country.getName())
                if country not in self._catalogue:
                    isDelete = True
                    print("The country has been deleted")
                break
        if isDelete == False:
            print("The country has not been deleted because it doesn't exist")

    def saveCountryCatalogue(self, filename):
        outputFile = open(filename, "w")
        catalogue = sorted(self._catalogue, key = Country.getName)
        for country in catalogue:
            country.save(outputFile)
        print("Catalogue has been stored in output.txt")
        outputFile.close()

    def findCountry(self):
        name = input("Please enter the country name you want to find: ")
        isFind = False
        for country in self._catalogue:
            if name == country.getName():
                print(country._name, "Population:",country._pop, "Area:", country._area, "Continenet:", country._continent)
                isFind = True
                break
        if isFind == False:
            print("The country you find does not exist")

    def filterCountriesByContinent(self):
        continenet = input("Please enter the continent name that you want to filter: ")
        for country in self._catalogue:
            if country.getContinent() == continenet:
                print(country._name)

    def printCountryCatalogue(self):
        catalogue = sorted(self._catalogue, key = Country.getName)
        for country in catalogue:
            print(country)

    def setPopulationOfASelectedCountry(self):
        countryName = input("Please enter the country name that you want to set a new population : ")
        newPopulation = int(input("Please enter the new population: "))
        for country in self._catalogue:
            if countryName == country.getName():
                country.setPopulation(newPopulation)
                print(country.getName(), country.getPopulation())

    def findCountryWithLargestPop(self):
        largest = 0
        for country in self._catalogue:
            if country.getPopulation() > largest:
                largest = country.getPopulation()
                largestName = country.getName()
        print("{} have the largest population {} among all the countries".format(largestName,largest))

    def findCountryWithSmallestArea(self):
        smallest = 10000000000000000
        smallestName = ""
        for country in self._catalogue:
            if country.getArea() < smallest:
                smallest = country.getArea()
                smallestName = country.getName()
        print("{} have the smallest area {} among all the countries".format(smallestName,smallest))

    def filterCountriesByPopDensity(self):
        lowerBound = int(input("Please enter the lower bound of population density range: "))
        upperBound = int(input("Please enter the upper bound of population density range: "))
        for country in self._catalogue:
            if country.getPopulation() > lowerBound and country.getPopulation() < upperBound:
                print(country.getName())

    def findMostPopulousContinent(self):
        asia = []
        northA = []
        southA = []
        africa = []
        europe = []
        for country in self._catalogue:
            if country.getContinent() == "Asia":
                asia.append(country.getPopulation())
            elif country.getContinent() == "North America":
                northA.append(country.getPopulation())
            elif country.getContinent() == "South America":
                southA.append(country.getPopulation())
            elif country.getContinent() == "Africa":
                africa.append(country.getPopulation())
            else:
                europe.append(country.getPopulation())
        mostPopularContinent = [asia, "Asia", northA, "North America", southA, "South America", africa, "Africa", europe, "Europe"]
        largest = 0
        for i in range(0,len(mostPopularContinent),2):
            if sum(mostPopularContinent[i]) > largest:
                largest = sum(mostPopularContinent[i])
                name = mostPopularContinent[i+1]
        print("The most popular continent is", name, "with", largest, "people")










