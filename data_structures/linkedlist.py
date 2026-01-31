# Linked List Implementation

# OOP Implementation
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
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")

# Procedural Implementation


def create_node(data):
    return {"data": data, "next": None}


def append_procedural(head, data):
    new_node = create_node(data)
    if not head:
        return new_node
    current = head
    while current["next"]:
        current = current["next"]
    current["next"] = new_node
    return head


def display_procedural(head):
    current = head
    elements = []
    while current:
        elements.append(str(current["data"]))
        current = current["next"]
    print(" -> ".join(elements) + " -> None")


def run_linkedlist_demo():
    print("--- Linked List (OOP) ---")
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.display()

    print("\n--- Linked List (Procedural) ---")
    head = None
    head = append_procedural(head, 10)
    head = append_procedural(head, 20)
    head = append_procedural(head, 30)
    display_procedural(head)


if __name__ == "__main__":
    run_linkedlist_demo()
