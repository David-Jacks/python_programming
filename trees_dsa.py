from random import randint, choices
# # Going throught the trees datastructure
# class BT_NODE:
#     data = 0
#     left = None
#     right = None

#     # constuctor
#     def __init__(self, data):
#         self.data = data
        

# root = BT_NODE(0)
# left_node = BT_NODE(1)
# right_node = BT_NODE(2)
# root.left = left_node
# root.right = right_node
# sec_right = BT_NODE(3)
# right_node.right = sec_right

# tmp = root
# while (tmp != None):
#     if tmp.right != None:
#         print(tmp.data, end="->")
#     else:
#         print(tmp.data, end="")
#     tmp = tmp.right


list1 = [num for num in range(1, 10)]
list2 = [randint(0, 10) for j in range(10)]


ziped_tuple = zip(list1, list2)

for key, val in ziped_tuple:
    # print(key, val)
    pass

for index, val in enumerate(list1):
    print(index, val)