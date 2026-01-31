# Stack Implementation

# OOP Implementation
class Stack:
    def __init__(self, maxlength=5) -> None:
        self.stack = []
        self.maxlength = maxlength

    def push(self, element):
        if len(self.stack) >= self.maxlength:
            print("Stack is full. Cannot push.")
        else:
            self.stack.append(element)
            print(f"Pushed {element} onto the stack.")

    def pop(self):
        if not self.stack:
            print("Stack is empty. Cannot pop.")
            return None
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.maxlength

    def peek(self):
        if not self.stack:
            print("Stack is empty.")
            return None
        return self.stack[-1]

# Procedural Implementation
def push_procedural(stack, element, max_length):
    if len(stack) >= max_length:
        print("Stack is full. Cannot push.")
    else:
        stack.append(element)
        print(f"Pushed {element} onto the stack.")

def pop_procedural(stack):
    if not stack:
        print("Stack is empty. Cannot pop.")
        return None
    return stack.pop()

def run_stack_demo():
    print("--- Stack (OOP) ---")
    MyStack = Stack(maxlength=2)
    MyStack.push(10)
    MyStack.push(20)
    MyStack.push(30) # Should be full
    print(f"Top element is {MyStack.peek()}")
    print(f"Is stack full? {MyStack.is_full()}")
    print(f"Popped element: {MyStack.pop()}")
    print(f"Is stack empty? {MyStack.is_empty()}")

    print("\n--- Stack (Procedural) ---")
    stack_list = []
    max_len = 3
    push_procedural(stack_list, "A", max_len)
    push_procedural(stack_list, "B", max_len)
    print(f"Popped from procedural stack: {pop_procedural(stack_list)}")

if __name__ == "__main__":
    run_stack_demo()
