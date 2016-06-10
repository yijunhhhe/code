#THIS IS THE WORKING IN CLASS ATTEMPT AT LAB 9 EXERCISE. THERE IS ALSO A FULL VERSION in ANOTHER FILE
inf = open('rawdata.txt', 'r')
countryInfo = {}
for line in inf:
    line = line.split('\t')
    line[2] = line[2].strip('\n')
    line[2] = line[2].lstrip('$')
    line[2] = line[2].strip()
    line[2] = int(line[2].replace(',', ''))
    countryInfo[line[1].upper()] = line[2]

print(countryInfo)
alphabet = {}
a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for el in a:
    alphabet[el] = set()

print(alphabet)

for char in alphabet:
    for country in countryInfo:
        if country.startswith(char):
            alphabet[char].add(country)

print(alphabet['B'])