def isIncreasing(listOfPops):
    #Reads in a list of numbers and determines if the population is always increasing n
    localCopyOfList = list(listOfPops)
    if len(listOfPops) == 5:
        localCopyOfList.sort()
        if localCopyOfList == listOfPops:
            return True
        else:
            return False
    else:
        return False

#Country,1995,2000,2005,2010,2015
inf = open('Example4.txt', 'r')
outf = open('PopPrediction.txt', 'w')
newListOfAll = []
nameOfCountries = []
num = 0
inf.readline()
for line in inf:
    contents = line.split(',')
    newListOfAll.append([])
    for i in range(len(contents)):
        if( i == 0):
            nameOfCountries.append(contents[i])
        else:
            newListOfAll[num].append(int(contents[i]))
    num = num+1

#JUST FOR CHECKING
print(newListOfAll)
print(nameOfCountries)

for i in range(len(newListOfAll)):
    country = newListOfAll[i]
    if isIncreasing(country):
        total = 0
        for j in range(len(country)-1):
            total = total + (country[j+1] - country[j])
        average = total/4
        #rounded up the new population and converted it to int so that we dont have decimals in the output file
        pop2020= int(round(country[len(country)-1]+average,0))
        print('The new population for country', nameOfCountries[i], pop2020, file=outf )


