class ChildNotFound(Exception):
    pass

class TreeNode:
    def __init__(self, name = "", parent = None):
        self.name = name
        self.parent = parent
        self.children = []

    def add_child(self, name):
        self.children.insert(0, TreeNode(name, self))

    def __str__(self):
        return self.name

    def print_children(self):
        for node in self.children:
            print(node)

    def get_child(self, name):
        for node in self.children:
            if node.name == name:
                return node
        raise ChildNotFound()


class TreeExit(Exception):
    pass

class DirectoryTree:
    def __init__(self):
        self.root = TreeNode("root")
        self.current_node = self.root

    def make_directory(self, name):
        self.current_node.add_child(name)
    
    def get_directory_name(self):
        return self.current_node.name

    def print_directory_contents(self):
        self.current_node.print_children()

    def go_to_directory(self, name):
        self.current_node = self.current_node.get_child(name)

    def go_to_parent_directory(self):
        self.current_node = self.current_node.parent
        if self.current_node == None:
            raise TreeExit()


def run_commands_on_tree(tree):
    print("  current directory: " + str(tree.root))
    while True:
        user_input = input()
        command = user_input.split()
        if command[0] == "mkdir":
            print("  Making subdirectory " + command[1])
                # command[1] is the name of the subdirectory that should be made here

            tree.make_directory(command[1])

        elif command[0] == "ls":
            print("  Listing the contents of current directory,  " + tree.get_directory_name())

            tree.print_directory_contents()

        elif command[0] == "cd":
            print("  switching to directory " + command[1])
                # command[1] is the name of the subdirectory that should now become the current directory
            if command[1] == "..":
                try:
                    tree.go_to_parent_directory()
                except(TreeExit):
                    return
            else:
                try:
                    tree.go_to_directory(command[1])
                    print("  current directory: " + tree.get_directory_name())
                except(ChildNotFound):
                    print("  No folder with that name exists")
        else:
            print("  command not recognized")



def run_directories_program():
    run_commands_on_tree(DirectoryTree())

if __name__ == "__main__":
    run_directories_program()
    
