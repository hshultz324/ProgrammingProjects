#!/usr/bin/env python3
from random import randint

target = randint(1, 100)

print("I'm thinking of a number between 1-100...")

while True:
    guess = int(input("What's your guess? "))

    if guess < target:
        print("Too low")
    elif guess > target:
        print("Too high")
    else:
        print("You got it!")
        break
