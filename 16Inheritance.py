__author__ = 'jbowman'

# https://pythonspot.com/inheritance/

class User:
    name = ''

    def __init__(self, name):
        self.name = name

    def printName(self):
        print('Name: ' + self.name)

class Programmer(User):

    def __init__(self, name):
        super().__init__(name)

    def doPython(self):
        print('Programming Python')

brian = User('Brian')
brian.printName()

diana = Programmer("Diana")
diana.printName()
diana.doPython()