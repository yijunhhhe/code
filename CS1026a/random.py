inputFile = open("random.txt", "r",encoding="utf-8", errors='ignore')
wordDict = {}
for line in inputFile:
    lineList = line.split()
    for word in lineList:
        word = word.rstrip()
        if word not in wordDict:
            wordDict[word] = 1
        else :
            wordDict[word] += 1



value = list(wordDict.values())
value.sort()
value.reverse()
newValue = value[0:100]
print(newValue)
count = 0
for i in range(len(newValue)):
    if newValue[i] == newValue[i-1]:
        continue
    for key in wordDict:
        if wordDict[key] == newValue[i]:
            count += 1
            print(count,key)

