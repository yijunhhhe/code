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
    line = line.split("$")
    line[0] = line[0].strip("1234567890")
    line[0] = line[0].strip().upper()
    line[1] = line[1].strip()
    number=line[1].replace(",","")
    dataDic[line[0]]=int(number)

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





