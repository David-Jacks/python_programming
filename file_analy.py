#A file analysis program
#input are two files that we will read from

file1 = open('file1.txt', 'r')
file2 = open('file2.txt', 'r')

set1 = set(file1.readline())
set2 = set(file2.readline())

file1.close()
file2.close()

# outputing
print("The sets read from the files are: ", end="") 
print(set1, set2)
print()
#list of all the unique words contained in both files.
print("1.", set1.union(set2))
#list of the words that appear in both files.
print("2.", set1.intersection(set2))
#list of the words that appear in the first file but not the second.
print("3.", set1.difference(set2))
#list of the words that appear in the second file but not the first.
print("4.", set2.difference(set1))
#list of the words that appear in either the first or second file, but not both.
print("5.", set1.symmetric_difference(set2))