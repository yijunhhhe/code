class Bicycle:
    def __init__(self, gear, cadence, speed):
        self._gear = gear
        self._cadence = cadence
        self._speed = speed

    def setGear(self, gear):
        self._gear = gear

    def setCadence(self, cadence):
        self._cadence = cadence

    def applyBrake(self, speed):
        self._speed = self._speed - speed

    def speedUp(self, speed):
        self._speed = self._speed + speed

    def getSpeed(self):
        return self._speed

class MountainBike(Bicycle):
    def __init__(self, height, gear, cadence, speed):
        super().__init__(gear, cadence, speed)
        self._height = height

    def setHeight(self,height):
        self._height = height

    def getHeight(self):
        return self._height


bike = Bicycle("gear", 50, 60)
bike.applyBrake(10)
print(bike.getSpeed())
bike.speedUp()