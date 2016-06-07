inputFile = open("rawdata.txt", "r")

dataDic = {}
letterDic = {}
letterSet = set()
key = []
value = []
number1 = ""
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N"
            "O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for line in inputFile:
    line = line.split("$")
    line[0] = line[0].strip("1234567890")
    line[0] = line[0].strip().upper()
    line[1] = line[1].strip()
    number=line[1].replace(",","")
    dataDic[line[0]]=int(number)

for i in range(len(key)):
    dataDic[key[i]] = value[i]

for letter in alphabet:
    for word in dataDic:
        if word.startswith(letter):
            letterSet.add(word)
    letterDic[letter] = letterSet
    letterSet = set()

countryName = input("country name: ")
if len(countryName) == 1:
    print(letterDic[countryName])
elif len(countryName) > 1:
    if countryName in dataDic:
        print(dataDic[countryName])
    else:
        print("Does not exiSt")
print(letterDic)
print(dataDic)





