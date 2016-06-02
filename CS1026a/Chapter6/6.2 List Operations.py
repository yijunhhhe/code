# Appending Elements
friends = []
friends.append("Ted")
friends.append("Yijun")
friends.append("Tedhe")

# Inserting an Element
friends.insert(2,"Hey")

# Finding an Element
if "Ted" in friends:  # see if it's in the list
    print("Yes")
n = friends.index("Tedhe") # find the position
n = friends.index("Tedhe", n + 1) # find the second Tedhe

# Removing an Element
friends.pop(0) # pop method will return the popped value
friends.remove("Hey") # Alternative

# Concatenation and Replication
myFriends = ["Fritz", "Cindy","Phuong"]
yourFriends = ["Lee", "Pat", "Phuong"]
ourFriends = myFriends + yourFriends
print(ourFriends)
monthInQuarter = [1, 2, 3] * 4  # same list multiple times

# Equality Testing
#[1, 4, 9] == [1, 4, 9] is True
#but [1, 4, 9 ] == [4, 1, 9] is False.

# Sum, Maximum, Minimum, and Sorting
sum = sum([1, 4, 9, 16])
max([1, 16, 9, 4])
min("Fred", "Ann", "Sue")
values = [1, 16, 9, 4] # sort
values.sort() # Now values is [1, 4, 9, 16]

# Copying Lists
prices = values #first way. this only add a reference
prices = list(values) #second way
characters = list("Hello") # The list is ["H", "e", "l", "l", "o"]