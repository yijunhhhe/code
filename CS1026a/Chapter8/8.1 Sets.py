# Creating and Using Sets
cast = {"Luigi","Gumbys","Spiny"}
names = ["Luigi", "Gumbys", "Spiny"]
cast = set(["Luigi", "Gumbys", "Spiny"])
cast = set(names)   # set up a list
cast = set()    # Make an empty set
for charater in sorted(cast):   # Sort cast
    print(charater)
len(cast)   # length of set


# Adding and Removing Elements
cast.add("Arthur")
cast.discard("Luigi")   # no effect
cast.remove("Luigi")    # Raise an exception if element not a member of list
cast.clear()
print(cast)


# Subsets
canadian = { "Red", "White" }
british = { "Red", "Blue", "White" }
italian = { "Red", "White", "Green" }
if canadian.issubset(british):
    print("oh yes")


# Equality
french = { "Red", "White", "Blue" }
if british == french :
    print("The British and French flags use the same colors.")



#Set Unions, Intersection, and Difference
inEither = british.union(italian)
inBoth = british.intersection(italian)
difference = british.difference(italian)


#
