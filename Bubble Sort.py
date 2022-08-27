def bubblesort(array):
    i = 0
    while i < len(array) - 1:
        j = 0
        while j < len(array) - i - 1:
            if array[j] > array[j + 1]:
                array[j], array[j+1] = array[j+1], array[j]
            j = j + 1
        i = i + 1

    print("After Sorting: ", array)


string = input("Enter any Array: ")
arr = [int(x) for x in string.split(' ')]
print("Before Sorting: ", arr)
bubblesort(arr)
