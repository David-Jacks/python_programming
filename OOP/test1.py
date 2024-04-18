# creating a Dog class in python
class Dog:
#     class attribute
        attri1 = "Mammal"
#       class instance variable or constructor
        def __init__(self, name):
                self.name = name        

# object instantiation

firstDog = Dog("Ricky")
secondDog  = Dog("Angel")

print(f"The first dogs name is {firstDog.name}")
print(f"The second dogs name is {secondDog.name}")

print(f"{firstDog.name} is a {firstDog.attri1}")