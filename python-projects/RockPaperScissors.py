# 57
import random
from colorama import Fore, Back, Style
print(Fore.CYAN)

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Rock/Paper/Scissors or q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # Rock = 1, paper = 2, scissors = 3
    computer_pick = options[random_number]
    print(f"computer picked {computer_pick}.")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
 
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
    
    elif user_input == computer_pick:
        print("It's a tie")
        continue

    else:
        print("You lose!")
        computer_wins += 1
 
print(f"You won {user_wins} times")
print(f"Computer wins {computer_wins} times")
print("Goodbye, have a lovely day")


