# -------------------------------------------------------------------------------
# Name:        window.py
# Purpose:     superclass window
#
# Author:      g852706 - James Cook
#
# Created:     03/03/2020
# -------------------------------------------------------------------------------

from PyQt5.QtWidgets import QMainWindow

import logging

from text_edit_logger import QPlainTextEditLogger
from logger import set_logger_level, init_console_logger
from cfg import get_configs, overwrite_config

logger = init_console_logger(name="gui")


class Window(QMainWindow):
    """
        Base class to be inherited by Qt Windows
    """
    def __init__(self):
        self.ui = None

    def init_GUI_logger(self, logger):
        """
            Initialises the textEdit logger.
        """
        if self.ui != None:
            try:
                logger.addHandler(QPlainTextEditLogger(self.ui.textEdit))
                set_logger_level(logger.level, name="gui") # essential to set the new handler's log level
            except Exception as e:
                raise "Failed to add textEdit as a handler for logger: " + str(e)

            try:
                self.ui.actionDISABLE.triggered.connect(self.logger_disable_checked)
                self.ui.actionINFO.triggered.connect(self.logger_info_checked)
                self.ui.actionDEBUG.triggered.connect(self.logger_debug_checked)
                self.ui.actionWARNING.triggered.connect(self.logger_warning_checked)
                self.ui.actionVERBOSE.triggered.connect(self.logger_verbose_checked)

                level = logger.level
                if level == logging.CRITICAL:
                    self.logger_disable_checked()
                elif level ==  logging.WARNING:
                    self.logger_warning_checked()
                elif level == logging.INFO:
                    self.logger_info_checked()
                elif level == logging.DEBUG:
                    self.logger_debug_checked()
                elif level == 5:
                    self.logger_verbose_checked()
                else:
                    logger.critical("Value '" + level + "' from config file is not recognised"
                                                       "as a log level. Setting level as debug.")
                    self.logger_debug_checked()
            except ValueError:
                logger.warning("Menubar log level selection not setup - interface does not contain required menubar")

    def uncheck_all_log_options(self):
        """
            Un-checks all log level logger menu items
        """
        self.ui.actionDISABLE.setChecked(False)
        self.ui.actionWARNING.setChecked(False)
        self.ui.actionINFO.setChecked(False)
        self.ui.actionDEBUG.setChecked(False)
        self.ui.actionVERBOSE.setChecked(False)

    def logger_disable_checked(self):
        """
            Disables the logger
        """
        self.uncheck_all_log_options()
        self.ui.actionDISABLE.setChecked(True)
        set_logger_level(logging.INFO, name="gui") # so the info log can be seen before change
        logger.info("Logger DISABLED")
        logging.disable(logging.CRITICAL)
        self.save_log_level(logging.CRITICAL)

    def logger_warning_checked(self):
        """
            Sets the logger level to WARNING
        """
        self.uncheck_all_log_options()
        self.ui.actionWARNING.setChecked(True)
        set_logger_level(logging.INFO, name="gui") # so the info log can be seen before change
        logger.info("Logger level set to 'WARNING'")
        set_logger_level(logging.WARNING, name="gui")
        self.save_log_level(logging.WARNING)

    def logger_info_checked(self):
        """
            Sets the logger level to INFO
        """
        self.uncheck_all_log_options()
        self.ui.actionINFO.setChecked(True)
        set_logger_level(logging.INFO, name="gui")
        logger.info("Logger level set to 'INFO'")
        self.save_log_level(logging.INFO)

    def logger_debug_checked(self):
        """
            Sets the logger level to DEBUG
        """
        self.uncheck_all_log_options()
        self.ui.actionDEBUG.setChecked(True)
        set_logger_level(logging.DEBUG, name="gui")
        logger.info("Logger level set to 'DEBUG'")
        self.save_log_level(logging.DEBUG)

    def logger_verbose_checked(self):
        """
            Sets the logger level to VERBOSE
        """
        self.uncheck_all_log_options()
        self.ui.actionVERBOSE.setChecked(True)
        set_logger_level(5, name="gui")
        logger.info("Logger level set to 'VERBOSE'")
        self.save_log_level(5)

    def save_log_level(self, level):
        config = get_configs()
        config["COMMON"]["log_level"] = str(level)
        overwrite_config(config)
        logger.debug("Log level saved")

if __name__ == "__main__":
    print ("No module test implemented.")
