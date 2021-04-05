# A class to implement the queue data structure using python list

class Queue:
    # constructor initiating an empty list as queue
    def __init__(self):
        self.items = []

    # places a new item at the back of queue
    def enqueue(self, item):
        self.items.insert(0, item)
    
    # removes the frontmost item from queue and returns it
    def dequeue(self):
        return self.items.pop()

    # returns True if the queue is empty, False otherwise
    def is_empty(self):
        return self.items == []
    
    # returns the number of items present in queue
    def size(self):
        return len(self.items)

    # returns a list containing all the elements of the queue in the reverse order
    def traverse(self):
        q_items = []
        for item in self.items:
            q_items.append(item)
        return q_items