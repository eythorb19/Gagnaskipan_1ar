
def modulus(a, b):  # ONLY NEEDS TO WORK FOR POSITIVE INTEGERS
    """Calculates the modulus of two integers a,b."""
    if a-b == b or a-b<0:
        return 0
    elif a-b <b:
        return a-b
    else:
        return modulus(a-b,b)

def how_many(lis1, lis2, index = 0):
    """takes two lists and returns an integer which is how many of the items in lis1 are also in lis2."""
    
    my_lis1 = lis1[:]
    my_lis2 = lis2[:]
    
    if index == len(my_lis1):
        return index
    
    is_in = False
    for i in range(len(my_lis2)):
        if my_lis1[index] == my_lis2[i]:
            is_in = True
        
    if is_in == False:
        del my_lis1[index]
        return how_many(my_lis1,my_lis2,index)
    else:
        index+=1
        return how_many(my_lis1,my_lis2,index)


# FEEL FREE TO EDIT THE TESTS AND MAKE THEM BETTER
# REMEMBER EDGE CASES!

def test_modulus(num1, num2):
    print("The modulus of " + str(num1) + " and " + str(num2) + " is " + str(modulus(num1, num2)))

def test_how_many(lis1, lis2):
    print(str(how_many(lis1, lis2)) + " of the items in " + str(lis1) + " are also in " + str(lis2))

def run_recursion_program():

    print("\nTESTING MODULUS:\n")

    test_modulus(8, 3)
    test_modulus(9, 3)
    test_modulus(10, 3)
    test_modulus(11, 3)
    test_modulus(8, 2)
    test_modulus(0, 7)
    test_modulus(15, 5)
    test_modulus(128, 16)
    test_modulus(128, 15)

    print("\nTESTING HOW MANY:\n")

    test_how_many(['a', 'f', 'd', 't'], ['a', 'b', 'c', 'd', 'e'])
    test_how_many(['a', 'b', 'f', 'g', 'a', 't', 'c'], ['a', 'b', 'c', 'd', 'e'])
    test_how_many(['f', 'g', 't'], ['a', 'b', 'c', 'd', 'e'])


if __name__ == "__main__":
    run_recursion_program()