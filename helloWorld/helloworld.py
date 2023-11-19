'''
name = "David Jackson";
age = 19;

print(f"hello world my name is {name} and i am {age} years old");

'''

import array as arr
# taking input
# name = input("please input your name ");
# age = int(input("please input your age "));

# processing based on ages of people

# if age <= 20 :
#     print(f"{name} you are very young");
# elif age <= 30 :
#     print(f"{name} you are very old fair enough!!");
# elif age <= 50 :
#     print(f"{name} you are extra old and this is quiet serious");
# else :
#     print(f"{name} i dont want to even talk about your age now");


names = arr.array('i', [1, 2, 3, 4, 5, 6, 7])

for i in range(len(names)):
    print(names[i], end=" ")

print()
names.extend([9, 8, 4, 7])
print(names.index(5))
print(names[-1])

names.remove(4)

for i in range(len(names)):
    print(names[i], end=" ")
print()