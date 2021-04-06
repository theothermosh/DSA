# A class that implements the deque (double-ended queue)
# data structure using python list

class Deque:
    # constructor initiating an empty list as deque
    def __init__(self):
        self.items = []
    
    # adds a new item at the front of the deque
    def push_front(self, item):
        self.items.append(item)

    # adds a new item at the back of the deque
    def push_rear(self, item):
        self.items.insert(0, item)
    
    # removes the item at the front of the deque
    def pop_front(self):
        return self.items.pop()

    # removes the item at the rear of the deque
    def pop_rear(self):
        return self.items.pop(0)

    # returns True is the deque is empty, False otherwise
    def is_empty(self):
        return self.items == []

    # returns the number of items present in dequeue
    def size(self):
        return len(self.items)

    # returns a list containing all the elements of the deque
    def traverse(self):
        deque_items = []
        for item in self.items:
            deque_items.append(item)
        return deque_items