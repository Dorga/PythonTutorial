__author__ = 'jbowman'

# https://pythonspot.com/random-numbers/

from random import *

print(random())
print(randint(1, 100))
print(uniform(1, 10))
print(10*random())

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

x = sample(items, 1) # pick a random item from the list
print(x[0])

y = sample(items, 4) # pick 4 random items from the list
print(y)

