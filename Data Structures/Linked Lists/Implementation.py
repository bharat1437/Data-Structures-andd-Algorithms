# Linked lists  are set of elements where one element is linked to next element. Last element is pointing to null.
# Linked lists has few advantanges and disadvantages when compared with arrays and hash tables.
# For array- continuous memory is allocated based on the size of array where as for linked list memory is allocated
# randomly and pointer is added to establish connection
# Complexity for linked lists:
# Append - O(1) - Directly inserts at head
# Prepend - O(1) - Directly inserts at tail
# Search - O(n) - Need to traverse through linked list until match is found
# Insert - O(n) - Need to traverse till the position where insert is required
# delete - O(n) - Need to traverse till the position where item should be deleted

# if we need to build a linked list with 10->5->16
# like
# dict = {
#     'head': {
#         'value': 10,
#         'next': {
#             'value': 5,
#             'next': {
#                 'value': 16,
#                 'next': None
#             }
#         }
#     }
# }


# New object of node is referenced to new node and link is created between them.

class Node:
    def __init__(self, dataval):
        self.dataval = dataval
        self.nextval = None


class MyLinkedList:
    def __init__(self):
        self.headval = None

    def printList(self):    # O(n) since it is iterating through all objects in list
        printVal = self.headval
        while printVal is not None:
            print(printVal.dataval)
            printVal = printVal.nextval

    def prepend(self, dataval):     # O(1) since it is just assigning next value of new node with head value
        newNode = Node(dataval)
        newNode.nextval = self.headval
        self.headval = newNode

    def append(self, dataval):  # O(n) since it is iterating till last node in linked list
        newNode = Node(dataval)
        if self.headval is None:
            self.headval = newNode
        else:
            last = self.headval.nextval
            while(last.nextval):
                last = last.nextval
            last.nextval = newNode

    def inBetween(self, middle_node, dataval):  # O(1) since it is just assigning new node value in between
        newNode = Node(dataval)
        if middle_node is None:
            print("Middle node not present")
        else:
            newNode.nextval = middle_node.nextval
            middle_node.nextval = newNode

    def insertUsingIndex(self, index, value):
        newNode = Node(value)
        leader = self.traverse(index-1)
        if leader is None:
            self.append(value)
        else:
            newNode.nextval = leader.nextval
            leader.nextval = newNode

    def traverse(self, index):
        counter = 0
        currentNode = self.headval
        while(counter != index and currentNode):
            currentNode = currentNode.nextval
            counter += 1
        return currentNode


    def remove(self, removeKey):  # O(n) since it is going to iterate through items for find exact key.
        notfound = True
        initialval = self.headval
        if initialval.dataval == removeKey:
            self.headval = initialval.nextval
            return
        while(initialval is not None):
            if initialval.dataval == removeKey:
                notfound = False
                break
            prev = initialval
            initialval = initialval.nextval

        if notfound == False:
            prev.nextval = initialval.nextval


    # reverse singly linked list. Must relook at logic. Very interesting

    def reverse(self):
        if self.headval.nextval is None:
            self.headval
        first = self.headval
        second = self.headval.nextval
        while second is not None:
            temp = second.nextval
            second.nextval = first
            first = second
            second = temp

        self.headval.nextval = None
        self.headval = first

newList = MyLinkedList()
node1 = Node('Mon')
node2 = Node('Tue')
node3 = Node('Wed')

newList.headval = node1
newList.headval.nextval = node2
node2.nextval = node3

newList.prepend('Sun')
newList.append('Thu')
newList.inBetween(newList.headval.nextval.nextval, 'Fri')
newList.insertUsingIndex(2, 'Wohooo')
newList.insertUsingIndex(50, 'Wohooo2')
newList.remove('Sat')
newList.printList()
print("############################")
newList.reverse()
newList.printList()

