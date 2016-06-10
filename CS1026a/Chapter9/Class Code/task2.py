file = open('rawdata.txt', 'r')
data = dict()

for line in file:
    line = line.rsplit("\t")
    line[2] = line[2].strip('\n')
    line[2] = line[2].strip('$')
    line[2] = line[2].strip(' ')
    line[2] = line[2].replace(',',"")
    data[line[1].upper()] = line[2]

alphaD = dict()

bets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for char in bets:
    alphaD[char] = set()

for char in alphaD:
    for key in data:
        if key.startswith(char):
            alphaD[char].add(key)

print(data)
print(alphaD)


category = (input("Enter an alphabet for get the proper name for a country or enter the name of the country or enter QUIT to quit: ")).upper()
while category != "QUIT":
   if len(category) == 1:
       print('The names of countries that begin with the letter ', category)
       print(alphaD[category])
   else:
       print('The amount for', category, 'is', data[category], 'dollars')
   print()

   # Read the next category from the user.
   category = (input("Enter an alphabet for get the proper name for a country or enter the name of the country or enter QUIT to quit: ")).upper()

