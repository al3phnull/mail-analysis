"""
Class to specify card values
"""

import sys
import os
import json
import random
import time


from data import *
from pile import *

class Board(object):

    def __init__(self):
        self.data = Data().load_data('res/cards.json')
        self.active = Pile()
        self.maindeck = Pile()
        self.supplement = Pile()
        self.nmain = 36
        self.nsupp = 10
        self.ncen = 5
        self.strategy = 0

    def deal_decks(self):
        self.maindeck.create_pile(self.data['central'], self.nmain)
        self.supplement.create_pile(self.data['supplement'], self.nsupp)


    def draw_active(self):
        for c in range(self.ncen):
            card = self.maindeck.draw()
            self.active.put(card)

    def update_active(self):
        if len(self.active) < self.ncen:
            if len(self.maindeck) > 0:
               card = self.maindeck.draw()
               self.active.put(card)
            else:
                pass

