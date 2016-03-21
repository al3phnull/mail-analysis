"""
Class to specify computer player functions
WIP: Would be used for cleaning up bot AI
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
            self.bot_aggressive()

        elif strategy == 'covetous':
            self.bot_covetous()

    def bot_aggressive(self):
        pass

    def bot_covetous(self):
        pass


