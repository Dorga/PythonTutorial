__author__ = 'jbowman'

# https://pythonspot.com/python-subprocess/

from subprocess import Popen, PIPE

# doesn't work?
process = Popen(['cat', 'test.py'], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
print(stdout)