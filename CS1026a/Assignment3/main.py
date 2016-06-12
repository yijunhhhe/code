from Assignment3.countryGalore import *
def main():
    cc = CountryCatalogue('data.txt')

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