from my_array_deque import ArrayDeque
from my_linked_list import LinkedList

class Queue:
    '''A collection of objects that are inserted and removed according to the first-in, first-out (FIFO) principle'''
    
    def __init__(self,type=""):  
        if type == "linked":
            self.queue = LinkedList()
        elif type == "array":
            self.queue = ArrayDeque()

    def add(self,data):
        '''Takes a parameter and adds its value to the back of the queue'''
        return self.queue.push_back(data)
        
    def remove(self):
        '''Removes the item off the front of the queue and returns its value'''
        return self.queue.pop_front()

    def get_size(self):
        '''Returns the number of items currently in the list'''
        return self.queue.get_size()
    
    