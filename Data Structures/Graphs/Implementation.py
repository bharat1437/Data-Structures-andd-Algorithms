# Exercise - build graph as shown on this site - https://visualgo.net/en/graphds?slide=1
# Implementation using adjacent list


class Graph:
    def __init__(self):
        self.nodes = 0
        self.adjecentList = {}

    def addVertex(self, node):
        if node in self.adjecentList.keys():
            print("Node already exists, please add connections")
        else:
            self.adjecentList[node] = []
            self.nodes += 1

    def addConnection(self, node1, node2):
        if node1 not in self.adjecentList.keys():
            self.addVertex(node1)
        if node2 not in self.adjecentList.keys():
            self.addVertex(node2)

        self.adjecentList[node1].append(node2)
        self.adjecentList[node2].append(node1)


myGraph = Graph()
print(myGraph.adjecentList)
myGraph.addVertex(0)
myGraph.addVertex(1)
myGraph.addVertex(2)
myGraph.addVertex(3)
myGraph.addVertex(4)
myGraph.addVertex(5)
myGraph.addVertex(6)
myGraph.addConnection(3, 1)
myGraph.addConnection(3, 4)
myGraph.addConnection(1, 0)
myGraph.addConnection(1, 2)
myGraph.addConnection(0, 2)
myGraph.addConnection(2, 4)
myGraph.addConnection(5, 4)
myGraph.addConnection(5, 6)
print(myGraph.adjecentList)
