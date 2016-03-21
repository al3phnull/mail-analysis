"""
Class to specify card values
"""

import sys
import os
import json
import random
import time

from player import *


class Bot(Player):

    def __init__(self):
        Player.__init__(self)
        self.strategy = 'aggressive'

    def set_strat(self, strategy):
        if strategy == 'aggressive':
            bot_aggressive()

        elif strategy == 'acquisitive':
            bot_acquisitive()

    def bot_aggressive(self):
        pass


    def bot_acquisitive(self):
        pass


