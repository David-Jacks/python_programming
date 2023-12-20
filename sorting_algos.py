#sorting algotithms problem solving

#Bubble sort
#assuming a list of values to be sorted in ascending order of magnitude
arr = [2, 4, 2, 3, 9, 8, 6, 1]

def bubbleSort(arr):
    arr_size = len(arr)

    for i in range(arr_size - 1):
        sorted = True
        for j in range(1, arr_size):
            if (arr[j] < arr[j - 1]):
                arr[j], arr[j - 1] = arr[j -1], arr[j] # over here we are swapping at a constant time using the tuple unpacking
                sorted = False #this flag is for early termination to make the algorithm more efficient, 
                               #such that if at the ith iteration there is no swap, then it meaans the array is sorted
        
        if (sorted):
            return
    print(arr)

bubbleSort(arr)

#selection sort algorithm
def selectionSort(arr):
    
    for i in range(len(arr)):
        for j in range(1, len(arr) - i):
            if (arr[j] < arr[j - 1]):
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    print(arr)

selectionSort(arr)