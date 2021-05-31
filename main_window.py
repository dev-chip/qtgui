# -------------------------------------------------------------------------------
# Name:        main_window.py
# Purpose:     Main window example.
#
# Author:      James Cook
#
# Created:     30/09/2020
# Copyright:   (c) James Cook 2020
# -------------------------------------------------------------------------------

from gen import MainWindowGenerated
from thread import thread_log
from window import Window
from logger import init_console_logger

from workers.routine1 import LoadThread

logger = init_console_logger(name="gui")


class MainWindow(Window):

    def __init__(self):

        logger.debug("Setting up UI")
        super(Window, self).__init__()
        self.ui = MainWindowGenerated.Ui_MainWindow()
        self.ui.setupUi(self)

        logger.verbose("Initialising GUI logger")
        self.init_GUI_logger(logger)

        logger.verbose("Initialising signals")
        self.init_signals()

        logger.info("GUI initialised")

    def init_signals(self):
        """
            Initialises widget signals
        """
        pass

    def thread_count(self):
        """
            Starts a thread that performs [process]
        """
        # disable button
        self.ui.pushButton_thread_count.setEnabled(False)
        # start thread
        logger.debug("Starting thread...")
        t = LoadThread(self.log_thread_callback, self.progress_thread_callback)
        t.start()
        logger.info("Thread started")

    def log_thread_callback(self, text, log_type=""):
        """
            Logs messages recieved from a thread
        """
        logger.verbose("Thread send values " + str(text) + ", " + str(log_type) + " to the MainWindow.")
        thread_log(logger, text, log_type)


if __name__ == "__main__":
    print ("No module test implemented.")