import unittest
class Pizza:
    '''
    Class that keeps track of pizzas, toppings and if they´re served or not.
    '''

    def __init__(self,id,toppings = list):
        self.toppings = toppings
        self.id = id
        self.is_served = False

    def __str__(self):
        pass

    def served(self):
        self.is_served = True


class Test(unittest.TestCase):
    
    def setUp(self):
        self.pizza = Pizza(1,"pepp")
        self.pizza.served()

    def test_served(self):
        self.assertEqual(self.pizza.is_served,True)

if __name__ == "__main__":
    unittest.main()


