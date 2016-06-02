<<<<<<< HEAD
# Write a program that replaces each line of a file with its reverse.
# For example, if you run
# 	python reverse.py hello.py

# then the contents of hello.py are changed to 

# 	.margorp nohtyP tsrif yM #
# 	)"!dlroW ,olleH"(tnirp

# Of course, if you run Reverse twice on the same file, you get back the original file


# IMPORTS
from sys import argv

# FUNCTIONS

# main
def main():
	filename = argv[1]
	file = open(filename, "r")
	reversedFile = ""

	for line in file:
		reversedFile += line[::-1]

	file.close()
	file = open(filename, "w")
	file.write(reversedFile)
	file.close()
    
# PROGRAM RUN
if __name__ == "__main__":
    main()
=======
<<<<<<< HEAD
def sum(list):
    smallest = 100
    largest = 0
    evenList = []
    oddList = []
    for i in list:
        if i % 2 == 0:
            evenList.append(i)
        if i % 2 == 1:
            oddList.append(i)
    print(evenList)
    print(oddList)
    sum = min(oddList) + max(evenList)
    return sum

list = [1,3,5,6,8,43,3,9,87,56,44,33,2,45]
sum = sum(list)
print(sum)

=======
>>>>>>> origin/master
>>>>>>> origin/master
