
class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if len(self.data) == 0:
            return None
        else:
            del self.data[len(self.data) - 1]

    def peek(self):
        if len(self.data) > 0:
            return print(self.data[len(self.data) - 1])
        else:
            return None


myStack = Stack()
myStack.push("Mon")
myStack.push("Tue")
myStack.push("Wed")
myStack.push("Thu")
myStack.pop()
myStack.pop()
#myStack.pop()
#myStack.pop()
myStack.peek()
print(myStack.data)