# A function that takes a python list as input and sorts it using
# the selection sort algorithm and returns the sorted list

def selection_sort(array):
    array_size = len(array)

    for i in range(0, array_size - 1):
        index_min = i

        for j in range(i + 1, array_size):
            if array[j] < array[index_min]:
                index_min = j
        
        if index_min != i:
            array[i], array[index_min] = array[index_min], array[i]

    
    return array