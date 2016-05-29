# Creating and Using Sets
cast = {"Luigi","Gumbys","Spiny"}

names = ["Luigi", "Gumbys", "Spiny"]
cast = set(names)
# Make an empty set
cast = set()
# Sort cast
for charater in sorted(cast):
    print(charater)

#-----------------------------
# Adding and Removing Elements
cast.add("Arthur")
cast.discard("Luigi")
cast.clear()
print(cast)

#---------------------------
# Subsets
canadian = { "Red", "White" }
british = { "Red", "Blue", "White" }
italian = { "Red", "White", "Green" }

if canadian.issubset(british):
    print("oh yes")


#----------------------------
#Set Unions, Intersection, and Difference
inEither = british.union(italian)
inBoth = british.intersection(italian)
difference = british.difference(italian)


#
