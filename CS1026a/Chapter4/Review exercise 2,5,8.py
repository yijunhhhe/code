# Write a loop that computes
# The sum of all even numbers between 2 and 100
sum1 = 0
for i in range(2,101,2):
    print(i, end=" ")
    sum1 = sum1 + i
print("")
print(sum1)

# The sum of all aquares between 1 and 100
sum2 = 0
for i in range(1,101):
    sum2 = sum2 + i**2
print(sum2)

#The sum pf all odd numbers between a and b
sum3 = 0
for i in range(sum1,sum2+1):
    if i % 2 == 1:
        sum3 = sum3 + i
print(sum3)

# The sum of all odd digits of n
sum = str(sum3)
sum4 = 0
for char in sum:
    if int(char) % 2 == 1:
        sum4 = sum4 + int(char)

print(sum4)





