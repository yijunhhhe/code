class VotingMachine :

   def __init__(self) :
      self._dem_count = 0
      self._rep_count = 0

   def voteDemocrat(self) :
      self._dem_count = self._dem_count + 1

   def voteRepublican(self) :
      self._rep_count = self._rep_count + 1

   def getTallies(self) :
      return (self._dem_count, self._rep_count)

   def reset(self) :
      self._dem_count = 0
      self._rep_count = 0

   def getTotal(self) :
      return self._dem_count + self._rep_count

   def getWinner(self) :
      if(self._dem_count > self._rep_count):
         return "the Democrats"
      elif (self._rep_count > self._dem_count) :
         return "the Republicans"
      else:
       return "No winner"
