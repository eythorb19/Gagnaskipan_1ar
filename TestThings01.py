class ArrayList:
    def __init__(self):
        self.capacity = 4
        self.size = 0
        self.arr = [0] * self.capacity


def append(array_list,value):
    array_list.arr[array_list.size] = value
    array_list.size += 1

def print_array(array_list):
    for i in range(array_list.size):
        str_val += str(array_list.arr[i])
    print(str_val)

def resize(array_list):
    array_list.arr *=2
    array_list.capacity *=2


array_list = ArrayList()
append(array_list,4)
append(array_list,2)
append(array_list,7)

print(array_list.arr)




