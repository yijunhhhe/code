# Creating Lists----
values = [2,3,5,7,6,5,1]

# Accessing List Elements----
print(values[5])

# Length
len(values)

# Traversing Lists----
for i in range(len(values)):
    print(i, values[i])

# List References and modifying------
scores = values  # copy the list
scores[3] = 2  # Modifying Aliased Lists



