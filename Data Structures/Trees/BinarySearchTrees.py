class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)
        if self.root is None:
            self.root = newNode
        else:
            topNode = self.root
            while True:
                rightNode = topNode.right
                leftNode = topNode.left
                if value < topNode.value:
                    if leftNode is not None:
                        topNode = leftNode
                    elif leftNode is None:
                        topNode.left = newNode
                        break
                if value > topNode.value:
                    if rightNode is not None:
                        topNode = rightNode
                    elif rightNode is None:
                        topNode.right = newNode
                        break
                if value == topNode.value:
                    return None

    def lookup(self, value):
        currentNode = self.root
        if currentNode is not None:
            while currentNode is not None:
                if value < currentNode.value:
                    currentNode = currentNode.left
                elif value > currentNode.value:
                    currentNode = currentNode.right
                elif value == currentNode.value:
                    return currentNode

            return False
        else:
            return False


binTree = BinarySearchTree()
binTree.insert(9)
binTree.insert(4)
binTree.insert(6)
binTree.insert(20)
binTree.insert(170)
binTree.insert(15)
binTree.insert(1)
print(binTree.root.value)
print(binTree.root.left.value)
print(binTree.root.right.value)
print(binTree.root.left.left.value)
print(binTree.root.left.right.value)
print(binTree.root.right.left.value)
print(binTree.root.right.right.value)
findNode = binTree.lookup(170)
if findNode:
    print("Found Node", findNode.value)

