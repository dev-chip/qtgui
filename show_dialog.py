#
# Show a qt message dialog
#

from PyQt5.QtWidgets import QDialog
from gen import (messageGenerated,
                 confirmGenerated)


def show_message_dialog(text):
    """
        Shows a generic message dialog to the user displaying the text
        passed. Utilizes word wrap.
    """

    dialog = QDialog()
    interface = messageGenerated.Ui_Dialog()
    interface.setupUi(dialog)
    interface.label.setText(text)
    dialog.exec_()


def show_confirm_dialog(text):
    """
        Shows a generic confirm dialog to the user displaying the text
        passed. Utilizes word wrap.
    """
    dialog = QDialog()
    interface = confirmGenerated.Ui_Dialog()
    interface.setupUi(dialog)
    interface.label.setText(text)
    if dialog.exec_() == 1:
        return True
    return False


# def show_line_edit_dialog(text):
#     """
#         Shows a generic line edit dialog to the user displaying the text
#         passed. Utilizes word wrap.
#     """
#     dialog = QDialog()
#     interface = lineEditEntryGenerated.Ui_Dialog()
#     interface.setupUi(dialog)
#     interface.label.setText(text)
#     if dialog.exec_() == 1:
#         return True, str(interface.lineEdit.text())
#     else:
#         return False, ""


if __name__ == "__main__":
    print("No module test implemented.")
