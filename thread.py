#
# Functions for handling thread functionality
#

import ctypes


def kill_thread(t):
    """
        Forces a thread to die.
        Takes paramater 't' - a threading.Thead() instance.
    """
    exc = ctypes.py_object(SystemExit)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(t.ident), exc)
    if res == 0:
        raise Exception("nonexistent thread id")
    elif res > 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(t.ident, None)
        raise Exception("PyThreadState_SetAsyncExc failed")
    else:
        return 0
    return 1


def thread_log(logger, text, log_type):
    """
        Logs messages received by callback function from threads.
    """
    if log_type == "info":
        logger.info(text)
    elif log_type == "debug":
        logger.debug(text)
    elif log_type == "warning":
        logger.warning(text)
    elif log_type == "verbose":
        logger.verbose(text)
    elif log_type == "error":
        logger.error(text)
    else:
        logger.error("'" + log_type + "' not recognised as a log type. Message to be logged: '" + text + "'")


if __name__ == "__main__":
    print ("No module test implemented.")
