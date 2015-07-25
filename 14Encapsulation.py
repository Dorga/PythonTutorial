__author__ = 'jbowman'

# https://pythonspot.com/encapsulation/

class Car:

    __maxspeed = 0
    otherspeed = 0
    __name = ''

    def __init__(self):
        self.__updateSoftware()
        self.__maxspeed = 200
        self.otherspeed = 3000
        self.__name = 'Supercar'

    def drive(self):
        print('Driving... ' + str(self.__maxspeed) + ' mph')

    def __updateSoftware(self):
        print('Updating software...')

    def setMaxSpeed(self, speed):
        self.__maxspeed = speed
        print('New maxspeed set to: ' + str(self.__maxspeed))

redcar = Car()
redcar.drive()
redcar.setMaxSpeed(155)
redcar.drive()
print(redcar.otherspeed)
redcar.otherspeed = 2
print(redcar.otherspeed)