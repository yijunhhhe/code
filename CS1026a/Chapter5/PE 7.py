def countWords(string):
    count = 1
    for i in string:
        if i.isspace():
            count = count + 1

    return count

print(countWords("what the fuck"))