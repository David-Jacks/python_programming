#linear search algorithm

#an array of n
#k is the element to be found in the array

arr1 = [5, 4, 3, 2, 1, 0, -1, -5, 10, 15]
def linearSearch(arr, k):
    size = len(arr) #1
    ans = -1 #1 this is to make sure that we know when the element is not found in the array, its an odd index
    for i in range(size):# n
        if (arr[i] == k): #1
            ans = i #1
    return ans #1

print(linearSearch(arr1, 5))

