#Rainfall statistics program
# initiating the rainfall list andsome variables
rainfall = []
total_rainfall = 0

for i in range(12):
    # taking inputs into the rainfall list
    rainfall.append(int(input(f"Enter rainfall amount for month {i + 1} : ")))
    total_rainfall += rainfall[i] #calculating the total rainfall for the year within same loop for efficiency purposes
    
highest = rainfall[0]
lowest = rainfall[0]
# processing inputs
average_mon_rainfall = total_rainfall / 12
for i in range(12):
    if (rainfall[i] > highest):
        highest = rainfall[i]
    if (rainfall[i] < lowest):
        lowest = rainfall[i]

#outputing
print("The total rainfall for the year is", total_rainfall)
print(f"Average monthly rainfall is {average_mon_rainfall :.2f}")
print(f"The months with the highest and lowest amounts are, {highest} and {lowest} respectively")