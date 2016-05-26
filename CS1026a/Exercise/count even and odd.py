numbers = list(range(21))
even = 0
odd = 0
for number in numbers:
    if number % 2 == 0:
        even = even + 1
    elif number % 2 == 1:
        odd = odd + 1
print(even, odd)