from Assignment3.countryGalore import *

canada = Country("Canada", 4300, 20000, "North America")
area = canada.getArea()
name = canada.getName()
population = canada.getPopulation()
continent = canada.getContinent()
popDensity = canada.getPopDensity()
print(area, name, population, continent, popDensity)
canada.setPopulation(10000)
population = canada.getPopulation()
print(population)

catalogue = CountryCatalogue("data.txt")
catalogue.findCountry()
catalogue.saveCountryCatalogue("outputfile.txt")




