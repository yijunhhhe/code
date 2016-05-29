# Creating Dictionaries
contacts = {"Fred": 87209562, "Ted": 4166666802, "Yijun":1371161273}
oldContacts = dict(contacts)

#-----------------------------
# Accessing Dictionary Values
print(contacts["Ted"])
if "Yijun" in contacts:
    print(contacts["Yijun"])
number = contacts.get("What", 811111)
print(number)

#-------------------------
# Adding and Modifying Items
contacts["Fred"] = 123456789
favoriteColors = {}
favoriteColors["Juliet"] = "Blue"
favoriteColors["Ted"] = "Yellow"

#-------------------------
# Removing Items
contacts.pop("Fred")
#fredsNumber = contacts.pop("Fred")

#------------------------
# Traversing a Dictionary
for key in sorted(contacts):
    print(key, contacts[key])

phoneNumbers = []
for number in contacts.values():
    phoneNumbers.append(number)

phoneNumbers = list(contacts.value())

