from stack import *
from que import *
from recursive import *

food = Stack()
food.push('hamburger')
food.push('fries')
food.push('cake')
food.pop()

print("1st off the Stack: {0}".format(food.pop()))

people = Queue()
people.enqueue('Bob')
people.enqueue('Sara')
people.enqueue('Jill')

print("1st off the Queue: {0}".format(people.dequeue()))
print("2nd off the Queue: {0}".format(people.dequeue()))

print(fact(5))
for x in range(20):
    print('fib({0}) = {1}'.format(x, fib(x)))