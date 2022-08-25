
class MyComparableKey:
    def __init__(self, int_value, string_value):
        self.i = int_value
        self.s = string_value
    
    def __lt__(self, other):
        if self.i < other.i:
            return True
        elif other.i < self.i:
            return False
        else:
            return self.s < other.s
