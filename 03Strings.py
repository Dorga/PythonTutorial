__author__ = 'jbowman'

s = 'Hello Python'
print(s)
print(s[0])
print(s[0:2])
print(s[2:4])
print(s[6:])
print(s + ' ' + s)
print(s.replace('Hello', 'Thanks'))

s2 = '123456'
print(s2)
print(s2[0:2])

# String compare
sentence = 'The cat is brown'
q = 'cat'

if q == sentence:
    print('equal')
else:
    print('not equal')

# String contains
if q in sentence:
    print(q + ' found in ' + sentence)
