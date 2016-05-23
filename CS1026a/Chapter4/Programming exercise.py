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



#Translate pseudocode for randomly permuting the characters in a string
from random import randint
first = ""
middle = ""
last = ""
word = input("Please enter a word: ")
for numberOfTime in range(len(word)):
    i = randint(0,len(word)-1)
    l = i + 1
    if i != len(word)-1:
        j = randint(l,len(word)-1)
for a in range(0,i-1):
    first = first + word[a]
for b in range(i,j-1):
    middle = middle + word[b]
for c in range(j,len(word)):
    last = last + word[c]

print(first + word[j-1] + middle + word[i-1] + last)


# Read a word and prints the word in reverse
word = input("Please enter a word: ")
for i in range(len(word)-1,-1,-1):
    print(word[i], end="")



