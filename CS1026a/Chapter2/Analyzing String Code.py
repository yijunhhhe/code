# Obtain the input from users
for i in range (5):
    string1 = input("Please enter first string: ")
    string2 = input("Please enter second string: ")


    if string1.isdigit() and string2.isdigit():
        average = (int(string1) + int(string2)) / 2
    elif not string1.isdigit() and not string2.isdigit():
        if string2 in string1:
            times = string1.count(string2)
            print(times)
