from Assignment3.countryGalore import *

catalogue = CountryCatalogue("data.txt")
catalogue.addCountry()
catalogue.deleteCountry()
catalogue.findCountry()
catalogue.filterCountriesByContinent()
catalogue.setPopulationOfASelectedCountry()
catalogue.findCountryWithLargestPop()
catalogue.findCountryWithSmallestArea()
catalogue.filterCountriesByPopDensity()
catalogue.findMostPopulousContinent()
catalogue.printCountryCatalogue()
catalogue.saveCountryCatalogue("outputfile.txt")