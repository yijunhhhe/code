from countryGalore import *
if "British" in eachLine:
        indexOfBrit = eachLine.index("British")
        eachLine.remove("Columbia")
        eachLine[indexOfBrit] = "British Columbia"
    if "Quebec" in eachLine:
        indexOfQuebec = eachLine.index("Quebec")
        eachLine.remove("City")
        eachLine[indexOfQuebec] = "Quebec City"
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