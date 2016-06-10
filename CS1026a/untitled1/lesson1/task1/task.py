# TODO: type solution here
class Banana:
    bananaID =0
    def __init__(self):
        Banana.bananaID+=1
        self._ID = Banana.bananaID
    def __str__(self):
        return "This banana has an id of "+ str(self._ID)


#place your code here


print(b1)
print(b2)