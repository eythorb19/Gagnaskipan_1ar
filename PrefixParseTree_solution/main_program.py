import tokenizer
from tokenizer import Tokenizer

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

class TokenType(Enum):
    NUMBER = 0
    OPERATOR = 1
    UNKNOWN = 2

class PrefixNode:
    def __init__(self, token, left = None, right = None, type = TokenType.OPERATOR):
        self.token = token
        self.left = left
        self.right = right
        self.type = type

class PrefixParseTree:
    def __init__(self):
        self.root = None
        self.format = OutputFormat.PREFIX

    def build_tree_recursive(self, tokenizer):
        token = tokenizer.get_next_token()

        if token == "+" or token == "-" or token == "*" or token == "/":
            return PrefixNode(token, self.build_tree_recursive(tokenizer), self.build_tree_recursive(tokenizer))
        elif token.isdigit():
            return PrefixNode(int(token), None, None, TokenType.NUMBER)
        else:
            return PrefixNode(token, None, None, TokenType.UNKNOWN)

    def load_statement_string(self, statement):
        tokenizer = Tokenizer(statement)
        self.root = self.build_tree_recursive(tokenizer)

    def set_format(self, out_format):
        self.format = out_format

    def tree_string(self, node):
        if node == None:
            return ""
        if self.format == OutputFormat.PREFIX:
            return str(node.token) + " " + self.tree_string(node.left) + self.tree_string(node.right)
        elif self.format == OutputFormat.INFIX:
            if node.left != None:
                return "(" + self.tree_string(node.left) + " " + str(node.token) + " " + self.tree_string(node.right) + ")"
            else:
                return str(node.token)
        if self.format == OutputFormat.POSTFIX:
            return self.tree_string(node.left) + self.tree_string(node.right) + str(node.token) + " "

    def node_value_recursive(self, node):
        if node.type == TokenType.NUMBER:
            return node.token
        elif node.type == TokenType.OPERATOR:
            if node.token == "+":
                return self.node_value_recursive(node.left) + self.node_value_recursive(node.right)
            elif node.token == "-":
                return self.node_value_recursive(node.left) - self.node_value_recursive(node.right)
            elif node.token == "*":
                return self.node_value_recursive(node.left) * self.node_value_recursive(node.right)
            elif node.token == "/":
                val1 = self.node_value_recursive(node.left)
                val2 = self.node_value_recursive(node.right)
                if(val2 == 0):
                    raise DivisionByZero()
                return val1 / val2
        else:
            raise UnknownInTree()

    def root_value(self):
        return self.node_value_recursive(self.root)

    def simplify_node_recursive(self, node):
        if node == None:
            return True
        try:
            left_bool = self.simplify_node_recursive(node.left)
            right_bool = self.simplify_node_recursive(node.right)
            if left_bool and right_bool:
                val = self.node_value_recursive(node)
                node.token = val
                node.left = None
                node.right = None
                node.type = TokenType.NUMBER
                return True
        except DivisionByZero:
            pass
        except UnknownInTree:
            pass
        return False

    def simplify_tree(self):
        self.simplify_node_recursive(self.root)

    def solve_node_recursive(self, node, node_value):
        if node.type == TokenType.UNKNOWN:
            return node_value
        left_value = None
        try:
            left_value = self.node_value_recursive(node.left)
        except UnknownInTree:
            left_value = None
        right_value = None
        try:
            right_value = self.node_value_recursive(node.right)
        except UnknownInTree:
            right_value = None
        if left_value == None and right_value != None:
            if node.token == "+":
                next_value = node_value - right_value
            elif node.token == "-":
                next_value = node_value + right_value
            return self.solve_node_recursive(node.left, next_value)
        elif right_value == None and left_value != None:
            if node.token == "+":
                next_value = node_value - left_value
            if node.token == "-":
                next_value = left_value - node_value
            return self.solve_node_recursive(node.right, next_value)
        else:
            return None
        

    def solve_tree(self, root_value):
        return self.solve_node_recursive(self.root, root_value)

    def __str__(self):
        return self.tree_string(self.root).strip()


# This is a tester function to test that
# the output and/or error message from the
# prefix_parser function are correct.
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


'''
PREFIX: - + - x 5 + 6 3 4
INFIX: (((x - 5) + (6 + 3)) - 4)
POSTFIX: x 5 - 6 3 + + 4 -
The value of the tree is: There is an unknown value in the tree
SIMPLIFIED:
PREFIX: - + - x 5 + 6 3 4
INFIX: (((x - 5) + (6 + 3)) - 4)
POSTFIX: x 5 - 6 3 + + 4 -
'''