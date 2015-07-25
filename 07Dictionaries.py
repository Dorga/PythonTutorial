__author__ = 'jbowman'

# Dictionaries

words = {}
words['Hello'] = 'Bonjour'
words['Yes'] = 'Oui'
words['No'] = 'Non'
words['Bye'] = 'Au Revoir'

print(words)
print(words['Hello'])
print(words['No'])

dict = {}
dict['Ford'] = 'Car'
dict['Number'] = 23425
dict[2] = 'This sentence is stored here'

print(dict)
print('Number')
print(2)

# manipulating dictionaries
print(words)
del words['Yes']
print(words)
words['Yes'] = 'Oui!'
print(words)