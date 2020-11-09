# Number Guessing Game 1
The computer is thinking of a number between 1 and 100. Try and guess it using the hints "too high" and "too low".

## Prerequisites
none

## Concepts
- variables
- random library
- while True loop/break
- if/elif/else
- input with integers

---

## Teaching

Import the random library. There are a few ways to do this. Any of the following will work (note we only need the randint function):

`import random`

`from random import *`

`from random import randint`

Optionally explain that the random library is used so the program will pick a different number every time the game is run.

Create a variable and assign it to a random integer between 1 and 100.

Optionally talk about variables and/or integers.

Optionally add a temporary `print(target)` and run the program a few times to see that a differet number is printed each time. This will also help to check that the comparison is working properly later.

Create a second variable and assign it using the input function. Note that we need to convert the result to an int so target and guess can be compared later.

Use an if statement to compare guess and target. This can be done using three separate ifs, an if/elif/elif, or an if/elif/else.

Run the program and ensure everything is working correctly so far. Note that the program only lets you guess once.

Add the `while True` loop and the break statement.

If you added `print(target)`, comment it out or remove it.

Run the completed program.

## Extensions

### 1. Add a Guess Counter

Create a variable to track the number of guesses the player takes.

Start by creating a variable before the `while True` loop and initializing it to 0.

Every time the player guesses, increment the variable by 1.

After the player guesses correctly, print the number of guesses.

### 2. Guess the Number Efficiently

Discuss strategies for winning using the least number of guesses. Ask the student for their ideas first.

Talk about how a *binary search* can be used to quickly guess the number by chopping the total range in half each time. Draw out a numberline and work through an example by hand crossing out ranges of numbers as they are eliminated.

Example:

    What's your guess? 50
    Too high
    What's your guess? 25
    Too high
    What's your guess? 12
    Too low
    What's your guess? 18
    Too high
    What's your guess? 15
    Too high
    What's your guess? 13
    You got it!

### 3. Add a way to lose

Talk about the worst-case scenario for *binary search*. What is the maximum number of guesses it could take? Answer: 7 for 1-100. Discuss why the answer is 7.

Some explanations include:

- log_2(100) = 6.64 (rounded up to 7)

- Binary search works by dividing the range in half each time. Instead of dividing by 2, do the opposite and multiply by 2. 2x2x2x2x2x2x2 (2^7) is 128 which is greater than 100.

Add another if statement at the end of the `while True` loop that checks if the player has reached 7 guesses. If they have print a message and break.
