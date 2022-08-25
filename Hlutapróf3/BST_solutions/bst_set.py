
class BSTSetNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        ret_str = ""
        if self.left != None:
            ret_str += str(self.left)
        ret_str += str(self.value) + " "
        if self.right != None:
            ret_str += str(self.right)
        return ret_str

class BSTSet:
    def __init__(self):
        self.root = None
        self.size = 0

    def _add(self, value, node):
        if node == None:
            self.size += 1
            return BSTSetNode(value)
        elif value < node.value:
            node.left = self._add(value, node.left)
        elif node.value < value:
            node.right = self._add(value, node.right)
        return node

    def add(self, value):
        self.root = self._add(value, self.root)

    def contains(self, value):
        node = self.root
        while node != None:
            if value == node.value:
                return True
            elif value < node.value:
                node = node.left
            else:
                node = node.right
        return False

    def _swap_and_remove_leftmost(self, org_node, node):
        if node.left == None:
            org_node.value = node.value
            return self._remove_node(node)
        else:
            node.left = self._swap_and_remove_leftmost(org_node, node.left)
            return node

    def _remove_node(self, node):
        if node.left == None and node.right == None:
            return None
        elif node.right == None:
            return node.left
        elif node.left == None:
            return node.right
        else:
            node.right = self._swap_and_remove_leftmost(node, node.right)
            return node

    def _remove(self, value, node):
        if node != None:
            if value < node.value:
                node.left = self._remove(value, node.left)
            elif node.value < value:
                node.right = self._remove(value, node.right)
            else:
                self.size -= 1
                return self._remove_node(node)
        return node

    def remove(self, value):
        self.root = self._remove(value, self.root)

    def __str__(self):
        return str(self.root).strip() if self.root != None else ""

    def __len__(self):
        return self.size

if __name__ == "__main__":

    print("\n\nTESTING ADD AND CONTAINS\n")

    bst_set = BSTSet()
    bst_set.add(4)
    bst_set.add(1)
    bst_set.add(7)
    bst_set.add(3)
    bst_set.add(5)
    print(bst_set)
    print("0: " + str(bst_set.contains(0)))
    print("1: " + str(bst_set.contains(1)))
    print("2: " + str(bst_set.contains(2)))
    print("3: " + str(bst_set.contains(3)))
    print("4: " + str(bst_set.contains(4)))
    print("5: " + str(bst_set.contains(5)))
    print("6: " + str(bst_set.contains(6)))
    print("7: " + str(bst_set.contains(7)))
    print("8: " + str(bst_set.contains(8)))
    bst_set.add(6)
    bst_set.add(2)
    print(bst_set)
    print("size of set: " + str(len(bst_set)))

    print("\n\nTESTING REMOVE\n")

    bst_set = BSTSet()
    bst_set = BSTSet()
    bst_set.add(5)
    bst_set.add(2)
    bst_set.add(4)
    bst_set.add(3)
    bst_set.add(1)
    bst_set.add(7)
    bst_set.add(6)
    bst_set.add(8)
    bst_set.add(10)
    bst_set.add(9)
    bst_set.add(11)
    bst_set.add(12)
    print(bst_set)
    print("size of set: " + str(len(bst_set)))
    bst_set.remove(11)
    print(bst_set)
    bst_set.remove(10)
    print(bst_set)
    bst_set.remove(8)
    print(bst_set)
    bst_set.remove(2)
    print(bst_set)
    bst_set.remove(7)
    print(bst_set)
    bst_set.remove(5)
    print(bst_set)
    bst_set.remove(9)
    print(bst_set)
    bst_set.remove(3)
    print(bst_set)
    print("size of set: " + str(len(bst_set)))
    bst_set.remove(1)
    print(bst_set)
    bst_set.remove(12)
    print(bst_set)
    bst_set.remove(4)
    print(bst_set)
    bst_set.remove(6)
    print(bst_set)
    print("size of set: " + str(len(bst_set)))