class BinaryTreeNode:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def _populate_tree_recur(self):
        data_str = input()
        
        if data_str == "":
            return None

        left = self._populate_tree_recur()
        right = self._populate_tree_recur()
            
        return BinaryTreeNode(data_str, left, right)

    def populate_tree(self):
        self.root = self._populate_tree_recur()

    def _print_tree_recur(self,node):
        if node == None:
            return 
        
        self._print_tree_recur(node.left)
        self._print_tree_recur(node.right)
        print(str(node.data), end =  " ")

    def print_tree(self):
        self._print_tree_recur(self.root)
        print(" ")

if __name__ == "__main__":
    bt = BinaryTree()
    bt.populate_tree()
    bt.print_tree()
