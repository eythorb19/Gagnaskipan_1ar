from my_array_deque import ArrayDeque
from my_linked_list import LinkedList

class Stack:
    '''A collection of objects that are inserted and removed according to the last-in, first-out (LIFO) principle'''

    def __init__(self,type=""):  
        if type == "linked":
            self.stack = LinkedList()
        elif type == "array":
            self.stack = ArrayDeque()

    def push(self,data):
        '''Takes a parameter and adds its value onto the stack'''
        return self.stack.push_front(data)

    def pop(self):
        '''Removes the item off the top of the stack and returns its value'''
        return self.stack.pop_front()

    def get_size(self):
        '''Returns the number of items currently in the list'''
        return self.stack.get_size()
    
    