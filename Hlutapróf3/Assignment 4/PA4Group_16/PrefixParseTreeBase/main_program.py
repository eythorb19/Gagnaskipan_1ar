
import sys
from enum import Enum

class DivisionByZero(Exception):
    pass

class UnknownInTree(Exception):
    pass

class OutputFormat(Enum):
    PREFIX = 0
    INFIX = 1
    POSTFIX = 2


class Expr_node():
    def __init__(self,value=None):
        self.left = None
        self.right = None
        self.value = value
        self.format = 0
        self.operator = ['+','-','/','*'] 


    def __str__(self):
        
        space = " "
        if self.value in self.operator:                 #checks if value is a operator 
            self.right.format = self.format
            self.left.format = self.format
            if self.format == 0:                        #if print format is OutputFormat.PREFIX
                return str(self.value) + space + str(self.left) + space + str(self.right)
            
            elif self.format == 1:                      #if print format is OutputFormat.INFIX 
                return "(" + str(self.left) + space + str(self.value) + space + str(self.right) + ")"
            
            elif self.format == 2:                      #if print format is OutputFormat.POSTFIX 
                return str(self.left) + space + str(self.right) + space + str(self.value)
        
        else:                                           #if value is variable unknown or a number
            return str(self.value)


    def eval(self):
        if self.isnumber():                                 #checks if self.value is a number
            return self.value
        
        elif self.value not in self.operator:               #if value is not a number and not in operator it is a unknown verible 
            return 0                                        #to calculate the root it is given 0 to find diffence of root with and without unkown variable
        
        else:                                               
            left = self.left.eval()                          #find total of left
            right = self.right.eval()                        #find total of right

            if self.value == '+':                            #depanding on what operator is given what methood is used
                result = left + right
            
            elif self.value == '-':
                result = left - right
            
            elif self.value == '/':
                if left == right:
                    return 1
                if right == 0 or right == 0.0:              #here I find DivisionByZero error
                    raise DivisionByZero()
                else:
                    result = left / right
            
            elif self.value == '*':
                result = left * right
            
            return result

    def isnumber(self,left=None,right=None):                #this function is used to find out if self.value of current node or left or right is int or a float
        
        if left:
            return isinstance(self.left.value, int) or isinstance(self.left.value, float) or self.left.value == 0
        elif right:
            return isinstance(self.right.value, int) or isinstance(self.right.value, float) or self.right.value == 0
        else:
            return isinstance(self.value, int) or isinstance(self.value, float)
            
            




class PrefixParseTree:
    def __init__(self):
        self.statement = None
        self.position = 0
        self.unknown = False
        self.format = 0
        self.operator = ['+','-','/','*'] 


    def load_statement_string(self, statement):
        self.statement = statement
        self.root = self.create_tree_recursive()
        


    def create_tree_recursive(self):
        current_token = self.get_next_token()
                
        if current_token == None:
            return None

        if current_token in self.operator:
            node = Expr_node(current_token)

            node.left=self.create_tree_recursive()
            node.right=self.create_tree_recursive()
        
        else: 
            a_type=self.check_if_number(current_token)                          
            if not a_type:
                self.unknown = True
                node = Expr_node(current_token)
            else:
                node = Expr_node(a_type(current_token))
                
            return node
        return node

    def check_if_number(self, number):                              #checks if token is a number and if so it returns what type, float or int.
        try:
            if int(number) or number=='0':
                return int
        except:
            return False
        
        try:
            if float(number):
                return float
        except:
            return False

    def get_next_token(self):
        i = self.position
        while i < len(self.statement) and self.statement[i] != " ":
            i += 1
        ret_val = self.statement[self.position:i]
        self.position = i + 1
        return ret_val

    def set_format(self, out_format):
        format_value = out_format.value
        self.format= format_value

    def root_value(self):
        if self.unknown:
            raise UnknownInTree()
        return self.root.eval()

    def simplify_recursiv(self,node):
        
        if node.isnumber():
            return node.value
        elif node.value not in self.operator:
            return

        if node.isnumber(left=True) and node.isnumber(right=True):
            left = node.left.value
            right = node.right.value
            if node.value == "/" and right == 0:
                pass
            else:
                node.value= self.calculate(node.value, left, right)
                node.left = None
                node.right = None
                
        elif node.value:
            self.simplify_recursiv(node.left)
            self.simplify_recursiv(node.right)
            if node.isnumber(left=True) and node.isnumber(right=True):
                self.simplify_recursiv(node)




    def simplify_tree(self):
        self.simplify_recursiv(self.root)

    def calculate(self, op, left, right):                               #takes in two values and operator and finds result
        if op == '+':
            result = left + right
                
        elif op == '-':
            result = left - right
        
        elif op == '*':
            result = left * right
        
        elif op == '/':
            result = left / right
            
        return result

    def solve_tree(self, root_value):
        return  abs(self.root.eval() - root_value) 

    def __str__(self):
        self.root.format = self.format
        return str(self.root)





def test_prefix_parser(str_statement, solve = False, root_value = 0):

    if solve == True:
        prefix_tree = PrefixParseTree()
        prefix_tree.load_statement_string(str_statement)
        print("PREFIX: " + str(prefix_tree))
        print("The value of x if the root_value is " + str(root_value) + " is: " + str(prefix_tree.solve_tree(root_value)))
    else:
        prefix_tree = PrefixParseTree()
        prefix_tree.load_statement_string(str_statement)
        print("PREFIX: " + str(prefix_tree))
        prefix_tree.set_format(OutputFormat.INFIX)
        print("INFIX: " + str(prefix_tree))
        prefix_tree.set_format(OutputFormat.POSTFIX)
        print("POSTFIX: " + str(prefix_tree))

        str_print = "The value of the tree is: "
        try:
            str_print += str(prefix_tree.root_value())
        except DivisionByZero:
            str_print += str("A division by zero occurred")
        except UnknownInTree:
            str_print += str("There is an unknown value in the tree")
        print(str_print)

        print("SIMPLIFIED:")
        prefix_tree.simplify_tree()
        prefix_tree.set_format(OutputFormat.PREFIX)
        print("PREFIX: " + str(prefix_tree))
        prefix_tree.set_format(OutputFormat.INFIX)
        print("INFIX: " + str(prefix_tree))
        prefix_tree.set_format(OutputFormat.POSTFIX)
        print("POSTFIX: " + str(prefix_tree))

    print("\n\n")


if __name__ == "__main__":
    org_out = sys.stdout
    fout = open(sys.path[0] + "/parse_out.txt", "w+")
    sys.stdout = fout
    f = open(sys.path[0] + "/prefix_statements.txt", "r")
    previous_line = None
    for line in f:
        some_split = line.split()
        if some_split[0] == "solve":
            test_prefix_parser(previous_line.strip(), True, int(some_split[1]))
        test_prefix_parser(line.strip())
        previous_line = line
    f.close()
    sys.stdout = org_out
    fout.close()



