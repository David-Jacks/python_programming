#creating a dictionary

phonebook = {'chris':'555-111', 'katie': '555-2222', 'Joanne':'555-3333'} #this is a dictionary
if 'Joanner' not in phonebook:
    phonebook['Joanner'] = '444-1234'
else :
    print(None)

del phonebook['chris'] #deleting an element from a dictionary
print(phonebook)

for k in phonebook:
    print(k, phonebook[k])

#dictionary comprehension
numbers = [1, 2 ,3, 4, 5]

dict_numbers = {key:key*2 for key in numbers}

print(dict_numbers)