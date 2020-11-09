#!/usr/bin/env python3
from random import choice

computer_choice = choice(["rock", "paper", "scissors"])
player_choice = input("Choose rock, paper, or scissors: ")
print("I choose", computer_choice)

if player_choice == computer_choice:
    print("Tie!")
elif player_choice == "rock" and computer_choice == "scissors":
    print("You win!")
elif player_choice == "paper" and computer_choice == "rock":
    print("You win!")
elif player_choice == "scissors" and computer_choice == "paper":
    print("You win!")
else:
    print("You lose!")
