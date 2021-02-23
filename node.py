
class Node:
    def __init__(self, ID, type):
        self.ID = ID
        self.type = type
        self.children = []

    def addChild(self, ID, distance):
        c = Child(ID, distance)
        self.children.append(c)

    def printChildren(self, attr):
        for i in self.children:
            output = getattr(i, attr)
            print(output)



class Child:
    def __init__(self, ID, distance):
        self.ID = ID
        self.distance = distance



def addNode(arr, node):
    arr.append(node)
    return arr

nodes = []
p1 = Node('A', 'wp')
p2 = Node('B', 'ws')


nodes = addNode(nodes, p1)
nodes = addNode(nodes, p2)
print(nodes)
p1.addChild('B', 4)
p1.printChildren('ID')
