largest = int(input("Enter a value: "))
inputStr = input("Enter a value: ")
while inputStr != "":
    value = int(inputStr)
    if value > largest:
        largest = value
    inputStr = input("Enter a value: ")

smallest = int(input("Enter a value: "))
inputStr = input("Enter a value: ")
while inputStr != 0:
    value = int(inputStr)
    if value < smallest:
        value = smallest
    inputStr = input("Enter a value: ")