# Raising Exceptions
if amount > balance:
    raise ValueError("Amount exceed balance")
balance = balance - amount


# Handling Exceptions
try:
    infile = open("hello.txt","r")
    line = infile.readline()
    process(line)
except IOError :
    print("Could not open the input file")
except Exception as exceptObj:
    print("Error:", str(exceptObj))


#The finaly Calause
outfile = open(filename, "w")
try :
    writeData(outfile)
#    . . .
finally :
    outfile.close()

