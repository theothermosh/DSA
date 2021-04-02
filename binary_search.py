# A function that finds an element from an array using binary search algorithm
# The function takes a list and an integer as arguments and returns the index
# of the integer if found in the list. If not found, returns -1.

def binary_search(array, element_to_find):
    array_size = len(array)
    left, right = 0, array_size - 1 # left and right keeps track of the two ends of the list

    while left <= right:
        mid = left + right // 2

        if array[mid] == element_to_find:
            return mid # element has been found in the mid position of the list
        
        elif array[mid] < element_to_find:
            left = mid + 1 # discards the elements at the left side of mid position as the required element
                           # must be in the right side as it is larger than the element at mid position
        else:
            right = mid - 1 # discards the elements at the right side of mid position as the required element
                            # must be in the left side as it is smaller than the element at mid position
    
    return -1 # If the element is absent in the list, returns -1