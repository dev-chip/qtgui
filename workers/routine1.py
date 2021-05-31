# -------------------------------------------------------------------------------
# A generic worker thread example
# -------------------------------------------------------------------------------

from time import sleep
import threading

from workers.classes import CommunicateLog, CommunicateProgress

from logger import init_signal_logger


class LoadThread(threading.Thread):
    """
        A thread that downloads and builds simulation whilst communicating with the UI.
    """

    def __init__(self, logger_callback, progress_callback):
        """
            init
        """
        threading.Thread.__init__(self)

        self.logCom = CommunicateLog()
        self.logCom.myGUI_signal.connect(logger_callback)
        self.log = init_signal_logger(self.logCom.myGUI_signal)

        self.kill = False
        self.pause = False

        self.progress = CommunicateProgress()
        self.progress.myGUI_signal.connect(progress_callback)

    def run(self):
        """
            Runs routine whilst commminicating with GUI
        """
        self.log.debug("Thread alive")

        # Progress bar initial value
        value = 0.0

        # Run for as long as the GUI mainloop is running
        while not self.kill and value < 100:

            # Increment progress bar completion value
            value += 1

            # Callback
            self.progress.myGUI_signal.emit(value)
            self.log.verbose("Emitted value " + str(value))
            sleep(0.05)

            # Repeatedly sleep in a loop while the user has chosen to pause
            while self.pause and not self.kill:
                sleep(0.05)
        self.log.debug("Thread dead")

    def kill(self):
        """
            Kill the thread
        """
        self.kill = True

    def pause(self):
        """
            Pause the thread process
        """
        self.pause = True


if __name__ == "__main__":
    print("Module test not implemented")
