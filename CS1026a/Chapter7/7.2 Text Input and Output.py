# Iterating over the Lines of a File
infile = open("hello.txt","r")
for line in infile:
    print(line)
# to remove the newline character
line = line.rstrip()
line = line.rstrip(".?")
# remove the left side character
line = line.lstrip()
# remove both side
line = line.strip()

#------------------------
# Reading Words
line = "what asdf asdfdf d fd fd  "
wordList = line.split(" ",2)
for word in wordList:
    print(word)
# other
line.split()
line.split("")
line.rsplit("",2)

#------------------
# Reading Characters
inputFile = open("hello.txt","r")
char = inputFile.read(1)


#------------------
# Reading Records
line = infile.readline()
while line != "":
    countryName = line.rstrip()
    line = infile.readline()
    population = int(line)
    line = infile.readline()

#-------------------------
# File Operations
#f = open(filename, mode)
#f.close()
#string = f.readline()
#string = f.read(num)
#string = f.read()
#f.write(string)

