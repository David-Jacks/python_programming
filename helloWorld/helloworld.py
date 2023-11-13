'''
name = "David Jackson";
age = 19;

print(f"hello world my name is {name} and i am {age} years old");

'''

# taking input
name = input("please input your name ");
age = int(input("please input your age "));

# processing based on ages of people

if age <= 20 :
    print(f"{name} you are very young");
elif age <= 30 :
    print(f"{name} you are very old fair enough!!");
elif age <= 50 :
    print(f"{name} you are extra old and this is quiet serious");
else :
    print(f"{name} i dont want to even talk about your age now");


