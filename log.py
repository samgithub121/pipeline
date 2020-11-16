"""
@Description : This py file is a wrapper on top of python logging module.
@ Author : Sam Mathew
@ Created on : 25/12/2019
@ Modified on : 28/12/2019

"""

# Global imports
import logging
import sys
import os


class Log(object):

    @staticmethod
    def capture_log():
        """ Capture event logs
        parameter : Path to the event logs
        return : logger instance
        """
        path = os.path.join(os.path.abspath(os.path.curdir), "es_logs.log")
        device_name = "Skylo_Auto"

        log = logging.getLogger(path)
        log.setLevel(logging.DEBUG)
        log.handlers = []

        # create file handler which logs even debug messages
        # log_file_name = os.path.join(path, "london_theatre.log")

        fh = logging.FileHandler(path)
        fh.setLevel(logging.DEBUG)

        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.DEBUG)

        # Create formatter and add it to the handler
        formatter = logging.Formatter(
            '%(asctime)s - {0} - %(levelname)s - %(message)s'.format(
                device_name),
            "%Y-%m-%d %H:%M:%S")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        #add the handlers to the logger
        log.addHandler(fh)
        log.addHandler(ch)

        log.handlers[-1]

        return log
