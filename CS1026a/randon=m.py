def combineWord(first, second, eachLine):
    if first in eachLine:
        index = eachLine.index(first)
        eachLine.remove(second)
        eachLine[index] = first + " " + second


popFile = open("pop3.txt", "r")
cityDic = {}
for i in range(1,6):
    cityDic[i] = list()
for eachLine in popFile:
    eachLine = eachLine.split()
    combineWord("British", "Columbia", eachLine)
    if "Quebec" in eachLine:
        index = eachLine.index("Quebec")
        eachLine.remove("Quebec")
        eachLine[index] = "Quebec" + " " + "City"

    combineWord("Nova", "Scotia", eachLine)
    combineWord("regional", "municipality", eachLine)
    print(eachLine)
    for i in range(1,6):
        cityDic[i].append(eachLine[i])
print(cityDic, end= "\n")

