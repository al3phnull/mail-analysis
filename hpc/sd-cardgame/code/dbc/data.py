"""
Class to load json data
"""

import json

class Data(object):
    """
    Used to accommodate the import of resource files
    """
    def __init__(self):
        self.data = []

    def load_data(self, textfile):
        """
        Takes a json file and feeds it into the
        program.
        :param textfile: a json file
        """
        with open(textfile) as in_file:
            self.data = json.load(in_file)

        return self.data
