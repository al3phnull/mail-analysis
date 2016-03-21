"""
Testing the program.
"""

import unittest
from dbc.bot import *


class TestBot(unittest.TestCase):

    def test_set_strat(self):
        bot = Bot()
        bot.set_strat('aggressive')
        bot.set_strat('covetous')

    def test_bot_aggressive(self):
        bot = Bot()
        bot.bot_aggressive()
        pass

    def test_bot_acquisitive(self):
        bot = Bot()
        bot.bot_covetous()
        pass
        
