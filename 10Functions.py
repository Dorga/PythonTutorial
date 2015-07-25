__author__ = 'jbowman'


# https://pythonspot.com/functions/

def f(x):
    return x * x


print(f(3))


def f(x, y):
    print('You called f(x,y) with the value x = ' + str(x) + ' and y = ' + str(y))
    print('x * y = ' + str(x * y))


f(3, 2)


def sum(x, y, z):
    return x + y + z


sum = sum(1, 2, 3)
print(str(sum))


# argument labels with defaults
def kwargs(a=0, b=0):
    return a - b


print(str(kwargs()))
print(str(kwargs(a=1)))
print(str(kwargs(b=1)))
print(str(kwargs(a=3, b=1)))
print(str(kwargs(b=3, a=1)))


def kwargs2(a=None, b=None):
    return a - b

print(str(kwargs()))
print(str(kwargs(a=1)))
print(str(kwargs(b=1)))
print(str(kwargs(a=3, b=1)))
print(str(kwargs(b=3, a=1)))