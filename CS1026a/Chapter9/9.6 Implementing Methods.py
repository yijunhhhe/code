def addItem(self, price) :
    self._itemCount = self._itemCount + 1
    self._totalPrice = self._totalPrice + price

def addItems(self, quantity, price) :
    for i in range(quantity) :
        self.addItem(price)