# Difference between singly and doubly linked list
# Singly linked list is simple for implementation, occupies less memory but can't traverse in reverse


class Node:
    def __init__(self, value):
        self.dataval = value
        self.nextval = None
        self.preval = None


class MyDoubleLinkedList:
    def __init__(self):
        self.headval = None
        self.tailval = None
        self.length = 0

    def append(self, value):
        newNode = Node(value)
        if self.headval is None:
            self.headval = newNode
            self.tailval = newNode
            self.length += 1
        else:
            currentNode = self.headval
            while(currentNode.nextval):
                currentNode = currentNode.nextval
            currentNode.nextval = newNode
            newNode.preval = currentNode
            self.tailval = newNode
            self.length += 1

    def prepend(self, value):
        if self.headval is None:
            self.headval = newNode
            self.tailval = newNode
            self.length += 1

        newNode = Node(value)
        newNode.nextval = self.headval
        self.headval.preval = newNode
        self.headval = newNode
        self.length += 1

    def printList(self):
        currentNode = self.headval
        print(currentNode.dataval)
        while(currentNode.nextval is not None):
            currentNode = currentNode.nextval
            print(currentNode.dataval)

    def printReverse(self):
        lastNode = self.tailval
        print(lastNode.dataval)
        while lastNode.preval is not None:
            lastNode = lastNode.preval
            print(lastNode.dataval)

    def travese(self, index):
        if index <= self.length/2:
            counter = 0
            currentNode = self.headval
            while counter != index:
                currentNode = currentNode.nextval
                counter += 1
            return currentNode
        else:
            counter = self.length - 1
            currentNode = self.tailval
            while counter != index:
                currentNode = currentNode.preval
                counter -= 1
            return currentNode

    def find(self, index):
        if index > self.length - 1:
            print("Invalid Index")
        node = self.travese(index)
        print(node.dataval)

    def insert(self, index, value):
        if index > self.length - 1:
            self.append(value)
            return True
        if index < 0:
            self.prepend(value)
            return True

        newNode = Node(value)
        preNode = self.travese(index-1)
        nextNode = preNode.nextval
        preNode.nextval = newNode
        newNode.preval = preNode
        newNode.nextval = nextNode
        nextNode.preval = newNode
        self.length += 1

    def removeAt(self, index):
        if index < 0 or index > self.length - 1:
            print("Invalid index")
            return True

        currentNode = self.travese(index)
        nextNode = currentNode.nextval
        preNode = currentNode.preval
        preNode.nextval = nextNode
        nextNode.preval = preNode
        self.length -= 1


myList = MyDoubleLinkedList()
myList.append('Mon')
myList.append('Tue')
myList.append('Wed')
myList.prepend('Sun')
#myList.find(2)
myList.insert(2, 'Fri')
myList.insert(10, 'Thu')
myList.removeAt(2)
#myList.printList()
print(myList.length)
myList.printReverse()
