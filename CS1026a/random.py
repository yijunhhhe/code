class Car:
    def __init__(self, fuel):
        self._fuelEfficiency = 50
        self._fuel = fuel
        self._distance = 0

    def addGas(self,fuel):
        self._fuel = self._fuel + fuel

    def drive(self, distance):
        self._distance = distance
        self.fuel = self._fuel - (self._distance/self._fuelEfficiency)

    def getGasLevel(self):
        return self._fuel