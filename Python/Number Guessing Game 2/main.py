#!/usr/bin/env python3
print("Think of a number from 1-100")

lower = 1
upper = 100

while True:
    guess = (lower + upper) / 2
    print("I guess", guess)
    answer = input("Am I correct? ")

    if answer == "too high":
        upper = guess
    elif answer == "too low":
        lower = guess
    elif answer == "correct":
        print("Yay!")
        break
