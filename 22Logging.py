__author__ = 'jbowman'

# https://pythonspot.com/logging/

import logging

# level DEBUG means that the logging is more verbose for basic info,
# not just warning or greater
desktopPath = 'c:\\users\\jbowman\\desktop'
programLogPath = desktopPath + '\program.log'
logging.basicConfig(filename=programLogPath,
                    level=logging.DEBUG,
                    format='%(asctime)s %(message)s')
logging.info('Logging started.')
logging.warning('This is a warning!')
logging.warning('This is another msg!')

