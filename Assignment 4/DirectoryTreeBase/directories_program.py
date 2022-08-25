class TreeNode:
    '''Node with name, list of child directories and link to parent directory'''
    def __init__(self, name = "", parent = None, children = None):
        self.name = name
        self.children = []
        self.parent = parent

    def __str__(self):
        '''Returns name of directory'''
        return self.name 

    def make_subdirectory(self, new_directory):
        '''Adds a subdirectory to the TreeNode.'''
        subdirectory = TreeNode(new_directory, self)
        self.children.append(subdirectory)

    def find_child_index(self, child_name):
        '''Returns index of child with specified child_name'''
        index = 0
        for child in self.children:
            if child.name == child_name:
                return index
            index+=1
        return None

    def check_child_names(self, directory_name):
        '''Returns True if directory has child with specified directory_name. Otherwise returns False.'''
        for child in self.children:
            if child.name == directory_name:
                return True
        return False

    def remove_child(self, directory_name):
        '''Removes subdirectory.'''
        index = self.find_child_index(directory_name)
        del self.children[index]

    def print_alphabetically(self):
        """Prints subdirectorys of current directory, in alphabetic order."""
        children_names = []
        children_alphabetic_names = []

        if len(self.children) > 0:
            #Create list of names of children
            for i in range(len(self.children)):
                children_names.append(self.children[i].name)

            #Insert first name to list
            children_alphabetic_names.append(children_names[0])
            for j in range(1, len(children_names)):
                child_to_insert = children_names[j]

                #If first in alphabet append
                if child_to_insert < children_alphabetic_names[0]:
                    children_alphabetic_names.insert(0,child_to_insert)

                #Insert inside or back of list
                else:
                    for k in range(len(children_alphabetic_names),0,-1):
                        child_to_compare = children_alphabetic_names[k-1]
                        
                        if child_to_insert > child_to_compare:
                            children_alphabetic_names.insert(k,child_to_insert)
                            break

            #Print names in alphabetic order
            for k in range(len(children_alphabetic_names)):
                print(children_alphabetic_names[k])


#Program functions 
def mkdir(current_directory, new_subdirectory):
    '''Creates a new subdirectory in current directory, if no subdirectory with same name exists.'''

    print("  Making subdirectory " + new_subdirectory)
    directory_exists = current_directory.check_child_names(new_subdirectory)

    if directory_exists == False:
        current_directory.make_subdirectory(new_subdirectory)
    else:
        print("  Subdirectory with same name already in directory")


def cd(current_directory, new_current_directory):
    '''Changes directory to parent or child, if directory exists.'''

    print("  switching to directory " + new_current_directory)

    #Change directory to parent
    if new_current_directory == "..":
        current_directory = current_directory.parent

    #Change directory to child
    else:
        child_index = current_directory.find_child_index(new_current_directory)
        if child_index == None:
            print("  No folder with that name exists")
        else:
            current_directory = current_directory.children[child_index]
    
    return current_directory


def rm(current_directory, child_to_remove):
    '''Removes subdirectory if directory exists'''

    print("  removing directory " + child_to_remove)
    directory_exists = current_directory.check_child_names(child_to_remove)

    if directory_exists == True:
        current_directory.remove_child(child_to_remove)
        print("  directory successfully removed!")
    else:
        print("  No folder with that name exists")

#Main program
def run_commands_on_tree(tree):
    print("  current directory: " + tree.name)
    current_directory = tree
    
    while True:
        user_input = input()
        command = user_input.split()
        action = command[0]
        if action != "ls":
            directory_name = command[1]

        #Make subdirectory
        if action == "mkdir":
            mkdir(current_directory, directory_name)

        #List contents of current directory
        elif action == "ls":
            print("  Listing the contents of current directory, " + str(current_directory))
            current_directory.print_alphabetically()

        #Change directory
        elif action == "cd":
            if directory_name == ".." and current_directory.parent == None:    #Exit program if user changes directory up from root
                print("Exiting directory program")
                quit()

            else:
                new_current_directory = cd(current_directory, directory_name)
                run_commands_on_tree(new_current_directory)

        #Remove directory
        elif action == "rm":
            rm(current_directory, directory_name)
            
        #Command unknown
        else:
            print("  command not recognized")

def run_directories_program():

    current_node = TreeNode("root")
    run_commands_on_tree(current_node)

if __name__ == "__main__":
    run_directories_program()
    
