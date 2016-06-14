# Load the data into a dictionary.
popDictionary = {}
inf = open("pop3.txt", "r")

for line in inf:
   parts = line.strip().split("\t")

   # Add the city to the dictionary.
   popDictionary[parts[1]] = []
   for el in parts:
      popDictionary[parts[1]].append(el)

def printAllInformation():
   for el in popDictionary:
      print(popDictionary[el])

def printInformation(category):
   for el in sorted(popDictionary):
      print(popDictionary[el][category])

categoryDictionary = {
   1: 'name',
   2: 'province',
   3:'type',
   4:'land area',
   5: 'population in 2011'
   #FINISH FILLING THIS
}

print(popDictionary.values())
# Find out specific information about Canadian citiesRead queries from the user and respond to them.
category = (input("Enter a category ( 0 to print all information, 1 for name, 2 for province, 3 for type\n,"
                     " 4 for land area, 5 for population in 2011) or entry a city name to print all "
                     "its information (or type -1 to quit): "))
while category != "-1":
   if category.isdigit():
      category = int(category)
      if category == 0:
         printAllInformation()
      elif category <= 5 :
         print("The", categoryDictionary[category], 'of the top 15 cities in Canada is ' )
         printInformation(category)
      else :
         print("That wasn't a recognized category.")
   else: # not a string so it must be a name of the city in Canada
      print(popDictionary[category])

   print()

   # Read the next category from the user.
   category = input("Enter a category or city name (or type -1 to quit): ")

