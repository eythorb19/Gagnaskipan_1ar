from timer import *
from random import *

'''Power (also done in teacher’s video)
○ Make a function that takes two parameters (the second one a positive integer)
○ Return the result of raising the first parameter to the power of the second
'''

#Tímaflækja O(n)
def power(a, b):
    '''
    Computes a^b.
    Time complexity O(n)
    '''
    num = 1
    for i in range(b):
        num *= a
    return num

'''● Multiplication of positive integers
○ Make a function that takes two parameters
○ Return the result from multiplying the two integer parameters with each other
○ The only math operators you may use in your implementation are + and -'''

#Tímaflækja O(n)
def multiply(a,b):
    '''
    Multiplies a*b. \\
    Time complexty O(n)
    '''

    num = 0
    for i in range(b):
        num += a
    return num

'''Random number insertion
○ Build a list of a certain size (lis = [0] * size)
○ Traverse list and for each location in the list:
■ Random generate number between 1 and 6
■ Put the number in the “current” location
'''

def build_list(size):
    '''
    Build list of certain size and fill with random numbers between 1 and 6. \\
    Time complexity: O(n)
    '''
    lst = [None]*size

    for i in range(size):
        value = random()
        scaled_value = 6 + (value * (10 - 6))
        lst[i] = scaled_value
    return lst


'''Switch items in list
○ Generate and fill a list of some size
○ Pick a location in the list
■ Switch the value in that location with the location next to it
○ Randomly pick two locations in the list
■ Switch the values in the two locations
'''

def switch_items_in_list(size,location):
    '''
    Generates list of specific size and fills with random numbers. \\
    Switches number in specified location with the number next to it.
    '''
    lst = build_list(size)

    print("Before:")
    print(lst)
    switch = lst[location]
    lst[location] = lst[location+1]
    lst[location+1] = switch
    print("After:")
    print(lst)
    return lst

def switch_random_items_in_list(size):
    '''
    Generates list of specific size and fills with random numbers. \\
    Switches number in random location with the number next to it.
    '''
    lst = build_list(size)
    print("Before:")
    print(lst)
    random_location = randint(0,size)
    switch = lst[random_location]
    lst[random_location] = lst[random_location +1]
    lst[random_location +1] = switch
    print("After:")
    print(lst)

    return lst

'''
● Ordered insertion
○ Random generate a number between 1 and 6
○ Put the number in the correct location so that the list is ordered
'''  

def ordered_instertion(size):
    lst = build_list(size)
    
    for i in range(size):
        if lst[i] > lst[i+1]:
            switch_items_in_list(size,lst[i])
    return lst    
    






    
'''
Combined insertion and ordering
○ First fill a list with random number insertion
○ Then for each element in that list
■ Add the number into another list with ordered insertion
'''



#Test power
print("")
print("Power:")
print("")
power_timer = Timer()
power_timer.start()
power1 = power(3,3)
elapsed = power_timer.elapsed()
print(power1)
print("Tíminn: " + str(elapsed))

#Test multiply
print("")
print("Multiply:")
print("")
multiply_timer = Timer()
multiply_timer.start()
multiply1 = multiply(2,4)
elapsed = multiply_timer.elapsed()
print(multiply1)
print("Tíminn: " + str(elapsed))

#Test build_list
print("")
print("Build list:")
print("")
list_timer = Timer()
list_timer.start()
list1 = build_list(5)
elapsed = list_timer.elapsed()
print(list1)
print("Tíminn: " + str(elapsed))

#Test switch_items_in_list
print("")
print("Switch items in list:")
print("")
switch_timer = Timer()
switch_timer.start()
switch1 = switch_items_in_list(5,2)
elapsed = switch_timer.elapsed()
print("Tíminn: " + str(elapsed))

#Test switch_random_items_in_list
print("")
print("Switch random items in list:")
print("")
switch_random_timer = Timer()
switch_random_timer.start()
switch1 = switch_random_items_in_list(5)
elapsed = switch_random_timer.elapsed()
print("Tíminn: " + str(elapsed))

#Test ordered_insertion
print("")
print("Order list in increasing order")
print("")
switch_order_timer = Timer()
switch_order_timer.start()
order1 = ordered_instertion(5)
elapsed = switch_order_timer.elapsed()
print("Tíminn: " + str(elapsed))





