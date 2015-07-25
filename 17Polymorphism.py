__author__ = 'jbowman'

# https://pythonspot.com/poylmorphism/

class Bear(object):
    def sound(self):
        print("Groarrr")

class Dog(object):
    def sound(self):
        print("Ruffff")

def makeSound(animalType):
    animalType.sound()

bearObj = Bear()
dogObj = Dog()

makeSound(bearObj)
makeSound(dogObj)

class Document:
    def __init__(self, name):
        self.name = name

    def show(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Pdf(Document):
    def show(self):
        return 'Show pdf contents!'

class Word(Document):
    def show(self):
        return 'Show word contents!'

# class Txt(Document):
#     def type(self):
#         print("I'm a text file!")

documents = [Pdf('PdfDoc1'), Pdf('PdfDoc2'), Word('WordDoc1')]
# documents = [Pdf('PdfDoc1'), Pdf('PdfDoc2'), Word('WordDoc1'), Txt('TxtDoc1')]

for ii in documents:
    print(ii.name + ': ' + ii.show())

class Car:
    def __init__(self, name):
        self.name = name

    def drive(self):
        raise NotImplementedError()

    def stop(self):
        raise NotImplementedError

class Sportscar(Car):
    def drive(self):
        return 'Sportscar driving!'

    def stop(self):
        return 'Sportscar stopping!'

class Truck(Car):
    def drive(self):
        return 'Truck driving!'

    def stop(self):
        return 'Truck stopping!'

cars = [Truck('BananaTruck'), Truck('OrangeTruck'), Sportscar('RedViper')]

for ii in cars:
    print(ii.name + ': ' + ii.drive())

