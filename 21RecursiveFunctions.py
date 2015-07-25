__author__ = 'jbowman'

# https://pythonspot.com/recursion/

# adding numbers in a list without recursion
def sum(list):
    total = 0

    for ii in range(0, len(list)):
        total = total + list[ii]

    return total

total = sum([1,2,3,4,5,6])
print(total)

# adding numbers in a list using recursion
def recursivesum(list):
    if len(list) == 1:
        return list[0]
    else:
        total = list[0] + sum(list[1:])
        return total

total = recursivesum([1,2,3,4,5,6])
print(total)

# factorial using recursion
import sys

sys.setrecursionlimit(5000)

def recursivefactorial(n):
    if n == 1:
        return n
    else:
        return n * recursivefactorial(n-1)

print(recursivefactorial(4))