
import sys

class TreeNode:
    def __init__(self, data = ""):
        self.data = data
        self.children = []
    
    def add_word(self, word, length = 1):

        # BASE CASE - WHOLE WORD DONE
        if length > len(word):
            return

        word_part = word[:length]

        # RECURSE INTO CORRECT CHILD IF FOUND
        for child in self.children:
            if child.data == word_part:
                child.add_word(word, length + 1)
                return

        # IF NOT FOUND MAKE NEW CHILD AND RECURSE
        child = TreeNode(word_part)

        for index in range(len(self.children)):
            if self.children[index].data > word_part:
                self.children.insert(index, child)
                child.add_word(word, length + 1)
                return

        self.children.append(child)
        child.add_word(word, length + 1)
    
    def print_preorder(self):
        print(self.data)
        for child in self.children:
            child.print_preorder()

    def print_leaves(self):
        if len(self.children) == 0:
            print(self.data)
        for child in self.children:
            child.print_leaves()

class AlphabetTree:
    def __init__(self):
        self.root = TreeNode()

    def add_word(self, word):
        self.root.add_word(word)
    
    def print_all(self):
        self.root.print_preorder()

    def print_leaves(self):
        self.root.print_leaves()



if __name__ == "__main__":
    file = open(sys.path[0] + "/alphabet_words.txt")
    
    tree = AlphabetTree()
    
    for line in file:
        tree.add_word(line.strip())
    
    tree.print_all()
    tree.print_leaves()
    
    file.close()
