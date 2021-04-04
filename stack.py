# A class that implements the stack data structure using python list

class Stack:
    # constructor initiating an empty list as stack
    def __init__(self):
        self.items = []
    
    # adds an element to the top of the stack
    def push(self, item):
        self.items.append(item)

    # returns the top item from the stack after removing it
    def pop(self):
        return self.items.pop()

    # returns True if the stack is empty
    def is_empty(self):
        return self.items == []

    # returns the top item from the stack without removing it
    def peek_top(self):
        return self.items[len(self.items) - 1]

    # returns the number of elements present in the stack
    def size(self):
        return len(self.items)

    # returns the element that was first kept in the stack
    def peek_bottom(self):
        return self.items[0]

    # returns a list containing all the elements of the stack in the order they are kept
    def traverse(self):
        stack_items = []
        for item in self.items:
            stack_items.append(item)
        return stack_items