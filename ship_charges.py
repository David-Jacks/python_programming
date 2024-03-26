# shipping charges program for a company

# taking input from the user
weight = int(input("Enter the weight of the package(in pounds): "))

# processing user input
if (weight <= 2):
    print("charge is $1.50")
elif (weight > 2 and weight <= 6):
    print("charge is $3.00")
elif (weight > 6 and weight <= 10):
    print("charge is $4.00")
elif (weight > 10):
    print("charge is $4.75")