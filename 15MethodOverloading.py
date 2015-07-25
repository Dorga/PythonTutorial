__author__ = 'jbowman'

# https://pythonspot.com/method-overloading/

class Human:

    name = ''

    def __init__(self, name=None):
        self.name = name

    def sayHello(self):

        if self.name is not None:
            print('Hello ' + self.name)
        else:
            print('Hello')

obj = Human()
obj.sayHello()
obj2 = Human('Jerry')
obj2.sayHello()
