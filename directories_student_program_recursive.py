class TreeNode:
    def __init__(self, name = ""):
        self.name = name
        self.first_child = None
        self.next_sibling = None

def run_commands_on_node(node):
    print("  current directory: " + node.name)
    while True:
        user_input = input()
        command = user_input.split()
        if command[0] == "mkdir":
            print("  Making subdirectory " + command[1])
                # command[1] is the name of the subdirectory that should be made here
            new_node = TreeNode(command[1])
            new_node.next_sibling = node.first_child
            node.first_child = new_node
        elif command[0] == "ls":
            print("  Listing the contents of current directory,  " + node.name)
            tmp_node = node.first_child
            while tmp_node != None:
                print(tmp_node.name)
                tmp_node = tmp_node.next_sibling
        elif command[0] == "cd":
            print("  switching to directory " + command[1])
                # command[1] is the name of the subdirectory that should now become the current directory
            if command[1] == "..":
                return
            tmp_node = node.first_child
            while tmp_node != None:
                if tmp_node.name == command[1]:
                    run_commands_on_node(tmp_node)
                    break
                tmp_node = tmp_node.next_sibling
            if tmp_node == None:
                print("  No folder with that name exists")
        else:
            print("  command not recognized")



def run_directories_program():
    run_commands_on_node(TreeNode("root"))

if __name__ == "__main__":
    run_directories_program()
    
