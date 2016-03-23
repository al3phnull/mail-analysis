"""
Testing the program.
"""

import unittest
from dbc.card import *
from dbc.data import *


class TestCards(unittest.TestCase):

    def test_card(self):
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

        self.assertEqual(card['name'], 'Archer')

        text = Data().load_data('res/strings.json')['cvals']
        self.assertEqual('%s' % card, text % (card.name, card.cost, card.attack, card.money))
