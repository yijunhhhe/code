# Student: Yijun He
# Student Number: 250892341
# This program define a Country class which can create a country object including
# name, population, continent, area and a Country catalogue class which can create
# catalogue object including different countries object

# This module defines the Country class
## A country with name, population, area and continent
class Country:
    ## Constructs a country with name, population, area, continent
    # @param name the country name
    # @param pop the country's population
    # @param area the area of the country
    # @param continent the continentof the country
    def __init__(self, name, pop, area, continent):
        self._name = name
        self._pop = pop
        self._area = area
        self._continent = continent

    # Gets the name of the country
    def getName(self):
        return self._name

    # Gets the population of the country
    def getPopulation(self):
        return self._pop

    # Gets the area of the country
    def getArea(self):
        return self._area

    # Gets the continent of the country
    def getContinent(self):
        return self._continent

    # get the population density of the country
    def getPopDensity(self):
        popDensity = self._pop / self._area
        return popDensity

    ## set a new population for the country
	# @param pop new population for the country
    def setPopulation(self,pop):
        self._pop = pop

    ## Gets a string representation of the country
    def __repr__(self):
        return self._name + " in " + self._continent

    ## Saves the data to a output file
	# @param outputFile a input file object
    def save(self, outputFile):
        popDensity = self.getPopDensity()
        outputFile.write("{}|{}|{}|{}\n".format(self._name, self._continent, self._pop, popDensity))

# This module define a country catalogue class
# A catalogue storing different countries information 	
class CountryCatalogue:

    ## Constructs a catalogue with a set storing country and a dictionary storing continenet value
	# param filename input file name 
    def __init__(self, filename):
        continentFile = open("continent.txt","r")
        datafile = open(filename, "r")
        self._cDic = {}
        self._catalogue = set()
        # Stores country and corresponding value into dictionary
        for line in continentFile:
            line = line.rstrip().split(",")
            # skip the first line when reading each line
            if line[0] == "Country":
                continue
            self._cDic[line[0]] = line[1]
        # Stores country object into a set
        for line in datafile:
            line = line.rstrip().split("|")
            # skip the first line
            if line[0] == "Country":
                continue
            line[1] = int(line[1].replace(",",""))
            line[2] = float(line[2].replace(",",""))
            country = Country(line[0], line[1], line[2], self._cDic[line[0]])
            self._catalogue.add(country)

    # Adds a country to country set
    def addCountry(self):
        name = input("Please enter the country name you want to add: ")
        # Keeps getting input from users if the country name exists
        while name in self._cDic:
            print("This country has already existed, please reenter a new one")
            name = input("Please enter the country name: ")
        population = int(input("Please enter the population: "))
        continent = input("Please enter the continent: ")
        area = float(input("Please enter the area: "))
        country = Country(name, population, area, continent)
        self._catalogue.add(country)
        self._cDic[country.getName()] = continent
        # Whether adding is successful or not, print the message for users
        if country in self._catalogue:
            print("The country has been successfully added to catalogue")
        else:
            print("The country has not been added to catalogue")
	
    # Deletes country from country set
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
        # If country has not been deleted
        if isDelete == False:
            print("The country has not been deleted because it doesn't exist")
	
    # Saves the country catalogue to a file
    def saveCountryCatalogue(self, filename):
        outputFile = open(filename, "w")
        catalogue = sorted(self._catalogue, key = Country.getName)
        for country in catalogue:
            country.save(outputFile)
        print("Catalogue has been stored in output.txt")
        outputFile.close()
	
    # Finds the country that users input
    def findCountry(self):
        name = input("Please enter the country name you want to find: ")
        isFind = False
        for country in self._catalogue:
            if name == country.getName():
                print(country.getName(), "Population:",country.getPopulation(), "Area:", country.getArea(), "Continenet:", country.getContinent())
                isFind = True
                break
        # if the country does not exist
        if isFind == False:
            print("The country you find does not exist")
	
    # Filters the country by continenet
    def filterCountriesByContinent(self):
        continent = input("Please enter the continent name that you want to filter: ")
        for country in self._catalogue:
            if country.getContinent() == continent:
                print(country._name)
				
    # Prints the country catalogue
    def printCountryCatalogue(self):
        catalogue = sorted(self._catalogue, key = Country.getName)
        for country in catalogue:
            print(country)
	
    # Sets a new population for seleted country
    def setPopulationOfASelectedCountry(self):
        countryName = input("Please enter the country name that you want to set a new population : ")
        for country in self._catalogue:
            if countryName == country.getName():
                newPopulation = int(input("Please enter the new population: "))
                country.setPopulation(newPopulation)
                print(country.getName(), "New population:", country.getPopulation())
	
    # Finds the country with largest population
    def findCountryWithLargestPop(self):
        largest = 0
        for country in self._catalogue:
            if country.getPopulation() > largest:
                largest = country.getPopulation()
                largestName = country.getName()
        print("{} have the largest population {} among all the countries".format(largestName,largest))
	
    # Finds the country with smallest area
    def findCountryWithSmallestArea(self):
        smallest = 10000000000000000
        smallestName = ""
        for country in self._catalogue:
            if country.getArea() < smallest:
                smallest = country.getArea()
                smallestName = country.getName()
        print("{} have the smallest area {} among all the countries".format(smallestName,smallest))
	
    # Filters countries by population density
    def filterCountriesByPopDensity(self):
        lowerBound = int(input("Please enter the lower bound of population density range: "))
        upperBound = int(input("Please enter the upper bound of population density range: "))
        for country in self._catalogue:
            if country.getPopulation() > lowerBound and country.getPopulation() < upperBound:
                print(country.getName())
	
    # Finds most popular continenet
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










