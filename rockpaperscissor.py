import random
user_choice= input("Enter your choice - Rock / Paper / Scissor: ")
choices=["Rock","Paper","Scissor"]
computer_choice=random.choice(choices)
print("Computer's choice is: ",computer_choice)
if user_choice== "Rock" or user_choice== "Paper" or user_choice== "Scissor":
    if user_choice == computer_choice :
        print("It's a TIE!")
    elif user_choice== "Paper" and computer_choice=="Rock":
        print("You WIN!")
    elif user_choice=="Scissor" and computer_choice=="Paper":
        print("You WIN!")
    elif user_choice=="Rock" and computer_choice=="Scissor":
        print("You WIN!")
    else:
        print("You LOSE :(")
else:
    print("Enter a valid response")