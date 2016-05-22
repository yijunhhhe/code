fahrenheit = float(input("Please enter the temperature value: "))

celsius = (fahrenheit - 32) * 5 / 9

if celsius < 0:
    print("It is solid")
elif celsius >= 0 and celsius <= 100:
    print("It is water")
else:
    print("It is gas")

