# Write a program that asks the user for a file name and
# prints the number of charac­ters, words, and lines in that file.

# FUNCTIONS

# main
fileName = input("file name: ")
openFile = open("marry1.txt","r")
count = 0
countWord = 0
countCharacter = 0
countWord1 = 0
for line in openFile:
    count = count + 1
    countCharacter += len(line.strip())
    countWord1 += len(line.split(" "))
    line = line.split(" ")


    for element in line:
        if element.isalpha():
            countWord = countWord + 1
char = openFile.read(1)


openFile.close()
print(count)
print(countWord)
print(countWord1)
print(countCharacter)
