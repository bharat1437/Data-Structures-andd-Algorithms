# Stacks and queues are used for specific use cases  where an individual need to only access the last time/first
# item in the data structure. Like in browser when we click back then it will take us to last viewed  page
# or undo and redo in applications. Even javascript uses stacks to handle functions.

# Stacks can be implemented using both Arrays and LinkedlLists
# Queues can also be implemented using both Arrays and LinkedLists however if we want to remove first item in Array
# then we have to do unshift of indexes to maintain sequence which can be O(n) operation. Better to use linked list for
# queues.


class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def push(self, value):
        if value is None:
            print("Please pass valid value")
            return True
        newNode = Node(value)

        if self.top is None:
            self.bottom = newNode
            self.top = newNode
            self.length = 1
        else:
            holdingPointer  = self.top
            self.top = newNode
            self.top.next = holdingPointer
            self.length += 1

    def pop(self):
        if self.top is None:
            print("Nothing to pop!!!")
        else:
            if self.length == 1:
                self.bottom = None
            self.top = self.top.next
            self.length -= 1

    def peek(self):
        if self.top is not None:
            print("Top Node is :", str(self.top.data))

    def isEmpty(self):
        if self.length == 0:
            return True
        else:
            return False


myStack = Stack()
myStack.push("Mon")
myStack.push("Tue")
myStack.push("Wed")
myStack.push("Thu")
myStack.pop()
myStack.pop()
#myStack.pop()
#myStack.pop()
print(myStack.length)
#print(myStack.top.data)
#print(myStack.bottom.data)
myStack.peek()
print(myStack.isEmpty())