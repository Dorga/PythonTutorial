__author__ = 'jbowman'

# https://pythonspot.com/loops/

items = ['Abby', 'Brenda', 'Cindy', 'Diddy']
for ii in items:
    print(ii)

for ii in range(1, 10):
    print(ii)

for ii in range(1,10):
    for jj in range(1,10):
        z = ii+jj
        print('(' + str(ii) + ',' + str(jj) + ') --> ' + str(z))

