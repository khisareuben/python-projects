from colorama import Fore, Back, Style
print(Fore.MAGENTA)

name = input("Enter your name: ")
print(f"\nWelcome {name} to this adventure\n\n")

answer = input(
    "You are on a dirt road, it has come to an end and you can go left of right. Which way would you choose? ").lower()

if answer == "left":
    answer1 = input(
        "You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ").lower()

    if answer1 == "swim":
        print("You swam accross and were eaten by an alligator")

    elif answer1 == "walk":
        print("You walked for many mile, ran out of water and lost the game")

    else:
        print("Not a valid option. You lose!")

elif answer == "right":
    answer1 = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")

    if answer1 == "back":
        print("You go back and lose.")

    elif answer1 == "cross":
        answer2 = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")

        if answer2 == "yes":
            print("You talked to the stranger and they give you gold. You win!")

        elif answer2 == "no":
            print("You ignored the stranger and got lost. You lose!")

        else:
            print("Not a valid option. You lose!")

    else:
        print("Not a valid option. You loose!")


else:
    print("Not a valid option. You loose!")
