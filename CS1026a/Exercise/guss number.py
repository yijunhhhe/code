from random import randint
randomNumber = randint(1,9)
guess = int(input("Please enter an integer: "))
while guess != randomNumber:
    if guess != randomNumber:
        guess = int(input("Please enter an integer: "))

if guess == randomNumber:
    print("Well guessed")
