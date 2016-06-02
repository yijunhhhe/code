# Filling
values = []
n = 10
for i in range(n):
    values.append(i * i)

# Combing List Elements
result = 0.0
for element in values:          # NUMBER
    result = result + element

result = ""
for element in friends:         # STRING
    result = result + element

# Element Separators
result = ""
for i in range(len(friends)) :   # For String
    if i > 0 :
        result = result + ", "
    result = result + friends[i]

for i in range(len(values)):       # For Number
    if i > 0:
        print("|", end = "")
    print(values[i], end = "")
print()

str(values)  # Convert a list to a string

# Maximum and Minimum
largest = values[0]
for i in range(1, len(values)) :   # Number Maximum
    if values[i] > largest :
        largest = values[i]
names = ["Ann", "Charlotte", "Zachary", "Bill"]
longest = names[0]
for i in range(1, len(names)) :     # String length maximum
    if len(names[i]) > len(longest) :
        longest = names[i]

# Linear Search
searchedValue = 100
if searchedValue in values :
    pos = values.index(searchedValue)
    print("Found at position:", pos)
else :
    print("Not found")

# Collecting and Counting Matches
limit = 100
result = []
for element in values :
    if (element > limit) :
        result.append(element)

# Removing Matches
i = 0
while i < len(words) :
    word = words[i]
    if len(word) < 4 :
        words.pop(i)
    else :
        i = i + 1

# Swapping Elements
temp = values[i]
values[i] = values[j]
values[j] = temp
swap(values, i, j)  # another way to swap

# Reading Input
values = []
print("Please enter values, Q to quit:")
userInput = input("") # Get user input without a prompt.
while userInput.upper() != "Q" :
    values.append(float(userInput))
    userInput = input("")


