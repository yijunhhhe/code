total = 0
count = 0
inputStr = input("Enter value: ")
while inputStr != "":
    value = float(inputStr)
    total = total + value
    count = count + 1
    inputStr = input("Enter value: ")

if count > 0:
    average = total / count
else:
    average = 0.0