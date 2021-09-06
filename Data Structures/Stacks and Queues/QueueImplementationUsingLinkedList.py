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


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def enqueue(self, value):
        if value is None:
            print("Please pass valid value")
            return True
        newNode = Node(value)

        if self.first is None:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        self.length += 1

    def dequeue(self):
        if self.first is None:
            print("Nothing to pop!!!")
        else:
            if self.length == 1:
                self.last = None
            self.first = self.first.next
            self.length -= 1

    def peek(self):
        if self.first is not None:
            print("First Node is :", str(self.first.data))

    def isEmpty(self):
        if self.length == 0:
            return True
        else:
            return False


myQueue = Queue()
myQueue.enqueue("Mon")
myQueue.enqueue("Tue")
myQueue.enqueue("Wed")
myQueue.enqueue("Thu")
myQueue.dequeue()
myQueue.dequeue()
#myQueue.dequeue()
#myQueue.dequeue()
print(myQueue.length)
#print(myStack.top.data)
#print(myStack.bottom.data)
myQueue.peek()
print(myQueue.isEmpty())