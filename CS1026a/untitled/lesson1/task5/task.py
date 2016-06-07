import math
#check if number is prime not overly efficient
def prime(n):
    if n==1 or n==0:
        return False
    for x in range(2,int(math.sqrt(n)+1)):
        if n%x == 0:
            return False
    return True

def evenSet(numberList):
    evenset = set()
    for i in numberList:
        if i % 2 == 0:
            evenset.add(i)
    return evenset

def oddSet(numberList):
    oddset = set()
    for i in numberList:
        if i % 2 == 1:
            oddset.add(i)
    return oddset

def multipleOf3Set(numberList):
    multipleof3 = set()
    for i in numberList:
        if i % 3 == 0:
            multipleof3.add(i)
    return multipleof3

def multipleOf5Set(numberList):
    multipleof5 = set()
    for i in numberList:
        if i % 5 == 0:
            multipleof5.add(i)
    return multipleof5



dict = {}
numberList = []
primeSet = set()
for i in range(101):
    numberList.append(i)
    isPrime = prime(i)
    if isPrime == True:
        primeSet.add(i)
even = evenSet(numberList)
odd = oddSet(numberList)
multipleOf3 = multipleOf3Set(numberList)
multipleOf5 = multipleOf5Set(numberList)
dict = {"even":even, "odd":odd, "multipleOfThree":multipleOf3, "MultipleOf5":multipleOf5, "Prime":primeSet}

print(dict)
