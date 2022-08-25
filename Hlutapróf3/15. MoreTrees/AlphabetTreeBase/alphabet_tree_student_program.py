
import sys

class AlphabetTree:
    def __init__(self):
        #TODO: Implement
        pass

    def add_word(self, word):
        #TODO: Implement
        pass
    
    def print_all(self):
        #TODO: Implement
        pass

    def print_leaves(self):
        #TODO: Implement
        pass



if __name__ == "__main__":
    file = open(sys.path[0] + "/alphabet_words.txt")
    
    tree = AlphabetTree()
    
    for line in file:
        tree.add_word(line.strip())
    
    tree.print_all()
    tree.print_leaves()
    
    file.close()
