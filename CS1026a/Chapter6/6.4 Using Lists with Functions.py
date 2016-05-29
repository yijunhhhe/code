# Accepting a list as an argument
def sum(values) :
    total = 0
    for element in values :
        total = total + element
    return total

def multiply(values, factor) :
    for i in range(len(values)) :
        values[i] = values[i] * factor