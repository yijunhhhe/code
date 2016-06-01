<<<<<<< HEAD
def sum(list):
    smallest = 100
    largest = 0
    evenList = []
    oddList = []
    for i in list:
        if i % 2 == 0:
            evenList.append(i)
        if i % 2 == 1:
            oddList.append(i)
    print(evenList)
    print(oddList)
    sum = min(oddList) + max(evenList)
    return sum

list = [1,3,5,6,8,43,3,9,87,56,44,33,2,45]
sum = sum(list)
print(sum)

=======
>>>>>>> origin/master
