# Color Mixure program
# primary colors are red, blue and yellow

import time #making neccesary imports to be used in the program

# Taking inputs from the user
pri_color1 = input("Enter first color(red, blue or yellow): ")


if (pri_color1 == "red" or pri_color1 == "blue" or pri_color1 == "yellow"):
    
    # taking the second input insside the if block
    pri_color2 = input("Enter second color(red. blue or yellow): ")
    print("the mixure is ongoing please wait....")
    time.sleep(3) #this statements causes the program to stop executing for 3 seconds and then continue

    if ((pri_color1 == "red" and pri_color2 == "blue") or (pri_color1 == "blue" and pri_color2 == "red")):
        print("The result is a purple color")
    elif ((pri_color1 == "blue" and pri_color2 == "yellow") or (pri_color1 == "yellow" and pri_color2 == "blue")):
        print("The result is a green color")
    elif ((pri_color1 == "yellow" and pri_color2 == "red") or (pri_color1 == "red" and pri_color2 == "yellow")):
        print("The result is a orange color")
    else:
        print("wrong second primary color was entered")
else:
    print("You entered a wrong primary color!")