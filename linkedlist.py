# OOP
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.display()
'''

# Procedural

def create_node(data):
    return {"data": data, "next": None}

def append(head, data):
    new_node = create_node(data)
    if not head:
        return new_node
    current = head
    while current["next"]:
        current = current["next"]
    current["next"] = new_node
    return head

def display(head):
    current = head
    while current:
        print(current["data"], end=" -> ")
        current = current["next"]
    print("None")


head = None
head = append(head, 1)
head = append(head, 2)
display(head)
