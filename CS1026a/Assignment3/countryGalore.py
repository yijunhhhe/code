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
        if "," in str(self._pop):
            self._pop = str(self._pop).replace(",","")
        if "," in str(self._area):
            self._area = str(self._area).replace(",","")
        popDensity = float(self._pop) / float(self._area)
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
            country = Country(line[0], line[1], line[2], self._cDic[line[0]])
            self._catalogue.add(country)

    def addCountry(self):
        name = input("Please enter the country name you want to add: ")
        while name in self._cDic:
            print("This country has already existed, please reenter a new one")
            name = input("Please enter the country name: ")
        population = int(input("Please enter the population: "))
        continent = input("Please enter the continenet: ")
        area = float(input("Please enter the area: "))
        country = Country(name, population, area, continent)
        self._catalogue.add(country)
        self._cDic[country] = continent
        if country in self._catalogue:
            print("The country has been successfully added to catalogue")
        else:
            print("The country has not been added to catalogue")

    def deleteCountry(self):
        name = input("Please enter the country you want to delete: ")
        Isdelete = False
        for country in self._catalogue:
            if name == country.getName():
                self._catalogue.discard(country)
                self._cDic.pop(country)
                Isdelete = True
                print("The country has been deleted")
                break
        if Isdelete == False:
            print("The country has not been deleted because it doesn't exist")

    def saveCountryCatalogue(self, filename):
        outputFile = open(filename, "w")
        catalogue = sorted(self._catalogue, key = Country.getName)
        for country in catalogue:
            country.save(outputFile)
        print("Catalogue has been stored in outpuFile.txt")
        outputFile.close()

    def findCountry(self):
        name = input("Please enter the country name you want to find: ")
        Isfind = False
        for country in self._catalogue:
            if name == country.getName():
                print(country._name, "Population:",country._pop, "Area:", country._area, "Continenet:", country._continent)
                Isfind =True
                break
        if Isfind == False:
            print("The country you find does not exist")


    def filterCountriesByContinent(self):
        continenet = input("Please enter the continent name that you want to filter: ")
        for country in self._catalogue:
            if country._continent == continenet:
                print(country._name)

    def printCountryCatalogue(self):
        catalogue = sorted(self._catalogue, key = Country.getName)
        for country in catalogue:
            print(country)

    def setPopulationOfASelectedCountry(self):
        countryName = input("Please enter the country name that you want to set a new population : ")
        newPopulation = int(input("Please enter the new population: "))
        for country in self._catalogue:
            if countryName == country._name:
                country._pop = newPopulation
                print(country._name, country._pop)

    def findCountryWithLargestPop(self):
        largest = 0
        for country in self._catalogue:
            country._pop = str(country._pop).replace(",","")
            if int(country._pop) > largest:
                largest = int(country._pop)
                largestName = country._name
        print("{} have the largest population {} among all the countries".format(largestName,largest))

    def findCountryWithSmallestArea(self):
        smallest = 10000000000000
        smallestName = ""
        for country in self._catalogue:
            country._area = str(country._area).replace(",","")
            if float(country._area) < smallest:
                smallest = float(country._area)
                smallestName = country._name
        print("{} have the smallest area {} among all the countries".format(smallestName,smallest))

    def filterCountriesByPopDensity(self):
        lowerBound = int(input("Please enter the lower bound of population density range: "))
        upperBound = int(input("Please enter the upper bound of population density range: "))
        for country in self._catalogue:
            country._pop = int(str(country._pop).replace(",",""))
            if country._pop > lowerBound and country._pop < upperBound:
                print(country._name)

    def findMostPopulousContinent(self):
        asia = []
        northA = []
        southA = []
        africa = []
        europe = []
        for country in self._catalogue:
            if country._continent == "Asia":
                asia.append(int(str(country._pop).replace(",","")))
            elif country._continent == "North America":
                northA.append(int(str(country._pop).replace(",","")))
            elif country._continent == "South America":
                southA.append(int(str(country._pop).replace(",","")))
            elif country._continent == "Africa":
                africa.append(int(str(country._pop).replace(",","")))
            else:
                europe.append(int(str(country._pop).replace(",","")))
        mostPopularContinent = [asia, "Asia", northA, "North America", southA, "South America", africa, "Africa", europe, "Europe"]
        largest = 0
        for i in range(0,len(mostPopularContinent),2):
            if sum(mostPopularContinent[i]) > largest:
                largest = sum(mostPopularContinent[i])
                name = mostPopularContinent[i+1]
        print("The most popular continent is", name, "with", largest, "people")










