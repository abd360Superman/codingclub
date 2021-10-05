import random

randNum = random.randint(1, 100)
tries = 0

while True:
    tries += 1
    guess = int(input('Guess a number between 1 to 100: '))

    if guess == randNum:
        print("You guessed right! It took you %s turns!" % (int(tries)))
        break
    elif guess > randNum:
        print("Too high")
    elif guess < randNum:
        print("Too low")