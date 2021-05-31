#-------------------------------------------------------------------------------
# Classes for workers signal-slot mechanism
#-------------------------------------------------------------------------------

from PyQt5 import QtCore


class CommunicateLog(QtCore.QObject):
    myGUI_signal = QtCore.pyqtSignal([str, str])


class CommunicateProgress(QtCore.QObject):
    myGUI_signal = QtCore.pyqtSignal([float])


if __name__ == "__main__":
    print("Module test not implemented")