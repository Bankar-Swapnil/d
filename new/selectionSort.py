# -22 5 0 11 -29 8 -7 20 47 38
def selectionsort(array, size):
    for ind in range(size):
        min_index = ind
        for j in range(ind + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        (array[ind], array[min_index]) = (array[min_index], array[ind])

arr = list(map(int, input("Enter the elements of the array (space-separated): ").split()))
size = len(arr)
selectionsort(arr, size)
print('Array after sorting in ascending order is:')
print(arr)
