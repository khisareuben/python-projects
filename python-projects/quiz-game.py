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
    print("The correct answer is central processing unit")
    print(Style.RESET_ALL)

answer = input("\n2. Who invented the Mechanical calculator known as Pascaline? ").lower()
if answer == "blaise pascal":
    print(Fore.BLUE + "correct!")
    score += 1
    print(Style.RESET_ALL)

else:
    print(Fore.RED + "Incorrect!")
    print("The correct answer is blaise pascal")
    print(Style.RESET_ALL)


answer = input("\n3. Which program runs on a computer when the computer boots up? ").lower()
if answer == "operating system":
    print(Fore.BLUE + "correct!")
    score += 1
    print(Style.RESET_ALL)


else:
    print(Fore.RED + "Incorrect!")
    print("The correct answer is operating system")
    print(Style.RESET_ALL)


answer = input("\n4. What was the first version of windows called? ").lower()
if answer == "interface manager":
    print(Fore.BLUE + "correct!")
    score += 1
    print(Style.RESET_ALL)



else:
    print(Fore.RED + "Incorrect!")
    print("The correct answer is Interface manager")
    print(Style.RESET_ALL)


answer = input("\n5. What is the name of the process when the operating system runs? ").lower()
if answer == "booting":
    print(Fore.BLUE + "correct!")
    score += 1
    print(Style.RESET_ALL)



else:
    print(Fore.RED + "Incorrect!")
    print("The correct answer is booting")
    print(Style.RESET_ALL)


answer = input("\n6. Which computer memory stores data temporarily? ").lower()
if answer == "random access memory" or "RAM":
    print(Fore.BLUE + "correct!")
    score += 1
    print(Style.RESET_ALL)



else:
    print(Fore.RED + "Incorrect!")
    print("the correct answer is random access memory(RAM)")
    print(Style.RESET_ALL)


answer = input("\n7. Which proramming language was used by the first generation computers? ").lower()
if answer == "machine language":
    print(Fore.BLUE + "correct!")
    score += 1
    print(Style.RESET_ALL)



else:
    print(Fore.RED + "Incorrect!")
    print("The correct answer is machine language")
    print(Style.RESET_ALL)


answer = input("\n8. Which programming language was used by the second generation computers? ").lower()
if answer == "assembly language":
    print(Fore.BLUE + "correct!")
    score += 1
    print(Style.RESET_ALL)



else:
    print(Fore.RED + "Incorrect!")
    print("The correct answer is assembly language")
    print(Style.RESET_ALL)


answer = input("\n9. Which programming language us used by apple computer? ").lower()
if answer == "swift language" or "swift":
    print(Fore.BLUE + "correct!")
    score += 1
    print(Style.RESET_ALL)

else:
    print(Fore.RED + "Incorrect!")
    print("The correct answer is Swift language")
    print(Style.RESET_ALL)


answer = input("\n10. When is world computer literacy day? ").lower()
if answer == "2 december" or "2nd dec" or "2nd december":
    print(Fore.BLUE + "correct!")
    score += 1
    print(Style.RESET_ALL)


else:
    print(Fore.RED + "Incorrect!")
    print("The correct answer is 2 december")
    print(Style.RESET_ALL)


print(f"You got {score} questions correct")
percentage = (score / 10) * 100
print(f"You got {percentage}%")

