__author__ = 'jbowman'

# https://pythonspot.com/conditional-statements/

x = 3
y = 10
if x < y:
    print(str(x) + ' is smaller than ' + str(y))
else:
    print(str(x) + ' is bigger than ' + str(y))

# game
age = 27
N = 3
halfrange = 5

print('Guess my age, you get ' + str(N) + ' guess(es)!')
for ii in range(N):
    guess = int(input('Guess: '))
    if guess != age:
        print('Wrong!')
        if guess > age - halfrange and guess < age + halfrange:
            print('But, your guess is within +- ' + str(halfrange) + ' years of the correct age!')
        else:
            print('And your guess is at least +-' + str(halfrange) + ' years from the correct age.')
    else:
        print('Correct')
        break
