# Accepting a list as an argument
def sum(values) :
    total = 0
    for element in values :
        total = total + element
    return total

def multiply(values, factor) :
    for i in range(len(values)) :
        values[i] = values[i] * factor

# Modifying List Elements
def multiply(values, factor) :
    for i in range(len(values)) :
        values[i] = values[i] * factor

# Returning Lists from functions
def squares(n) :
    result = []
    for i in range(n) :
        result.append(i * i)
    return result

# Returning Multiple Values-------------
# Function definition
def readDate() :
    print("Enter a date:")
    month = int(input(" month: "))
    day = int(input(" day: "))
    year = int(input(" year: "))
    return (month, day, year) # Returns a tuple.
# Function call: assign entire value to a tuple
date = readDate()
# Function call: use tuple assignment:
(month, day, year)  = readDate()


