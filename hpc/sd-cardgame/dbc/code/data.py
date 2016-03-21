"""
Class to load json data
"""

import json

class Data(object):
    def __init__(self):
        self.data = []

    def load_data(self, textfile):
        with open(textfile) as in_file:
            self.data = json.load(in_file)

        return self.data
