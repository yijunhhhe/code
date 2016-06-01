# Write a program that initializes a list with ten random integers
#  and then prints four
# lines of output, containing
# •	 Every element at an even index.
# •	 Every even element.
# •	 All elements in reverse order.
# •	 Only the first and last element.
from random import randint
random = []
for i in range(10):
    random.append(randint(1,10))
for i in range(0,10,2):
    print(random[i], end = " ")
print()
for i in random:
    if i % 2 == 0:
        print(i, end = " ")
print()
for i in range(len(random) - 1, -1, -1):
    print(random[i], end = " ")
print()
print(random[0],random[-1])


# Write a program that reads numbers and adds them to a list if they aren’t already
# contained in the list. When the list contains ten numbers, the program displays the
# contents and quits.

def addNumber(number, list):
    if number not in list:
        list.append(number)
    return list

listOfNumber = []
count = 0
while len(listOfNumber) < 10:
    number = int(input("number: "))
    listOfNumber = addNumber(number,listOfNumber)
print(listOfNumber)