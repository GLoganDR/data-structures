__author__ = 'loganrichardson'

class Node:
    # Tree node: left and right child + data which can be any object

    def __init__(self, data):
        #Node constructor
        self.prev = None
        self.next = None
        self.data = data

class BinTree:
    root = None

    def insert(self, name):
        if not self.root:
            self.root = Node(name)
        else:
            node = self.find(name)
            if name < node.data:
                node.prev = Node(name)
            else:
                node.next = Node(name)

    def find(self, name, node = None):
        if not node:
            node = self.root
        if name < node.data and node.prev:
            return self.find(name, node.prev)
        elif name > node.data and node.next:
            return self.find(name, node.next)
        else:
            return node

    def visit_node(self, node, list):
        if node.prev:
            self.visit_node(node.prev, list)
        list.append(node.data)
        if node.next:
            self.visit_node(node.next, list)

    def to_list(self):
        list = []
        if self.root:
            self.visit_node(self.root, list)
        return list

t = BinTree()

t.insert('a')
t.insert('b')
t.insert('c')
t.insert('d')
t.insert('e')
t.insert('z')
t.insert('y')
t.insert('x')
t.insert('w')
t.insert('v')
t.insert('n')
t.insert('i')
t.insert('f')
t.insert('p')

list = t.to_list()

print("the list of letters in alphabetical order is {0}".format(list))

pass
