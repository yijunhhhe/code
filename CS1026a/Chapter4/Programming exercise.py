for i in range(21):
    power = 2 ** i
    print(power," ", end="")
print("")

# Only the uppercase letters in the string
string = input("Please enter anything you want: ")
for char in string:
    if char.isupper():
        print(char, end="")
print("")

# Every second letter of the string
print(string[1])

# The string, with all vowels replaced by an underscore
for char in string:
    if char == "A" or "E" or "I" or "O" or "U":
        
