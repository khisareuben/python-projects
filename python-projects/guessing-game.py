# 42
import random
from colorama import Fore, Back, Style
print(Fore.MAGENTA)

top_of_range = (input("Enter a number: "))

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please enter a number greater than 0 next time")
        quit()

else:
    print("Please type a number next time")



random_number = random.randint(0, top_of_range)

guess_count = 0

while True:
    user_guess = input("Make a guess: ")
    guess_count += 1
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Please type a number next time")
        continue

    if user_guess == random_number:
        print("You won!")
        break

    elif user_guess > random_number:
        print("You were above the number")

    else:
        print("You were below the number")

print(f"You got it in {guess_count} guesses")
print(Style.RESET_ALL)
