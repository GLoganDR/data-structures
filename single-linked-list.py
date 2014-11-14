class Node:
    #constructor function is called __init__
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList():
    head = None
    def last(self, node = None):
        if(not node):
            node = self.head
        if(not node.next):
            return node
        else:
            return self.last(node.next)
    def insert(self, obj):
        if(not self.head):
            self.head = Node(obj)
        else:
            self.last().next = Node(obj)

people = SingleLinkedList()
people.insert("bob")
people.insert("sara")
people.insert("jill")

pass