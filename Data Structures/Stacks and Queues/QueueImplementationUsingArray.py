class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        first = self.data[0]
        del self.data[0]
        return first

    def peek(self):
        if len(self.data) > 0:
            return self.data[0]
        else:
            return None

    def empty(self):
        if len(self.data) == 0:
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
#print(myQueue.length)
print(myQueue.data)
#print(myStack.bottom.data)
print(myQueue.peek())