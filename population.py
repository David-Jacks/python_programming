# predicting the appropiate population of organisms

# variables initialization with user input
start_no = int(input("Enter the starting number of organisms: "))
increase = start_no
aver_increase = float(input("Enter the average daily population increase(as percentage): ")) / 100

no_days = int(input("Enter the number of das he organism will be left to multiply: ")) 

# processing and output

print("Day Approximate\t\tPopulation")

for i in range(no_days):
    print(f"{i + 1}\t\t\t{increase :.5f}")
    increase = increase + (aver_increase * increase)

