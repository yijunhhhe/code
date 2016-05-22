age = int(input("Please enter your age: "))
month = int(input("month in which you were born"))

bornYear = 2016 - age

if 1970 < bornYear < 1989 and month == 5:
    print("You are intelligent")
    print("The people before that")
elif 1970 < bornYear < 1989 and month != 5:
    print("living in Canada and it snowed on Sunday")
elif bornYear > 2000:
    print("Z")
elif 1980 < bornYear < 2000:
    print("Millennials")
elif 1940 < bornYear < 1969:
    print("Baby boomers")