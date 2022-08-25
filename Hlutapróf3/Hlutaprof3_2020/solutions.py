# Implement helper classes here

def split(my_string): 
    return list(my_string) 

class LRCNode:
    """Node with data and left,right,center children"""

    def __init__(self, data = None):
        self.data = data
        self.l_child = None
        self.c_child = None
        self.r_child = None

    def add_children(self, node, current_depth = 0, depth = 0):
        """Adds children recursively until defined depth is reached"""
        if current_depth == depth:
            return

        else:
            current_depth+= 1

            node.l_child = LRCNode()
            node.c_child = LRCNode()
            node.r_child = LRCNode()

            node.l_child.add_children(node.l_child, current_depth, depth)
            node.c_child.add_children(node.c_child, current_depth, depth)
            node.r_child.add_children(node.c_child, current_depth, depth)
        

class LRCMap:
    """Map of LRC nodes"""

    def __init__(self, build = False):
        self.root = LRCNode()

        if build == True:
            self.root = LRCNode()
            self.root.add_children(self.root, 0,7)
        else: 
            self.root = LRCNode()

    def put_data(self, key, data):
        """Puts data into map according to string key l,r,c"""
        current_node = self.root
        keys = split(key)

        for i in range(0,len(keys)):
            if keys[i] == "l":

                if current_node.l_child == None:
                    current_node.l_child = LRCNode()

                current_node = current_node.l_child

            elif keys[i] == "r":
                if current_node.r_child == None:
                    current_node.r_child = LRCNode()

                current_node = current_node.r_child
            
            elif keys[i] == "c":
                if current_node.c_child == None:
                    current_node.c_child = LRCNode()

                current_node = current_node.c_child

        current_node.data = data

    def get_data(self, key): # returns data for that key or None if non-existant
        """Gets data according to string key lrc"""
        
        current_node = self.root
        keys = split(key)

        for i in range(0,len(keys)):
            if keys[i] == "l":
                # current_node.l_child = LRCNode()
                current_node = current_node.l_child

                if current_node == None:
                    return None

            elif keys[i] == "r":
                # current_node.r_child = LRCNode()
                current_node = current_node.r_child

                if current_node == None:
                    return None
            
            elif keys[i] == "c":
                # current_node.c_child = LRCNode()
                current_node = current_node.c_child

                if current_node == None:
                    return None
            
        # print(str(current_node.data))
        return current_node.data


class HashMap:
    """Hashed map with keys and data"""
    def __init__(self):
        self.array_length = 16
        # MUST USE ONE OF THE FOLLOWING LINES, BUT NOT BOTH
        self.hash_table = [ [ ] for _ in range(self.array_length) ]
        # self.hash_table = [ { } for _ in range(self.array_length) ]
        self.item_count = 0

    def __setitem__(self, key, data): # overrides/updates if already there
        """Sets data at key"""
        index = hash(key) %  self.array_length
        # self.hash_table[index] = [key,data]

        key_list = self.hash_table[index]
        for i in range(len(key_list)):
            if key_list[i][0] == key:
                key_list[i][1] = data
            return
        self.hash_table[index].append([key,data])
        self.item_count+=1

    def __getitem__(self, key): # returns data - returns None if nothing there
        """Gets data at key"""
        index = hash(key) %  self.array_length
        if self.hash_table[index] == []:
            return None

        else:
            key_list = self.hash_table[index]
            for i in range(len(key_list)):
                if key_list[i][0] == key:
                    return key_list[i][1]
        return None

    def __len__(self):
        return self.item_count


# NO IMPLEMENTATION OF EXAM SOLUTIONS BELOW THIS LINE
if __name__ == "__main__":

    # MAKE ALL TEST CODE BELOW THIS LINE
    # AND AT THIS INDENT LEVEL!!

    tm = LRCMap()
    tm.put_data("lrl", "THIS IS THE DATA FOR KEY lrl")
    tm.put_data("lc", "THIS IS THE DATA FOR KEY lc")
    print(tm.get_data("lrl"))
    print(tm.get_data("lrcclc"))
    print(tm.get_data("lc"))

    tm = LRCMap(True)
    tm.put_data("lrlrccr", "THIS IS THE DATA FOR KEY lrlrccr")
    tm.put_data("lrlrcclc", "THIS IS THE DATA FOR KEY lrlrcclc")
    print(tm.get_data("lrlrcclc"))
    print(tm.get_data("lrlclc"))
    print(tm.get_data("lrlrccr"))


    hm = HashMap()
    hm["key_value:345"] = "THIS IS THE DATA FOR KEY: key_value:345"
    hm[345] = "THIS IS THE DATA FOR KEY: 345"
    print(hm[345])
    print(hm[346])
    print(hm["key_value:345"])
    print(len(hm))
    hm[345] = "THIS IS THE NEW DATA FOR KEY: 345"
    print(hm[345])
    print(len(hm))
