# There are two type of arrays 1. Static 2. Dynamic array.
# Static array are one where size is fixed while initialization
# Dynamic arrays are one where arrays expand when new elements are added.
# Big O complexity for various operations on array are mentioned below.
# Arrays are fast at lookup, push and pop operations
# They are slow in insert at specific position and delete elements

class Array:

    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index): # O(1)
        if self.length == 0:
            return "No elements in array"
        else:
            return self.data[index]

    def push(self, item): # O(1)
        self.length += 1
        self.data[self.length - 1] = item

    def pop(self): # O(1)
        lastItem = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return lastItem

    def delete(self, index): # O(n)
        for i in range(index, self.length - 1):
            self.data[index] = self.data[index + 1]
        del self.data[self.length - 1]
        self.length -= 1


arr1 = Array()
arr1.push("Hi")
arr1.push("Bharat")
arr1.push("Chavan")
arr1.pop()
arr1.push("!!!!")
arr1.delete(1)
print(arr1.data)
print(arr1.length)



