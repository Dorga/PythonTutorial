__author__ = 'jbowman'

# https://pythonspot.com/datatype-casting/
# Function	Description
# int(x)	Converts x to an integer
# long(x)	Converts x to a long integer
# float(x)	Converts x to a floating point number
# str(x)	Converts x to an string.  x can be of the type float. integer or long.
# hex(x)	Converts x integer to a hexadecimal string
# chr(x)	Converts x integer to a character
# ord(x)	Converts character x to an integer

x = 3
y = 2.15315315313532

print('We have defined two numbers,')
print('x = ' + str(x))
print('y = ' + str(y))

a = '135.31421'
b = '133.1112223'

c = float(a) + float(b)
print(c)
print('a + b = ' + str(c))