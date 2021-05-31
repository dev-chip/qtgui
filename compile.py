import os
import datetime

from PyQt5 import uic

THIS_PATH = os.path.abspath(os.path.dirname(__file__))
UI_PATH = os.path.join(THIS_PATH, "ui")
GEN_PATH = os.path.join(THIS_PATH, "gen")


def compile_ui(ui_file_name, ui_file_path, gen_file_path):
    print("Compiling '{}' ...".format(ui_file_name), end="")
    fp = open(gen_file_path, "w")
    uic.compileUi(ui_file_path, fp, from_imports=True)
    fp.close()
    print(" Done")


def compile_if_modified():

    last_modified = 0
    count = 0

    # checks
    if not os.path.isdir(UI_PATH):
        raise Exception("UI_PATH '{}' cannot be found.".format(UI_PATH))
    if not os.path.isdir(GEN_PATH):
        raise Exception("UI_PATH '{}' cannot be found.".format(GEN_PATH))

    # get ui files
    ui_files = [_ for _ in os.listdir(UI_PATH) if (os.path.isfile(os.path.join(UI_PATH, _)) and _[-3:] == '.ui')]
    if len(ui_files) == 0:
        print("No ui files present at '{}'".format(UI_PATH))
        return

    # compile modified files
    for ui_file_name in ui_files:
        gen_file_name = ui_file_name.replace('.ui', 'Generated.py')

        gen_file_path = os.path.join(GEN_PATH, gen_file_name)
        ui_file_path = os.path.join(UI_PATH, ui_file_name)

        ui_mod_timestamp = os.path.getmtime(ui_file_path)

        if ((not os.path.isfile(gen_file_path)) or
           ui_mod_timestamp > os.path.getmtime(gen_file_path)):
            compile_ui(ui_file_name, ui_file_path, gen_file_path)
            count += 1

        if ui_mod_timestamp > last_modified:
            last_modified = ui_mod_timestamp

    print("\n" + ("-"*50))
    print("Compiled {} files".format(count))
    print("Last ui modified on {}".format(datetime.datetime.fromtimestamp(last_modified).strftime("%m/%d/%Y at %H:%M:%S")))
    print(("-"*50) + "\n")


if __name__ == "__main__":
    compile_if_modified()


