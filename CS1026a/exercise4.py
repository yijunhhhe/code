#Quiode
#Sama Rahimian, Jae Seo, Eun Seo, Yijun He
from random import randint

sum = 0
largest = 0
smallest = 100
count = 0
while sum < 100:
    value = randint(15,30)
    if value > largest:
        largest = value
    elif value < smallest:
        smallest = value
    sum = sum + value
    count = count + 1
print("Maximum", largest, "\nMinimum", smallest, "\nSum:", sum, "\nAverage: ", sum/count)
