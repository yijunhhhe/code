from countryGalore import *

def main():
    cc = CountryCatalogue('data.txt')
    cc.findCountry()
    cc.addCountry()
    cc.findCountry()
    cc.deleteCountry()
    cc.findCountry()
    cc.findCountryWithSmallestArea()
    cc.findCountryWithLargestPop()
    cc.setPopulationOfASelectedCountry()
    cc.filterCountriesByContinent()
    cc.filterCountriesByPopDensity()
    cc.findMostPopulousContinent()
    cc.printCountryCatalogue()
    cc.saveCountryCatalogue('output.txt')

main()