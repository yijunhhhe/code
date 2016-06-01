def middle(string):
    if len(string) % 2 == 1 :
        character = string[int(len(string)/ 2)]
    elif len(string) % 2 == 0 :
        character = string[int(len(string)/2-1)]+ string[int(len(string)/2)]
    return character

print(middle("what"))