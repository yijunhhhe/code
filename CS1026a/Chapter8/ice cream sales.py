def readData(filename):
    salesData = {}
    flavor = []
    dataFile = open(filename, "r")
    for line in dataFile:
        line = line.split(":")
        flavor = line[0]
        salesData[flavor] = buildList(line)
    dataFile.close()
    return salesData

def buildList(data):
    list = []
    for i in (1,len(data)):
        list.append(float(data[i]))
    return list

def printData(salesData):
    numStore = 0
    for salesdata in salesData.value():
        if len(salesdata) > 0:
            numStore = len(salesdata)
    scoreTotal = [0] * numStore
    for key in sorted(salesData):
        print("%-15s" % flavor, end = "")
        flavorTotal = 0
        storeSales = salesData[key]
        for i in range(len(storeSales)):
            sale = storeSales[i]
            flavorTotal = flavorTotal + sale
            storeTotal[i] = storeTotal[i] + sale
            print("%10.2f" % sale, end = "")
        print("%15.2f" % flavorTotal)




