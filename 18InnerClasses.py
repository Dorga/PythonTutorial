__author__ = 'jbowman'

# https://pythonspot.com/inner-classes/

class Human:

    def __init__(self, name):
        self.name = name
        self.head = self.Head()

    def addhead(self):
        self.head2 = self.Head()

    class Head:
        def __init__(self):
            self.brain = self.Brain()

        def talk(self):
            return 'talking...'

        class Brain:
            def think(self):
                return 'thinking...'

if __name__ == '__main__': # execute only if run as a script directly
    joey = Human('Joey')
    print(joey.name)
    print(joey.head.talk())
    print(joey.head.brain.think())