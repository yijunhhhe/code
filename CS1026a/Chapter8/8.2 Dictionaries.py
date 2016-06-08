# Creating Dictionaries
contacts = {"Fred": 87209562, "Ted": 4166666802, "Yijun":1371161273}
oldContacts = dict(contacts)    # duplicate copy of dictionary


# Accessing Dictionary Values
print(contacts["Ted"])
if "Yijun" in contacts:
    print(contacts["Yijun"])
number = contacts.get("What", 811111)
print(number)


# Adding and Modifying Items
contacts["Fred"] = 123456789  # modifying
favoriteColors = {}
favoriteColors["Juliet"] = "Blue"   # adding
favoriteColors["Ted"] = "Yellow"
favoriteColors["Ted"].append("Hey")


# Removing Items
contacts.pop("Fred")    # remove item and also return value
#fredsNumber = contacts.pop("Fred")


# Traversing a Dictionary
for key in sorted(contacts):    # for key
    print(key, contacts[key])

phoneNumbers = []
for number in contacts.values():    # for dictionary value
    phoneNumbers.append(number)

phoneNumbers = list(contacts.value())

