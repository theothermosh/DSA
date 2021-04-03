# A function that takes a python list as input and sorts it using
# the bubble sort algorithm and returns the sorted list

def bubble_sort(array):
    array_size = len(array)

    for _ in range(array_size):
        for index in range(array_size - 1):
            if array[index] > array[index + 1]:
                array[index], array[index + 1] = array[index + 1], array[index]


    return array