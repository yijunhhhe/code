# Student: Yijun He
# Student Number: 250892341
# This program test country and countryCatalogue class

from Assignment3.countryGalore import *

# This function test the country class
def testCountryClass():
    output = open("outputCountryClass.txt", "w")
    canada = Country("Canada", 4300, 20000, "North America")
    # Gets name, area, population, continent, pop density and print them
    # Tests get method
    area = canada.getArea()
    name = canada.getName()
    population = canada.getPopulation()
    continent = canada.getContinent()
    popDensity = canada.getPopDensity()
    print(name, "Area: {}. Population: {}. Continent: {}. Population desity: {}"
          .format(area, population, continent, popDensity))
    # Tests setPopulation method
    canada.setPopulation(10000)
    population = canada.getPopulation()
    print("New Population:", population)
    # Tests print repr method
    print(canada)
    # Tests save method
    canada.save(output)
    output.close()

# This function test the countryCatalogue class
def testCountryGaloreClass():
    catalogue = CountryCatalogue('data.txt')
    catalogue.findCountry()
    catalogue.addCountry()
    catalogue.findCountry()
    catalogue.deleteCountry()
    catalogue.findCountry()
    catalogue.findCountryWithSmallestArea()
    catalogue.findCountryWithLargestPop()
    catalogue.setPopulationOfASelectedCountry()
    catalogue.filterCountriesByContinent()
    catalogue.filterCountriesByPopDensity()
    catalogue.findMostPopulousContinent()
    catalogue.printCountryCatalogue()
    catalogue.saveCountryCatalogue('output.txt')

testCountryClass()
testCountryGaloreClass()



