# A simple stack implementation using a list
class Stack:
    def __init__(self):
        self.stack = []

    # Push: Add an item to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # Pop: Remove the item from the top of the stack
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()  # Remove and return the last item
        else:
            return "Stack is empty"

    # Peek/Top: See the top item of the stack
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]  # Return the last item without removing it
        else:
            return "Stack is empty"

    # isEmpty: Check if the stack is empty
    def isEmpty(self):
        return len(self.stack) == 0


stack = Stack()  # Create a new stack
stack.push("A")  # Push A onto the stack
stack.push("B")  # Push B onto the stack
stack.push("C")  # Push C onto the stack

print(stack.pop())  
print(stack.peek())  
print(stack.isEmpty()) 