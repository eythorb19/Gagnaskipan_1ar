
class HeapNode:
    def __init__(self, priority, data = None, parent = None, left = None, right = None):
        self.priority = priority
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right

class PriorityQueue:
    def __init__(self):
        self.root = None
        self.last_node = None

    def add(self, priority, value):
        if self.root == None:
            self.last_node = self.root = HeapNode(priority, value)
        elif self.last_node.parent != None and self.last_node is self.last_node.parent.left:
            # The last node is a left node,so we now add its right sibling and make that the last node
            self.last_node.parent.right = HeapNode(priority, value, self.last_node.parent)
            self.last_node = self.last_node.parent.right
        else:
            next_to_add = self.last_node
            # Go all the way up right side of subtree
            while next_to_add is not self.root and next_to_add is next_to_add.parent.right:
                next_to_add = next_to_add.parent
            # If we're not at the root, go one up and one down to the right
            if next_to_add is not self.root:
                next_to_add = next_to_add.parent.right
            # Go all the way down the left side of subtree
            while next_to_add.left != None:
                next_to_add = next_to_add.left
            # Add new node to the left of the bottom left of the subtree
            next_to_add.left = HeapNode(priority, value, next_to_add)
            self.last_node = next_to_add.left
        # Bubble up
        node = self.last_node
        while node.parent != None and node.priority < node.parent.priority:
            self.swap_values(node, node.parent)
            node = node.parent

    def remove(self):
        if self.last_node == None:
            return None
        ret_val = self.root.data
        if self.last_node is self.root:
            self.last_node = self.root = None
            return ret_val
        self.swap_values(self.last_node, self.root)
        if self.last_node is self.last_node.parent.right:
            self.last_node = self.last_node.parent.left
            self.last_node.parent.right = None
        else:
            self.last_node = self.last_node.parent
            self.last_node.left = None
            # Go all the way up left side of subtree
            while self.last_node is not self.root and self.last_node is self.last_node.parent.left:
                self.last_node = self.last_node.parent
            # If we're not at the root, go one up and one down to the left
            if self.last_node is not self.root:
                self.last_node = self.last_node.parent.left
            # Go all the way down the right side of subtree
            while self.last_node.right != None:
                self.last_node = self.last_node.right
        # Bubble down
        node = self.root
        # if there isn't a left child, there's not a right child either, as tree is always full
        while node.left != None:
            # if there's a right child and it's lower than this one
            if node.right != None and node.right.priority < node.priority:
                # check if the left one is even lower
                if node.left.priority < node.right.priority:
                    # swap with left and move down to the left
                    self.swap_values(node, node.left)
                    node = node.left
                else:
                    # swap with right and move down to the right
                    self.swap_values(node, node.right)
                    node = node.right
            # There's no right child, but the left child may be lower
            elif node.left.priority < node.priority:
                # swap with left and move down to the left
                self.swap_values(node, node.left)
                node = node.left
            else:
                # if its lower than both children, it has found its place
                break
        return ret_val

    def is_empty(self):
        return self.root == None

    def swap_values(self, node1, node2):
        tmp_pri = node1.priority
        tmp_val = node1.data
        node1.priority = node2.priority
        node1.data = node2.data
        node2.priority = tmp_pri
        node2.data = tmp_val

    def _str_recur(self, node, level):
        if node == None:
            return ""
        return str(node.data) + " (" + str(level) + ") " + self._str_recur(node.left, level + 1) + self._str_recur(node.right, level + 1)

    def __str__(self):
        return self._str_recur(self.root, 0)

if __name__ == "__main__":
    pq = PriorityQueue()
    print("Enter priority of node:", end = " ")
    choice = input()
    while choice != "":
        pq.add(int(choice), choice)
        print("Enter priority of node:", end = " ")
        choice = input()
    print(str(pq).strip())
    while not pq.is_empty():
        print(str(pq.remove()))
        print(str(pq).strip())