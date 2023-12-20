# creating a Dog class in python
# class Dog:
# #     class attribute
#         attri1 = "Mammal"
# #       class instance variable or constructor
#         def __init__(self, name):
#                 self.name = name        

# # object instantiation

# firstDog = Dog("Ricky")
# secondDog  = Dog("Angel")

# print(f"The first dogs name is {firstDog.name}")
# print(f"The second dogs name is {secondDog.name}")

# print(f"{firstDog.name} is a {firstDog.attri1}")

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None #since python is dynamically typed, the next will automatically store the address of a type node if a node is assigned to it
        
head = Node(4)
tmp = head
counter = 1
while(counter != 5):
    currNode = Node(counter)
    tmp.next = currNode
    tmp = tmp.next
    counter += 1

tmp = head #printing the linked list values
while tmp is not None:
    print(tmp.val)
    tmp = tmp.next
print()
#insertion at a particular position in a linked list
#let say we are inserting at position 3
pos = 1
counter = 1
tmp = head #traversing the linked list to be able to insert at the desired position
while (tmp != None):
        if (pos == 1):
             newNode = Node(45)
             newNode.next = head
             head = newNode
             break
        if (counter == pos - 1):
             tmpAdd = tmp.next
             newNode = Node(45)
             tmp.next = newNode
             newNode.next = tmpAdd
             break
        tmp = tmp.next
        counter += 1

#printing linked list after insertion
tmp = head #printing the linked list values
while tmp is not None:
    print(tmp.val)
    tmp = tmp.next
print()
#deleting a node at a specified position in a linked list
pos = 1
tmp = head

while(tmp != None):
        if (pos == 1):
                head = head.next
                break
        if (counter == pos - 1):
                tmp.next = tmp.next.next
                break
        
        tmp = tmp.next

#printing linked list after deletion
tmp = head #printing the linked list values
while tmp is not None:
    print(tmp.val)
    tmp = tmp.next