from countryGalore import *

def main():
    cc = CountryCatalogue('data.txt')
    cc.findCountry()
    cc.findCountry()
    cc.addCountry()
    cc.findCountry()
    cc.deleteCountry()
    cc.printCountryCatalogue()
    cc.findCountryWithSmallestArea()
    cc.findCountryWithLargestPop()
    cc.setPopulationOfASelectedCountry()
    cc.findCountry()
    cc.filterCountriesByContinent()
    cc.filterCountriesByPopDensity()
    cc.findMostPopulousContinent()
    cc.printCountryCatalogue()
    cc.saveCountryCatalogue('output.txt')

main()