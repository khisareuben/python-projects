from colorama import Fore, Back, Style

print(Fore.GREEN + "\n\n............. Welcome to my computer quiz ..............")
print(Style.RESET_ALL)

playing = input("Do you want to play? ").lower()
if playing != "yes":
    quit()

score = 0

print("Let's go soldier, Let's play...")

answer = input("\n1. What does CPU stand for? ").lower()
if answer == "central processing unit":
    print(Fore.BLUE + "correct!")
    score += 1
    print(Style.RESET_ALL)


else:
    print(Fore.RED + "Incorrect!")
    print(Style.RESET_ALL)

answer = input("\n2. What does CPU stand for? ").lower()
if answer == "central processing unit":
    print(Fore.BLUE + "correct!")
    score += 1
    print(Style.RESET_ALL)

else:
    print(Fore.RED + "Incorrect!")
    print(Style.RESET_ALL)


answer = input("\n3. What does CPU stand for? ").lower()
if answer == "central processing unit":
    print(Fore.BLUE + "correct!")
    score += 1
    print(Style.RESET_ALL)


else:
    print(Fore.RED + "Incorrect!")
    print(Style.RESET_ALL)


answer = input("\n4. What does CPU stand for? ").lower()
if answer == "central processing unit":
    print(Fore.BLUE + "correct!")
    score += 1
    print(Style.RESET_ALL)



else:
    print(Fore.RED + "Incorrect!")
    print(Style.RESET_ALL)


answer = input("\n5. What does CPU stand for? ").lower()
if answer == "central processing unit":
    print(Fore.BLUE + "correct!")
    score += 1
    print(Style.RESET_ALL)



else:
    print(Fore.RED + "Incorrect!")
    print(Style.RESET_ALL)


answer = input("\n6. What does CPU stand for? ").lower()
if answer == "central processing unit":
    print(Fore.BLUE + "correct!")
    score += 1
    print(Style.RESET_ALL)



else:
    print(Fore.RED + "Incorrect!")
    print(Style.RESET_ALL)


answer = input("\n7. What does CPU stand for? ").lower()
if answer == "central processing unit":
    print(Fore.BLUE + "correct!")
    score += 1
    print(Style.RESET_ALL)



else:
    print(Fore.RED + "Incorrect!")
    print(Style.RESET_ALL)


answer = input("\n8. What does CPU stand for? ").lower()
if answer == "central processing unit":
    print(Fore.BLUE + "correct!")
    score += 1
    print(Style.RESET_ALL)



else:
    print(Fore.RED + "Incorrect!")
    print(Style.RESET_ALL)


answer = input("\n9. What does CPU stand for? ").lower()
if answer == "central processing unit":
    print(Fore.BLUE + "correct!")
    score += 1
    print(Style.RESET_ALL)

else:
    print(Fore.RED + "Incorrect!")
    print(Style.RESET_ALL)


answer = input("\n10. What does CPU stand for? ").lower()
if answer == "central processing unit":
    print(Fore.BLUE + "correct!")
    score += 1
    print(Style.RESET_ALL)


else:
    print(Fore.RED + "Incorrect!")
    print(Style.RESET_ALL)


print(f"You got {score} questions correct")
percentage = (score / 10) * 100
print(f"You got {percentage}%")

