#!/usr/bin/env python3
from random import randint

target = randint(1, 100)
guess_count = 0

print("I'm thinking of a number between 1-100...")

while True:
    guess = int(input("What's your guess? "))
    guess_count += 1

    if guess < target:
        print("Too low")
    elif guess > target:
        print("Too high")
    else:
        print("You got it in", guess_count, "guesses!")
        break
