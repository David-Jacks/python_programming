# average rainfall calculation program
# initializing variables
to_inches = 0
months = 0
# Taking inputs from user
yrs = int(input("Enter the number of years: "))
# Processing Input with a loop
for i in range(yrs):
    for t in range(12):
        rain_inches = float(input(f"Enter the inches of rainfall for month {months + 1}: "))
        to_inches += rain_inches
        months += 1

average_rainfall = to_inches / 12 # calculating average   
# making neccesary outputs
print("The number of months is", months)
print("The total inches of rainfall is", to_inches)
print(f"The average rainfall for the entire period is {average_rainfall :.2f}")
