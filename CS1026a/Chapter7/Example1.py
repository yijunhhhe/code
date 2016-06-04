fileName = input('Please enter the file name')
if not fileName.endswith('.txt'):
    fileName = fileName + '.txt'
infile = open(fileName, 'r+')

count = 0
for num in infile:
    if int(num) < 0:
        count +=1

print('There are ', count, "number of negative numbers in the file")
#print('There are ', count, "number of negative numbers in the file", file=infile)