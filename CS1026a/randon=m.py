class student:
    def __init__(self,name):
        self._name = name
        self._totalScore = 0
        self._count = 0

    def getName(self):
        return  self._name

    def addQuiz(self,score):
        self._totalScore = self._totalScore + score
        self._count = self._count + 1

    def getTotalScore(self):
        return self._totalScore

    def getAverageScore(self):
        return self._totalScore/self._count
