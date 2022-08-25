
class BinaryTreeNode:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def _populate_tree_recur(self, level = 0):
        data_str = input()
        if data_str == "":
            return None
        level += 1
        print(level*"   |" + "--LEFT :", end = " ")
        left_node = self._populate_tree_recur(level)
        print(level*"   |" + "--RIGHT:", end = " ")
        right_node = self._populate_tree_recur(level)
        return BinaryTreeNode(data_str, left_node, right_node)

    def populate_tree(self):
        print("ROOT :", end = " ")
        self.root = self._populate_tree_recur()

    def _print_preorder_recur(self, node):
        if node == None:
            return
        print(str(node.data), end = " ")
        self._print_preorder_recur(node.left)
        self._print_preorder_recur(node.right)

    def print_preorder(self):
        self._print_preorder_recur(self.root)
        print("")

    def _print_inorder_recur(self, node):
        if node == None:
            return
        self._print_inorder_recur(node.left)
        print(str(node.data), end = " ")
        self._print_inorder_recur(node.right)

    def print_inorder(self):
        self._print_inorder_recur(self.root)
        print("")

    def _print_postorder_recur(self, node):
        if node == None:
            return
        self._print_postorder_recur(node.left)
        self._print_postorder_recur(node.right)
        print(str(node.data), end = " ")

    def print_postorder(self):
        self._print_postorder_recur(self.root)
        print("")

if __name__ == "__main__":
    print("\nTESTING BINARY TREE\n")
    bt = BinaryTree()
    bt.populate_tree()
    print("preorder :", end = " ")
    bt.print_preorder()
    print("inorder  :", end = " ")
    bt.print_inorder()
    print("postorder:", end = " ")
    bt.print_postorder()


class GeneralTreeNode:
    def __init__(self, data = None):
        self.data = data
        self.children = []


class GeneralTree:
    def __init__(self):
        self.root = None

    def _populate_tree_recur(self, level = 0):
        data_str = input()
        if data_str == "":
            return None
        node = GeneralTreeNode(data_str)
        level += 1
        while True:
            print(level*"   |" + "--NODE :", end = " ")
            child_node = self._populate_tree_recur(level)
            if child_node == None:
                break
            node.children.append(child_node)
        return node

    def populate_tree(self):
        print("ROOT :", end = " ")
        self.root = self._populate_tree_recur()

    def _print_preorder_recur(self, node):
        if node == None:
            return
        print(str(node.data), end = " ")
        for child_node in node.children:
            self._print_preorder_recur(child_node)

    def print_preorder(self):
        self._print_preorder_recur(self.root)
        print("")

    def _print_postorder_recur(self, node):
        if node == None:
            return
        for child_node in node.children:
            self._print_postorder_recur(child_node)
        print(str(node.data), end = " ")

    def print_postorder(self):
        self._print_postorder_recur(self.root)
        print("")


if __name__ == "__main__":
    print("\nTESTING GENERAL TREE\n")
    bt = GeneralTree()
    bt.populate_tree()
    print("preorder :", end = " ")
    bt.print_preorder()
    print("postorder:", end = " ")
    bt.print_postorder()

