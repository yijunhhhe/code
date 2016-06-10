class Course:
    MAXNUMBER = 100
    def __init__(self, cn):
        self._name = cn
        self._studentDict = {}

    def addStudent(self, name, studentNumber ):
        if(len(self._studentDict) < Course.MAXNUMBER):
            self._studentDict[studentNumber] = list()
            self._studentDict[studentNumber].append(name)
            self._studentDict[studentNumber].append(0)

    def printStudentsByName(self):
        for (key, value) in self._studentDict.items():
            print(value[0])

        for key in self._studentDict:
            print(self._studentDict[key][0])

    def printStudentsByScore(self):
        for (key, value) in self._studentDict.items():
            print(value[1])

    def getAverageScore(self):
        totalScore = 0
        for (key, value) in self._studentDict.items():
            totalScore = totalScore + value[1]

        return totalScore/len(self._studentDict)

    def getMinimumScore(self):
        minScore = 100
        for (key, value) in self._studentDict.items():
            if (value[1] < minScore):
                minScore = value[1]

        return minScore

    def updateStudentScore(self, studentNumber, score):
        if studentNumber in self._studentDict:
            self._studentDict[studentNumber][1] = score

    def searchForStudent(self, studentNumber):
        if studentNumber in self._studentDict:
            return self._studentDict[studentNumber][1]

    def __repr__(self):
        return "I am a Course"