negatives = 0
inputStr = input("Enter value: ")
while inputStr != "":
    value = int(inputStr)
    if value < 0:
        negatives = negatives + 1
    inputStr  = input("Enter value: ")

print("There were", negatives, "negative values")