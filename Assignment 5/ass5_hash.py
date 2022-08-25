import random

class NotFoundException(Exception):
    pass
class ItemExistsException(Exception):
    pass

# Helper functions
class Node:
    '''Stores a reference to an object that is an element of a sequence, as well as a reference to the next node of the list'''
    def __init__(self, key = None, data = None, next = None):
        self.key = key
        self.data = data
        self.next = next

class LinkedList():
    '''A collection of nodes that collectively form a linear sequence.'''
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        '''Returns a string with all the items in the list, separated by a single space.'''
        return_string = ""
        node = self.head
        while node != None:
            return_string += "(" + str(node.key) + "," + str(node.data)+ ")" + " "
            node = node.next
        return return_string

    def push_back(self, key, data):
        '''Takes a parameter and adds its value to the back of the list.'''
        new_node = Node(key, data)
        self.size+=1
        if self.head == None:    #Is list empty?
            self.head = new_node
        else:
            self.tail.next = new_node   
        self.tail = new_node    

    def pop_front(self):
        '''Removes the item from the front of the list and returns its value.'''
        if self.head == None:   #Is list empty?
            return None
        self.size-=1

        head = self.head
        pop_val = head.data
        self.head = head.next   
        return pop_val

    def get_size(self):
        '''Returns the number of items currently in the list.'''
        return self.size

# Assignment functions
class Bucket:
    """Bucket implemented with singly-linked list"""

    def __init__(self):
        self.bucket_list = LinkedList()

    def __str__(self):
        return str(self.bucket_list)

    def __setitem__(self, key, data):
        '''Update value if it contains key, otherwise add value pair to collection'''
        if self.contains(key) == True:
            self.update(key,data)
        else:
            self.insert(key,data)

    def __getitem__(self, key):
        '''Return data value of the value pair with equal key'''
        return self.find(key)
        
    def __len__(self):
        return self.bucket_list.get_size()

    def insert(self, key, data):
        '''Adds value pair key,data to the collection'''
        if self.contains(key) == True:
            raise ItemExistsException()
        else:
            self.bucket_list.push_back(key,data)

    def update(self, key, data):
        '''Sets the data value of the value pair with equal key to data'''  
        current_node = self.bucket_list.head
        for _ in range(self.bucket_list.size):
            if current_node.key == key:
                current_node.data = data
                return
            current_node = current_node.next
        raise NotFoundException()

    def find(self, key):
        '''Returns the data value of the value pair with equal key'''
        current_node = self.bucket_list.head
        for _ in range(self.bucket_list.size):
            if current_node.key == key:
                return current_node.data
            current_node = current_node.next
        raise NotFoundException()

    def contains(self, key):
        '''Returns True if equal key is found in the collection, otherwise False.'''
        current_node = self.bucket_list.head
        for _ in range(self.bucket_list.size):
            if current_node.key == key:
                return True
            current_node = current_node.next
        return False

    def remove(self, key):
        '''Removes the value pair with equal key from the collection'''
        current_node = self.bucket_list.head
        if current_node.key == key:
            self.bucket_list.pop_front()
            return
            
        for _ in range(self.bucket_list.size):
            if current_node.key == key:
                if self.bucket_list.size == 1:
                    self.bucket_list.head = self.bucket_list.tail = None
                else:
                    prev_node.next = current_node.next
                self.bucket_list.size-=1
                return
            prev_node = current_node
            current_node = current_node.next
        raise NotFoundException()

class HashMap:
    '''Indexable collection of Bucket'''
    def __init__(self):
        self.hash_length = 16
        self.hash_table =[Bucket() for _ in range(self.hash_length) ]
        self.item_count = 0

    def __str__(self):
        return_string = ""
        for i in range(self.hash_length):
            bucket = self.hash_table[i]
            return_string+= str(bucket) + "\n"
        return return_string

    def __setitem__(self, key, data):
        '''Override to allow this syntax: some_hash_map[key] = data'''
        bucket = self.get_bucket(key)

        if bucket.contains(key) == True:
            self.update(key,data)
        else:
            self.insert(key,data)

    def __getitem__(self, key):
        '''Override to allow this syntax: my_data = some_hash_map[key]'''
        bucket = self.get_bucket(key)
        return bucket.find(key)

    def __len__(self):
        '''Override to allow this syntax: my_data = some_hash_map[key]'''
        return self.item_count

    def rebuild(self):
        '''Doubles the number of buckets in HashTable structure'''
        old_length = self.hash_length
        self.hash_length*=2

        double_hash_table = [Bucket() for _ in range(self.hash_length)]
        for i in range(old_length):
            double_hash_table[i] = self.hash_table[i]

        self.hash_table = double_hash_table

    def insert(self, key, data):
        '''Adds this value pair to the collection'''
        if self.item_count > 1.2*self.hash_length:  #Rebuild if HashMap has reached 120% of number of buckets
            self.rebuild()

        bucket = self.get_bucket(key)
        bucket.insert(key,data)
        self.item_count+=1

    def update(self, key, data):
        '''Sets the data value of the value pair with equal key to data'''
        bucket = self.get_bucket(key)
        bucket.update(key,data)

    def find(self, key):
        '''Returns the data value of the value pair with equal key'''
        bucket = self.get_bucket(key)
        return bucket.find(key)

    def contains(self, key):
        '''Returns True if equal key is found in the collection, otherwise False'''
        bucket = self.get_bucket(key)
        return bucket.contains(key)

    def remove(self, key):
        '''Removes the value pair with equal key from the collection'''
        bucket = self.get_bucket(key)
        bucket.remove(key)
        self.item_count-=1

    def get_bucket(self, key):
        '''Returns bucket at hashed index from key'''
        index = hash(key) % self.hash_length
        bucket = self.hash_table[index]
        return bucket
    
class MyHashableKey:
    '''Integer and string value keys that can be hashed'''
    
    def __init__(self, int_value, string_value):
        self.int_value = int_value
        self.string_value = string_value

    def __eq__(self, other):
        '''Compares two instances of MyHashableKey and returns True if their values are equal, otherwise False'''
        
        if hash(self) == hash(other):
            return True
        else:
            return False

    def __hash__(self):
        hash_value = 0
        for i in range(len(self.string_value)):
            hash_value+= ord(self.string_value[i])
        hash_value+=self.int_value
        return hash_value
