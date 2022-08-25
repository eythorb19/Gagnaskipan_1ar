class TreeNode:
    def __init__(self, name = ""):
        self.name = name
        # ADD STUFF HERE IF NEEDED
        
    # ADD STUFF HERE IF NEEDED

# ADD STUFF HERE IF NEEDED

# IF YOU WANT TO PUT THIS ALL INTO A CLASS AND USE INSTANCE VARIABLES (self.xx) THAT IS OK

def run_commands_on_node(node):
    print("  current directory: " + node.name)
    while True:
        user_input = input()
        command = user_input.split()
        if command[0] == "mkdir":
            print("  Making subdirectory " + command[1])
                # command[1] is the name of the subdirectory that should be made here

            # ADD STUFF HERE IF NEEDED

        elif command[0] == "ls":
            print("  Listing the contents of current directory,  " + node.name)

            # ADD STUFF HERE IF NEEDED

        elif command[0] == "cd":
            print("  switching to directory " + command[1])
                # command[1] is the name of the subdirectory that should now become the current directory
            if command[1] == "..":
                # "cd .." MEANS I WANT TO GO UP A FOLDER
                return # change if needed, but this should exit if you are in the root folder

            # ADD STUFF HERE IF NEEDED

            if True: # Change this to equivalent of "if folder not found":
                print("  No folder with that name exists")

        else:
            print("  command not recognized")

        # ADD STUFF HERE IF NEEDED



def run_directories_program():
    # YOU CAN CHANGE THE WHOLE THING IF YOU LIKE!!
    # YOU CAN DESIGN THIS DIFFERENTLY IF IT SUITS YOU
    run_commands_on_node(TreeNode("root"))

if __name__ == "__main__":
    run_directories_program()
    
