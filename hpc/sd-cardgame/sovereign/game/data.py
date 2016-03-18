"""
Class to specify card values
"""

import sys
import json
import random


class Data:
    def __init__(self):
        self.data = []

    def load_cards(self, cardfile = '../res/cards.json'):
        with open(cardfile) as card_file:
            self.data = json.load(card_file)

        return self.data
