#paint job estimator program

#taking user inputs
sq_feet = int(input("Enter square feet of wall space to be painted: "))
one_gal_price = float(input("Enter the price of paint per gallon: "))

#processsing inputs
num_gall = sq_feet / 112 #finding the numer of gallons of paint required for the painting
hrs_lab = 8 * num_gall #8hrs is required to exhaust 1 gallon on a 112 square feet
paint_cost = one_gal_price * num_gall
lab_charges = hrs_lab * 35 # sinces for every hrs the labour cost is 35 dollars
total_cost = paint_cost + lab_charges

#output
print("The number of gallons of paint required is", num_gall)
print("The hours of labour required is", hrs_lab)
print("The cost of the paint is", paint_cost)
print("The labor charges is", lab_charges)
print("The total cost of the paint job is", total_cost)