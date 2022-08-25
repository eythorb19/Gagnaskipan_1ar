class IndexOutOfBounds(Exception):
    pass

class NotFound(Exception):
    pass

class Empty(Exception):
    pass

class NotOrdered(Exception):
    pass

class ArrayList:
    def __init__(self):
        self.capacity = 4
        self.size = 0
        self.arr = [0] * self.capacity
        self.ordered = True
        
    #Time complexity: O(n) - linear time in size of list
    def __str__(self):
        """Returns string with comma separated items from array"""

        return_string = ""
        for i in range(self.size-1):
            val = str(self.arr[i])
            return_string += val + ", "

        if self.size >0:
            return_string += str(self.arr[self.size-1])
        return return_string

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        """Inserts an item into the list before the first item"""

        if self.size == self.capacity: #Resize if capacity fully utilized
            self.resize()
        
        self.size+=1
        for i in range(self.size,1,-1):
            self.arr[i-1] = self.arr[i-2] 
        self.arr[0] = value

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        """Insert value to list at a given index."""
            
        if self.size == self.capacity:
            self.resize()

        if not (0 <= index <= self.size): #If index not within current list OutOfBounds
            raise IndexOutOfBounds()

        elif index == 0:    #Index at the start of list  
            self.prepend(value)

        elif index == self.size:  #Index at the end of list
            self.append(value)

        else:   #Index between, not at start or end
            self.size+=1
            for i in range(self.size,index,-1):      
                self.arr[i-1] = self.arr[i-2]
            self.arr[index] = value     

    #Time complexity: O(1) - constant time
    def append(self, value):
        """Adds a defined value at the back of a list"""

        if self.size == self.capacity:
            self.resize()
        self.size+=1    
        self.arr[self.size-1] = value

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        """Sets the value at a specific location to a specific value"""

        if not 0 <= index <= self.size-1:
            raise IndexOutOfBounds()
        
        self.arr[index] = value

    #Time complexity: O(1) - constant time
    def get_first(self):
        """Returns the first value in the list"""

        if self.size == 0:
            raise Empty()
        return self.arr[0]

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        """Returns a value from list at a specific index."""

        if not (0<= index <= self.size-1):
            raise IndexOutOfBounds()

        return self.arr[index]

    #Time complexity: O(1) - constant time
    def get_last(self):
        """Returns the last value in the list"""
        if self.size == 0:
            raise Empty()
        return self.arr[self.size-1]

    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        """Doubles the size of an array"""
        self.capacity *= 2
        new_arr =[0]*self.capacity

        for i in range(self.size):
            new_arr[i] = self.arr[i]
        
        self.arr = new_arr
        return self.arr

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        """Removes from the list an item at a specific location"""

        if not (0<= index <= self.size-1):
            raise IndexOutOfBounds()
        
        new_arr =[0]*self.capacity
        j = 0
        for i in range(self.size):
            if i == index:
                i-=1
            else:
                new_arr[j] = self.arr[i]
                j+=1
        self.arr = new_arr
        self.size -=1

    def is_ordered(self):
        """Checks if list is ordered. Sets attribute ordered to T or F"""

        self.ordered = True
        value = self.arr[0]

        for i in range(1,self.size):
            if self.arr[i] < value:
                self.ordered = False
                break
            else:
                value = self.arr[i]

    #Time complexity: O(1) - constant time
    def clear(self):
        """Removes all items from the list"""
        
        self.capacity = 4
        self.size = 0
        new_arr = [0]*self.capacity
        self.arr = new_arr

    #Time complexity: O(n) - linear time in size of list
    def insert_ordered(self, value):
        """Inserts value in ordered list."""
        self.is_ordered()

        if self.ordered == False:
            raise NotOrdered()
        else:
            if self.size == 0:
                self.append(value)
                return
            else:
                for i in range(self.size):
                    comp_value = self.arr[i]
                    if comp_value >= value:
                        self.insert(value,i)
                        return
                    
        self.insert(value,self.size)

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value):
        """Searches for specific value in list. Returns index"""

        self.is_ordered()
        if self.ordered ==True:
            return self.binary_search(0,self.size-1,value)
        else:
            return self.linear_search(value,0)
    
    def binary_search(self,lower,upper,value):
        """Binary search for specific value in ordered list. Returns index."""
        
        mid_index = lower + ((upper-lower)//2)
        mid_val = self.arr[mid_index]

        if upper < 0:
            upper = 0
        
        if value == mid_val:
            return mid_index
        if lower == upper:
            raise NotFound()
        elif value > mid_val:
            return self.binary_search(mid_index+1,upper,value)
        else:
            return self.binary_search(lower,mid_index-1,value)  

    def linear_search(self,value, index):
        """Linear search for specific value in unordered list. Returns index."""
        
        if index == self.size:
            raise NotFound

        elif self.arr[index] == value:
            return index

        else:
            return self.linear_search(value,index+1)

    #Time complexity: O(n) - linear time in size of list
    def remove_value(self, value):
        """Removes specific value from list."""

        index = self.find(value)
        self.remove_at(index)

if __name__ == "__main__":
    pass
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level
