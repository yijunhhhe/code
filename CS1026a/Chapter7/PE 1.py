# Write a program that carries out the following tasks:
#     Open a file with the name hello.txt.
#     Store the message “Hello, World!” in the file.
#     Close the file.
#     Open the same file again.
#     Read the message into a string variable and print it.

outFile = open("Hello.txt","w")
outFile.write("Hello,World!")
outFile.close()
outFile = open("Hello.txt","r")
line = outFile.readline()
print(line)

# Write a program that reads a file containing text. Read each line and send it to the
# output file, preceded by line numbers. If the input file is
#     Mary had a little lamb
#     Whose fleece was white as snow.
#     And everywhere that Mary went,
#     The lamb was sure to go!

# then the program produces the output file
#     /* 1 */ Mary had a little lamb
#     /* 2 /* Whose fleece was white as snow.
#     /* 3 /* And everywhere that Mary went,
#     /* 4 /* The lamb was sure to go!

file = open("marry.txt","r")
outFile = open("marry1.txt","w")
lineNumber = 1
for line in file:
    outFile.write("/* %s */ %s" % (lineNumber, line))
    lineNumber += 1
file.close()
outFile.close()
