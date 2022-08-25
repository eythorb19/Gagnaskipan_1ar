
# THIS SOLUTION IS NOT FULLY COMPATIBLE WITH THE DESCRIPTION YET.
# I WILL MAKE IT FULLY OPERATION BEFORE I POST SOLUTIONS FOR STUDENTS
# THIS ONE IS STILL AN INDICATOR ON A DIFFERENT METHOD OF TREE SOLUTION
# WITH JUST NODES, NOT A CLASS
# THE CLASS VERSION IS A FULLY WORKING SOLUTION

class TreeNode:
    def __init__(self, name = ""):
        self.name = name
        self.first_child = None
        self.next_sibling = None


def has_sibling(node, name):
    if node == None:
        return False
    if node.name == name:
        return True
    return has_sibling(node.next_sibling, name)

def get_sibling(node, name):
    if node == None or node.name == name: #found or not found
        return node
    return get_sibling(node.next_sibling, name)

def add_sibling(node, name):
    if node == None:
        return TreeNode(name)
    if name < node.name:
        new_node = TreeNode(name)
        new_node.next_sibling = node
        return new_node
    node.next_sibling = add_sibling(node.next_sibling, name)
    return node

def remove_sibling(node, name):
    if node == None:
        return None
    if node.name == name:
        return node.next_sibling
    node.next_sibling = remove_sibling(node.next_sibling, name)
    return node


def run_commands_on_node(node):
    print("  current directory: " + node.name)
    while True:
        user_input = input()
        command = user_input.split()
        if command[0] == "mkdir":
            print("  Making subdirectory " + command[1])
                # command[1] is the name of the subdirectory that should be made here
            if has_sibling(node.first_child, command[1]):
                print("  Subdirectory with same name already in directory")
            else:
                node.first_child = add_sibling(node.first_child, command[1])
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
            tmp_node = get_sibling(node.first_child, command[1])
            if tmp_node == None:
                print("  No folder with that name exists")
            else:
                run_commands_on_node(tmp_node)
            print("  current directory: " + node.name)

        elif command[0] == "rm":
            print("  removing directory " + command[1])
            if has_sibling(node.first_child, command[1]):
                node.first_child = remove_sibling(node.first_child, command[1])
                print("  directory successfully removed!")
            else:
                print("  No folder with that name exists")
        else:
            print("  command not recognized")



def run_directories_program():
    run_commands_on_node(TreeNode("root"))
    print("Exiting directory program")

if __name__ == "__main__":
    run_directories_program()
    
