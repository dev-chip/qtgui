#
# Functions for reading and writing configs
#

import os
import configparser

CONFIGS_PATH = os.path.abspath(os.path.dirname(__file__))


def get_configs():
    """
        Returns the data stored in the config file
        as a dictionary
    """
    try:
        config = configparser.ConfigParser()
        file_path = os.path.join(CONFIGS_PATH, 'configs.ini')
        if not os.path.isfile(file_path):
            raise Exception("file '" + file_path + "' not found")
        config.read(file_path)
        return config
    except Exception as e:
        raise Exception("Failed reading configs: " + str(e))


def overwrite_config(config):
    """
        Overwrites the current config file with data
        from the ConfigParser object passed
    """
    try:
        with open(os.path.join(CONFIGS_PATH, 'configs.ini'), 'w') as configfile:
            config.write(configfile)
    except Exception as e:
        raise Exception("Failed writing configs: " + str(e))
