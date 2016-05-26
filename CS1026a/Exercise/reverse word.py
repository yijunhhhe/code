word = input("Please enter a word: ")
wordLength = int(len(word)-1)
newWord = ""
for i in range(wordLength,-1,-1):
    newWord = newWord + word[i]

print(newWord)


# Method 2
word = input("Please enter a word: ")
for char in range(len(word) - 1, -1, -1):
    print(word[char], end="")
