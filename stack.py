__author__ = 'logan'

class Stack:
    data = []
    def push(self, name):
        self.data.append(name)
    def pop(self):
        self.data.pop()

pass