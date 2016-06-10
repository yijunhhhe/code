#For the exercise you will use data from the CIA’s website and create two dictionaries. Write a program that reads the data in rawdata.txt into a dictionary whose keys are country names and whose values are per capita incomes. Also create another dictionary whose keys are letters A- Z and whose values are sets of country names. Convert the country names to all uppercase for both dictionaries Your program should prompt the user to enter country names and print the corresponding values.
# If the user enters a string with only one letter (like A) print all the countries that begin with that letter,
# If the user enters a string that contains more than one letter, print the corresponding value for that country if it exists or print “Does not exist” if invalid.  Stop when the user enters quit.

inputFile = open("rawdata.txt", "r")

dataDic = {}
letterDic = {}
letterSet = set()

number1 = ""
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N"
            "O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for line in inputFile:
    line = line.split("\t")
    line[2] = line[2].strip('\n')
    line[2] = line[2].lstrip("$")
    line[2] = line[2].strip()
    line[2] = int(line[2].replace(',',""))   # Important! When strip the comma in the number
    dataDic[line[1]] = line[2]

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





