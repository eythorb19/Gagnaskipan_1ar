
class Node:
    '''Stores a reference to an object that is an element of a sequence, as well as a reference to the next node of the list'''
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next

class LinkedList():
    '''A collection of nodes that collectively form a linear sequence.'''
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        '''Returns a string with all the items in the list, separated by a single space.'''
        return_string = ""
        node = self.head
        while node != None:
            return_string += str(node.data) + " "
            node = node.next
        return return_string

    def push_back(self,data):
        '''Takes a parameter and adds its value to the back of the list.'''
        new_node = Node(data)
        if self.head == None:    #Is list empty?
            self.head = new_node
        else:
            self.tail.next = new_node   
        self.tail = new_node    

    def push_front(self,data):
        '''Takes a parameter and adds its value to the front of the list.'''
        new_node = Node(data,self.head) #current head becomes new_node.next
        self.head = new_node

    def pop_front(self):
        '''Removes the item from the front of the list and returns its value.'''
        if self.head == None:   #Is list empty?
            return None

        head = self.head
        pop_val = head.data
        self.head = head.next   
        return pop_val

    def get_size(self):
        '''Returns the number of items currently in the list.'''
        curr = self.head
        size = self.count_nodes(curr)
        return size
        
    def count_nodes(self,curr,count=0):
        '''Counts nodes recursively'''
        if curr == None:    #Are we at the end of the list?
            return count
        else:
            return self.count_nodes(curr.next, count + 1) 


if __name__ == "__main__":
    pass