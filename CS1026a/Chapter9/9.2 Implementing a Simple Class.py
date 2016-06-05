tally = counter()  # Construct an object using class
tally.reset()   # Method
tally.click()
tally.click()
result = tally.getValue()

def click(self) :   # Define a method
    self._value = self._value + 1

def getValue(self) :  # Return a value
    return self._value

def reset(self) :
    self._value = 0