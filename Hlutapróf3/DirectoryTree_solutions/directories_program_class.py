class ChildNotFound(Exception):
    pass

class ChildExists(Exception):
    pass

class TreeNode:
    def __init__(self, name = "", parent = None):
        self.name = name
        self.parent = parent
        self.children = []

    def add_child(self, name):
        if name in self.children:
            raise ChildExists()
        else:
            self.children.insert(0, TreeNode(name, self))
            self.children.sort()


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

    def remove_child(self, name):
        for node in self.children:
            if node.name == name:
                self.children.remove(node)
                return
        raise ChildNotFound()

    def __lt__(self, other):
        return self.name < other.name

    def __eq__(self, other):
        return str(self) == str(other)



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

    def remove_directory(self, name):
        self.current_node.remove_child(name)



def run_commands_on_tree(tree):
    print("  current directory: " + str(tree.root))
    while True:
        user_input = input()
        command = user_input.split()
        if command[0] == "mkdir":
            print("  Making subdirectory " + command[1])
                # command[1] is the name of the subdirectory that should be made here
            try:
                tree.make_directory(command[1])
            except(ChildExists):
                print("  Subdirectory with same name already in directory")

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
                    print("Exiting directory program")
                    return
            else:
                try:
                    tree.go_to_directory(command[1])
                except(ChildNotFound):
                    print("  No folder with that name exists")
            print("  current directory: " + tree.get_directory_name())

        elif command[0] == "rm":
            print("  removing directory " + command[1])
            try:
                tree.remove_directory(command[1])
                print("  directory successfully removed!")
            except(ChildNotFound):
                print("  No folder with that name exists")
        else:
            print("  command not recognized")



def run_directories_program():
    run_commands_on_tree(DirectoryTree())

if __name__ == "__main__":
    run_directories_program()
    
