def __init__(self, filename):
        continentFile = open("continent.txt","r")
        datafile = open(filename, "r")
        self._cDic = {}
        self._catalogue = set()
        # Stores country and corresponding value into dictionary
        for line in continentFile:
            line = line.rstrip().split(",")
            # skip the first line when reading each line
            if line[0] == "Country":
                continue
            self._cDic[line[0]] = line[1]
        # Stores country object into a set
        for line in datafile:
            line = line.rstrip().split("|")
            # skip the first line
            if line[0] == "Country":
                continue
            line[1] = int(line[1].replace(",",""))
            line[2] = float(line[2].replace(",",""))
            country = Country(line[0], line[1], line[2], self._cDic[line[0]])
            self._catalogue.add(country)