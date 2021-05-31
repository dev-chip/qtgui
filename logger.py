# -------------------------------------------------------------------------------
# Name:        logger.py
# Purpose:     Handles logger initialisation and immitates a logger
#              object for threads to callback their log messages.
#
# Author:      g852706 - James Cook
#
# Created:     03/03/2020
# -------------------------------------------------------------------------------

import logging


# Additional log level for verbose information for debugging
VERBOSE_LOGGER_LEVEL = 5
logging.addLevelName(VERBOSE_LOGGER_LEVEL, 'VERBOSE')
def verbose(self, message, *args, **kws):
    self._log(VERBOSE_LOGGER_LEVEL, message, args, **kws)
logging.Logger.verbose = verbose


class init_signal_logger:
    """
        Used to imitate a logger class to receive log messages
        as a callback by a thread
    """
    def __init__(self, signal):
        self.signal = signal
    def info(self, text):
        self.signal.emit(text, "info")
    def debug(self, text):
        self.signal.emit(text, "debug")
    def warning(self, text):
        self.signal.emit(text, "warning")
    def verbose(self, text):
        self.signal.emit(text, "verbose")
    def error(self, text):
        self.signal.emit(text, "error")


def init_console_logger(log_level=logging.DEBUG, name="bob", stream_handler=True, file_handler=False):
    """
        Gets a logger of the name passed, returning an existing instance
        if the name passed is already created or initialises a new logger
        if a different name is passed.

        Configurations for handlers that are passed are only used if the
        logger is not already instantiated.
    """
    logger = logging.getLogger(name)
    # check if logger exist (if it already has handlers)
    if len(logger.handlers) > 0:
        return logger

    logger.setLevel(log_level)
    formatter = logging.Formatter(fmt = '[%(asctime)s]\t%(levelname)s:\t%(message)s', datefmt = '%H:%M:%S')

    if file_handler:
        fh = logging.FileHandler("log.log")
        fh.setLevel(log_level)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    if stream_handler:
        sh = logging.StreamHandler()
        sh.setLevel(log_level)
        sh.setFormatter(formatter)
        logger.addHandler(sh)

    return logger


def set_logger_level(log_level, name="bob"):
    """
        Sets the logger level of the logger and all handlers
        for the logger passed.
    """
    logging.disable(logging.NOTSET)
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    for handler in logger.handlers:
        handler.setLevel(log_level)
    logger.verbose("Log level value set to " + str(log_level))


if __name__ == '__main__':
    level = 20
    print ("Module test - logger (level " + str(level) + ")")
    testlogger = init_console_logger(name = "bob")
    set_logger_level(20, "bob")
    print(testlogger.level)
    testlogger.info('Console Log initialized')
    testlogger.verbose('testmessage: "verbose"')
    testlogger.debug('testmessage: "debug"')
    testlogger.info('testmessage: "info"')
    testlogger.warn('testmessage: "warn"')
    testlogger.error('testmessage: "error"')
    testlogger.critical('testmessage: "critical"')
