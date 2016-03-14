"""
Testing the program.
"""

import unittest
from card import *


class TestCards(unittest.TestCase):

    def card_test(self):
        test_dict = {
                'name' : 'Archer',
                'attack' : 3,
                'money' : 0,
                'cost' : 2
                }
        card = Card(test_dict)
        self.assertEqual(type(card.name), str)
        self.assertEqual(type(card.attack), int) 
        self.assertEqual(type(card.money), int)
        self.assertEqual(type(card.cost), int)


    def test_load_cards(self):
        g = Game()
        arc = g.load_cards('../res/cards.json')['central'][0]
        self.assertEqual(str(arc['name']), 'Archer')

        



