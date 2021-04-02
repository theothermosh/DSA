# A function that finds an element from an array using linear search algorithm
# The function takes a list and an integer as arguments and returns the index
# of the integer if found in the list. If not found, returns -1.

def linear_search(array, element_to_find):
    array_size = len(array)
    
    for index in range(array_size):
        if array[index] == element_to_find:
            return index # If the element passed as parameter is found,
                         # returns the index at which it is found
    return -1 # If the element is absent in the list, returns -1