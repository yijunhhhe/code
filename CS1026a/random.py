class City:

    def __init__(self, n, p, t, la, pop):
        self._name = n
        self._province = p
        self._type = t
        self._landArea = la
        self._population = pop

cityDic = dict()
inFile = open("pop3.txt", "r")
line = inFile.split()
for eachWord in line:
    cityDic[line[1]] = line

