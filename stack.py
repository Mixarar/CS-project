# OOP
class Stack:
    def __init__(self, stack=None, maxlength=2) -> None:
        self.stack = stack if stack is not None else []
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

MyStack=Stack()
MyStack.push(10)
MyStack.push(20)
print(f"Top element is {MyStack.peek()}")
print(f"Is stack full? {MyStack.is_full()}")
print(f"Popped element is {MyStack.pop()}")
print(f"Is stack empty? {MyStack.is_empty()}")
print(f"Is stack full? {MyStack.is_full()}")


# Procedural
'''
global max_length
max_length = 2
stack = []

def push(stack, element):
    if len(stack) > max_length:
        print("Stack is full. Cannot push.")
    else:
        stack.append(element)
        print(f"Pushed {element} onto the stack.")

def pop(stack):
    if not stack:
        print("Stack is empty. Cannot pop.")
        return None
    return stack.pop()

def is_empty(stack):
    return len(stack) == 0

def is_full(stack):
    return len(stack) == max_length

def peek(stack):
    if not stack:
        print("Stack is empty.")
        return None
    return stack[-1]

push(stack, 10)
push(stack, 20)
print(f"Top element is {peek(stack)}")
print(f"Is stack full? {is_full(stack)}")
print(f"Popped element is {pop(stack)}")
print(f"Is stack empty? {is_empty(stack)}")
print(f"Is stack full? {is_full(stack)}")
'''