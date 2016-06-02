# Open and Close file
infile = open("input.txt","r")
outfile = open("output.txt","w")
infile.close()

# reading from a file
line = infile.readline()
while line != "":
    line = infile.readline()

# reading multiple lines from a file
line = infile.readline()
while line != "" :
    # Process the line.
    line = infile.readline()
# or
for line in infile:
    line = infile.readline()

# Writing to a File
outfile.write("Hello World!\n")
print("Hello World", file = outfile)
print("Hello World", end="", file = outfile)



