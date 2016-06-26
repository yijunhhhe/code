class Country :
   def __init__(self, name, pop, area, continent) :
      self._name = name
      self._population = pop
      self._area = area
      self._continent = continent

   def __repr__(self):
      return self._name + " in " +self._continent

   def setPopulation(self, pop):
      self._population = pop

   def getName(self) :
      return self._name

   def getArea(self) :
      return self._area

   def getPopulation(self) :
      return self._population

   def getContinent(self):
      return self._continent

   def getPopDensity(self) :
      return self.getPopulation() / self.getArea()

   def save(self, outf) :
      #print(self._name, self._population, self._area, self._continent, file=outf)
      outf.write("%s|%s|%d|%d\n" % (self._name, self._continent, self._population, self.getPopulation() / self.getArea()))

   def __cmp__(self, other):
      if hasattr(other, '_name'):
         return self._name.__cmp__(other._name)

   def __getitem__(self, item):
      return self._population

class CountryCatalogue:
   def __init__(self, filename):

      self._cSet =set()
      self._catalogue = dict()
      self._cDictionary = dict()

      inf = open("continent.txt", "r")
      inf.readline()
      for line in inf:
         parts = line.split(",")
         self._cDictionary[parts[0]] = parts[1].strip()

      inf.close()

      inf = open("data.txt", "r")
      inf.readline()
      for line in inf:
         parts = line.split("|")
         name = parts[0]
         pop = int(parts[1].replace(",", ""))
         area = float(parts[2].replace(",", ""))
         country = Country(name, pop, area,self._cDictionary[name])
         self._catalogue[name] = country
         self._cSet.add(country)


   def filterCountriesByContinent(self):
      print('************************FILTER COUNTRIES BY CONTINENT************************')
      continent = input("Enter the continent: ")
      for country in self._catalogue.keys():
         if self._catalogue[country].getContinent() == continent :
             print(self._catalogue[country].getName())

      #for country in self._cSet:
       #  if country.getContinent() == continent :
        #     print(country.getName())

   def printCountryCatalogue(self):
      print('************************PRINT COUNTRY CATALOGUE************************')
      #countries = sorted(self._cSet, key=Country.getName)
      #for country in countries:
       #     print(country)

      for country in sorted(self._catalogue.values(), key=Country.getName):
            print(country)

   def findCountry(self):
      print('************************FIND COUNTRY************************')
      countryName = input('Enter the name of the country: ')
      if countryName in self._catalogue:
         print('Name: ',self._catalogue[countryName].getName())
         print('Continent: ',self._catalogue[countryName].getContinent())
         print('Area: ',self._catalogue[countryName].getArea())
         print('Population: ',self._catalogue[countryName].getPopulation())
         print('Population Density: ',self._catalogue[countryName].getPopDensity())
      else:
         print(countryName, "is not in our catalogue")

  #    for country in self._cSet:
   #      if country.getName() == countryName:
    #        print(country)

   def deleteCountry(self):
      print('************************DELETE COUNTRY************************')
      countryName =input('Enter the name of country you would like to delete: ')
      if countryName in self._catalogue:
         self._catalogue.pop(countryName)
         print('The country has been removed')
      else:
         print('The country does not exist in the catalogue')

   def addCountry(self):
      print("************************ADD COUNTRY ************************")
      print('You want to add a new country ')
      notValid = True
      while notValid:
         name = input("Enter the country's name: ")
         if not name in self._catalogue.keys():
            notValid = False
         else:
            print('Please enter a unique name, a country with that name already exists')
      #check to see if the country is already in the db.
      #check to see if we have a continent for that country
      area= float(input('Enter the area :'))
      pop = int(input('Enter the population of the country: '))
      cont = input('Enter a continent for the country: ')
      c = Country(name, area, pop, cont)
      self._cDictionary[name] = cont
      self._catalogue[name] = c
      self._cSet.add(c)
      print('The country has been added successfully')

   def setPopulationOfASelectedCountry(self):
      print('************************ SET POPULATION OF A SELECTED COUNTRY')
      #Assume valid input
      name = input("Enter the name of the country you would like to change its population: ")
      pop = int(input('Enter the new population of the country, must be an integer: '))
      #for c in self._cSet:
       #  if c.getName() == name:
        #    c.setPopulation(pop)
         #   print("The population of ",c.getName(), " has been updated to ", c.getPopulation())
          #  print('The new population density is ', c.getPopDensity())

      if name in self._catalogue:
         self._catalogue[name].setPopulation(pop)
         print("The population of ",self._catalogue[name].getName(), " has been updated to ", self._catalogue[name].getPopulation())
         print('The new population density is ', self._catalogue[name].getPopDensity())


   def saveCountryCatalogue(self, filename):
      print('************************SAVE COUNTRY CATALOGUE TO FILE ************************')
      outf = open(filename, "w")
      for country in self._catalogue :
         self._catalogue[country].save(outf)
      print("The catalogue has been saved to ", filename)

      outf.close()

   def findCountryWithLargestPop(self):
      print('************************FIND COUNTRY WITH LARGEST POPULATION ************************')
      # Find and display the country with the largest population.
      #countries = sorted(self._cSet, key=Country.getPopulation)
      #print("Largest Population:", countries[-1].getName())

      x = sorted(self._catalogue.values(), key=Country.getPopulation)
      print("Largest Population:", x[-1].getName())

   def findCountryWithSmallestArea(self):
      print('************************FIND COUNTRY WITH SMALLEST AREA ************************')
      # Find and display the country with the largest area.
      #countries = sorted(self._cSet, key=Country.getArea)
      #print("Largest Area:", countries[0].getName())
      x = sorted(self._catalogue.values(), key=Country.getArea)
      print("Country with smallest Area:", x[0].getName())

   def filterCountriesByPopDensity(self):
      print('************************FILTER COUNTRIES BY POPULATION DENSITY************************')
      lBound = int(input('Enter the lower bound of the range'))
      UBound = int(input('Enter the upper bound of the range'))
      for c in self._catalogue.values():
         if  lBound < c.getPopDensity() < UBound:
            print(c.getName(), ' has a population density of ', c.getPopDensity())


   def findMostPopulousContinent(self):
      print('************************FIND MOST POPULOUS CONTINENT ************************')
      #Add up all the populations for each continent and return the continent with the biggest population
      dictOfCont = dict()
      listOfCont = set()
      for c in self._catalogue.values():
         listOfCont.add(c.getContinent())
      #print(listOfCont)
      for cont in listOfCont:
         dictOfCont[cont] = list()

      for country in self._catalogue.values():
         dictOfCont[country.getContinent()].append(country.getPopulation())

     # print(dictOfCont)

      dictOfPopulation = dict()
      for co in dictOfCont.keys():
         dictOfPopulation[co] = sum(dictOfCont[co])

    #  print(dictOfPopulation)

      max = 0
      name = ""
      for c in dictOfPopulation.keys():
          if dictOfPopulation[c] > max:
            max = dictOfPopulation[c]
            name = c
      print('The most populous continent in our catalogue is', name, 'with', dictOfPopulation[name], ' people')
