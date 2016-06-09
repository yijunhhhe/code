class Car:
    def __init__(self, e):
        self._fuelEfficiency =e
        self._fuel = 0


    def addGas(self,fuel):
        self._fuel = self._fuel + fuel

    def drive(self, distance):

        self._fuel = self._fuel - (distance/self._fuelEfficiency)

    def getGasLevel(self):
        return self._fuel