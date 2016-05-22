for i in range(3):
    for j in range(4):
        print("*", end="")
    print()

for i in range(4):
    for j in range(3):
        print("*", end="")
    print()

for i in range(4):
    for j in range(i+1):
        print("*", end="")
    print()

for i in range(3):
    for j in range(5):
        if j % 2 == 1:
            print("*", end="")
        else:
            print("-", end="")
    print()

for i in range(3):
    for j in range(5):
        if i % 2 == j % 2:
            print("*", end="")
        else:
            print("", end="")
    print()