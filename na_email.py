#A program on name and Email addresses
import pickle #pickle to be able to store my dictionary to a file
#global variables
users_details = {}
user_choice = 0
email = ''
name = ''
#displaying menu to allow for input taking
print("Enter any of the bellow choices: ")
while (user_choice != 5):
    user_choice = int(input("1. Check for a users email\n2. add a new user\n3. Change user email\n4. delete user details\n5. End session\n: "))
    
    if (user_choice == 1):
        name = input("Enter the users name: ")
        print(users_details[name])
    elif (user_choice == 2):
        name = input("Enter users name: ")
        email = input("Enter users email address: ")
        users_details[name] = email
    elif (user_choice == 3):
        name = input("Enter users name: ")
        email = input("Enter new email address: ")
        users_details[name] = email
    elif (user_choice == 4):
        name = input("Enter users name to delete user details: ")
        del users_details[name]
    else :
        print("No valid choice made, please check your input")

#saving it to a file
print(users_details)