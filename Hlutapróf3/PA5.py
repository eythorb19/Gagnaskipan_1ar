class NotFoundException(Exception):
    pass

class Key():
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def update(self,key, value):
        if key==self.key:
            self.value = value
        else:
            print ("value can not be updated. Keys don't match!")

    # def return_value(self):
    #     return self.value

    # def return_key(self):
    #     return self.key

    def __str__(self):
        return str(self.value)

class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        
        self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None


    def push_back(self, data):
        new_node = Node (data)
        if self.head == None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node


    def push_front(self, data):
        new_node = Node (data)
        if self.head == None:
            self.tail = new_node
        else:
            new_node.next = self.head
        self.head = new_node

    def give_next(self, node):
        return node.next

    def get_size(self):
        node = self.head
        counter = 0
        while node != None:
            counter += 1
            node = node.next
        return counter


    def pop_front (self):
        if self.head == None:
            return None
        else:
            return_value = self.head.data
            self.head = self.head.next
            return return_value

    def pop_back(self):
        current_node = self.head
        return_value = self.tail
        if current_node == None:
            return None
        elif current_node == return_value:
            self.head = None
            self.tail = None
            return return_value.data

        while True:
            if current_node.next == return_value:
                current_node.next = None
                self.tail = current_node
                return return_value.data
            else:
                current_node = current_node.next


    def give_next(self):
        return self.head.next

    def __str__(self):
        node = self.head
        return_str = ""
        while node != None:
            return_str += str(node.data) + " "
            node = node.next
        return return_str

class Bucket():
#with a ​ singly-linked list ​ .
#The class must fully implement the ​ Map​ ADT, including the following operations:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count =  0

 
    def  insert(self,key, data):
    #○ Adds this value pair to the collection
    #○ If equal key is already in the collection, raise ItemExistsException()'''
        new_key = Key(key, data)
        if self.head == None:
            self.head = Node(new_key)
            self.tail = self.head
            self.count = 1
            
        else:
            self.tail.next = Node(new_key)
            self.tail = self.tail.next
            self.count += 1


    def  update(self,key, value):
    #'''○ Sets the data value of the value pair with equal ​ key ​ to ​ data
    #○ If equal key is not in the collection, ​ raise NotFoundException()'''
        node_check = self.head
        while node_check != None or found:
            if node_check.data.key == key:
                node_check.data.update(key, value)
                break
            else:
                node_check = node_check.next
        else:
            raise NotFoundException()

    def  find(self, key):
    #'''○ Returns the ​ value ​ value of the value pair with equal ​ key
    #○ If equal key is not in the collection, ​ raise NotFoundException()'''
        node_check = self.head
        while node_check != None:
            if node_check.data.key == key:
                return node_check.data.value
            else:
                node_check = node_check.next
        else:
            raise NotFoundException()


    def  contains(self, key):
    #'''○ Returns ​ True ​ if equal ​ key ​ is found in the collection, otherwise ​ False'''
        node_check = self.head
        while node_check != None:
            if node_check.data.key == key:
                return True
            else:
                node_check = node_check.next
        else:
            return False

    def  remove(self, key):
    #'''○ Removes the value pair with equal ​ key ​ from the collection
    #○ If equal key is not in the collection, ​ raise NotFoundException()'''
        if self.head.data.key == key:
            self.head = self.head.next
            return
        
        node_check_prev = self.head
        node_check = self.head.next
        while node_check != None:
            if node_check.data.key == key:
                node_check_prev.next = node_check.next
            else:
                node_check_prev = node_check_prev.next
                node_check = node_check.next

    def  __setitem__(self, key, data):
    #'''○ Override to allow this syntax:
    #■ some_hash_map[ ​ key ​ ] = ​ data
    #○ If equal ​ key ​ is already in the collection, update its ​ data ​ value
    #■ Otherwise add the value pair to the collection'''
        pass

    def  __getitem__(self, key):
    #'''○ Override to allow this syntax:
    #■ my_data = some_bucket[ ​ key ] ​
    #○ Returns the ​ data ​ value of the value pair with equal ​ key
    #○ If equal key is not in the collection, ​ raise NotFoundException()'''
        pass

    def  __len__(self):
    #'''○ Override to allow this syntax:
    #■ length_of_structure = len(some_bucket)
    #○ Returns the number of items in the entire data structure'''
        pass

    def __str__(self):
        node = self.head
        return_str = ""
        while node != None:
            return_str += str(node.data) + " "
            node = node.next
        return return_str


if __name__ == "__main__":
    test = Bucket()
    test.insert(5, 'fimm')
    test.insert(4, 'fjorir')
    test.insert(3,'trir')
    print(test)
    test.update(3, 'thrir')
    print(test)
    print(test.find(3))
    print(test.contains(3))
    print(test.remove(3))
    print(test)