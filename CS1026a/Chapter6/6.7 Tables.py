# Creating Tables
counts = [     # one way
[ 0, 3, 0 ],
[ 0, 0, 1 ],
[ 0, 0, 1 ],
[ 1, 0, 0 ],
[ 0, 0, 1 ],
[ 3, 1, 1 ],
[ 0, 1, 0 ]
[ 1, 0, 1 ]
]

table = []             # another way
ROWS = 5
COLUMNS = 20
for i in range(ROWS):
    row = [0] * COLUMNS
    table.append(row)

# Accessing Elements
for i in range(COUNTRIES) :
# Process the ith row.
    for j in range(MEDALS) :
    # Process the jth column in the ith row.
        print("%8d" % counts[i][j], end="")
print()

# Locating Neighboring Elements
total = 0
if i > 0 :
    total = total + counts[i - 1][j]
if i < ROWS - 1 :
    total = total + counts[i + 1][j]

# Computing Row and Column Totals
total = 0
for j in range(MEDALS) :
    total = total + counts[i][j]
total = 0
for i in range(COUNTRIES) :
    total = total + counts[i][j]

# Using Tables with Function.
len(values) # is the number of rows.
len(values[0]) # is the number of columns.

def sum(values) :                   # Sum of all elements
    total = 0
    for i in range(len(values)) :
        for j in range(len(values[0])) :
            total = total + values[i][j]
    return total