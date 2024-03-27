#rock, paper, scissor game
import random #importing the random module to implement random number generation

#the main function
def main():
    print("Welcome to the rock, paper, scissor game")
    while (True):
        ran_no = random.randint(1, 3)
    
        computerChoice = comp_choice(ran_no)
        usersChoice = user_choie()
        if(usersChoice == "x"):
            print("thank you for playing this game")
            return

        print("You selected " + usersChoice);
        print()
        print("And your Computer also selected " + computerChoice)
        print()
        answer = judgement(computerChoice, usersChoice)
        if (answer == -1):
            print("fair judgement, please play game again")
        else:
            print(answer)
        print()


# definning the computer choice as a function
def comp_choice(choice):
     if(choice == 1):
        return "rock"
     elif(choice == 2):
        return "paper"
     elif (choice == 3):
        return "scissors"
     else:
        return "incorrect choice"
     
# definning the users choice as a function
def user_choie():
    choice = input("""Please input your choice of either "rock","paper" or "scissors" (note!! all in smaller cases) input "x" to end game: """)
    return choice

# definning the final decision as a function
def judgement(computer, user):
    if(computer == user):
        return -1
    elif (computer == "rock" and user == "scissors"):
        return "Computer won"
    elif (computer == "scissors" and user == "paper"):
        return "Computer won"
    elif (computer == "paper"  and user == "rock"):
        return "Computer won"
    elif(computer == "paper" and user == "scissors"):
        return "you won"
    elif(computer == "scissors" and user == "rock"):
        return "you won"
    elif(computer == "rock" and user == "paper"):
        return "you won"
    else:
        return "incorrect choices made"

main() #calling the main function
