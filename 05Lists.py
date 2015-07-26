__author__ = 'jbowman'

# Lists
l = ['Drake', 'Derp', 'Derek', 'Dominique']
p = []

print(l)
print(l[0])
print(l[1])
print(l[2])

# add and remove
print("-------")
l.append('Victoria')
print(l)
l.remove('Derp')
l.remove('Drake')
print(l)
p = l.append('Drake')
l.append('Drake')
print(l)
print(p)

# sort
l.append('Drake')
print(l)
l.sort()
print(l)
l.reverse()
print(l)
