class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

def print_to_screen(head):
    if head != None:
        print(head.data, end=" ")
        print_to_screen(head.next)
    else:
        print("")

def palindrome(head):
    if head.next == None:
        return True
    if find_end(head) == head.data:
        head = cut_from_back(head)
        next_val = head.next
        return palindrome(next_val)
    else:
        return False

def cut_from_back(head,new_head):
    if head.next.next == None:
        return new_head
    else:
        new_tail = Node(head.data,None)
        if new_tail.next == None:
            new_head = new_tail
        else:
            new_head.next = new_tail

        return cut_from_back(head.next,new_head)

def find_end(head):
    if head.next == None:
        end = head.data
        return end
    else:
        return find_end(head.next)

if __name__ == "__main__":

    print("\n")
    head = Node("A", Node("E", Node("L", Node("E", Node("A", None)))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("A", Node("E", Node("L", Node("B", Node("A", None)))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("C", Node("A", Node("L", Node("L", Node("A", Node("C", None))))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("C", Node("A", Node("L", Node("T", Node("E", Node("C", None))))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")