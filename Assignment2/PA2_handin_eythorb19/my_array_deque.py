
class ArrayDeque():
    '''A Double ended queue.'''

    def __init__(self):
        self.capacity = 8
        self.arr = [None] * self.capacity
        self.end_index = 0
        self.start_index = 0
        self.full = False   #To distinct between full and empty, when start and end indexes are equal.

    def __str__(self):
        '''Returns a string with all the items in the list, separated by a single space.'''
        return_string = ""
        size = self.get_size()

        if size > 0:
            index = self.start_index
            for i in range(size-1):
                val = str(self.arr[index])
                return_string+= val + " "

                if index == self.capacity-1:
                    index = 0
                else:
                    index+=1
            return_string += str(self.arr[index])
        return return_string

    def push_back(self, value):
        '''Takes a parameter and adds its value to the back of the deque.'''
        size = self.get_size()
        if size == self.capacity:
            self.resize()
            
        self.arr[self.end_index] = value
        if self.end_index == self.capacity-1:
            self.end_index = 0
        else:
            self.end_index+=1

        if self.start_index == self.end_index:
            self.full = True

    def push_front(self,value):
        '''Takes a parameter and adds its value to the front of the deque.'''
        size = self.get_size()
        if size == self.capacity:
            self.resize()

        if self.start_index == 0:
            self.start_index = self.capacity-1
        else:
            self.start_index-=1
        self.arr[self.start_index] = value

        if self.start_index == self.end_index:
            self.full = True

    def pop_back(self):
        '''Removes the item from the back of the deque and returns its value.'''
        size = self.get_size()
        if size == 0:
            return None
        elif self.end_index == 0:
            self.end_index = self.capacity-1
        else:
            self.end_index-=1
        return self.arr[self.end_index]

    def pop_front(self):
        '''Removes the item from the front of the list and returns its value.'''
        size = self.get_size()
        if size == 0:
            return None 

        return_value = self.arr[self.start_index]
        if self.start_index == self.capacity - 1:
            self.start_index = 0
        else:
            self.start_index+=1
        return return_value

    def resize(self):
        '''Doubles the capacity of the array and rearranges with circular buffer method.'''
        old_capacity = self.capacity
        self.capacity *= 2
        new_arr =[None]*self.capacity
        old_index = self.start_index

        if self.start_index != 0:
            self.start_index = old_index + old_capacity
            new_index = self.start_index
        else:
            new_index = old_index

        for i in range(old_capacity):
            new_arr[new_index] = self.arr[old_index]
            if new_index == self.capacity-1:
                new_index=0
                old_index =0
            else:
                new_index+=1
                old_index+=1

        self.full = False
        self.arr = new_arr
        return self.arr

    def get_size(self):
        '''Returns the number of items currently in the deque.'''
        if self.full == True:
            size = self.capacity
        elif self.start_index == self.end_index:
            size = 0
        elif self.start_index < self.end_index:
            size = self.end_index - self.start_index
        else:
            size = (self.capacity - self.start_index) + self.end_index
        return size

if __name__ == "__main__":
    pass

