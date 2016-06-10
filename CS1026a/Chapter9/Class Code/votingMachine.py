class VotingMachine:
    def __init__(self):
        self._dems = 0
        self._reps = 0

    def voteDemocrat(self):
        self._dems = self._dems + 1
        print('You just voted for hillary :( ')

    def voteRepublican(self):
        self._reps = self._reps + 1
        print('You just voted the Donald :( ')

    def getTallies(self):
        return (self._dems, self._reps)

    def reset(self):
        self._dems = 0
        self._reps = 0

    def getTotal(self):
        return self._reps + self._dems

    def getWinner(self):
        if self._reps > self._dems:
            return 'Republican'
        elif self._dems > self._reps:
            return 'Democrat'
        else:
            if self._dems == 0:
                print('Samar is hopeful that all is well')
            else:
                print('Your country will devolve into chaos')
