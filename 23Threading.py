__author__ = 'jbowman'

# https://pythonspot.com/threading/

import time
import threading
from threading import *

# thread class
class MyThread(threading.Thread):

     def __init__(self, x):
         self.__x = x
         threading.Thread.__init__(self)

     def run(self):
         print(str(self.__x))

# start 10 threads
for ii in range(10):
    MyThread(ii).start()

def hello():
    print("Hello World")

# create thread
t = Timer(10.0, hello)

# start thread after 10 seconds
t.start()

def handleClient():
    while(True):
        print("Waiting for client 1...")
        time.sleep(5)

def handleClientTwo():
    while(True):
        print("Waiting for client 2...")
        time.sleep(5)

# create threads
t = Timer(5.0, handleClient)
t2 = Timer(3.0, handleClientTwo)

# start threads
t.start()
t2.start()
