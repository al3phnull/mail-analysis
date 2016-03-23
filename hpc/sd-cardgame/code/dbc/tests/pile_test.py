"""
Testing the program.
"""

import unittest
from dbc.pile import *
from dbc.data import *
from dbc.player import *
from dbc.card import *


class TestPile(unittest.TestCase):

    def test_len(self):
        pile = Pile()
        self.assertEqual(len(pile), 0)

    def test_create_pile(self):
        pile = Pile()
        testcardlist = Data().load_data('res/cards.json')['central']
        ncards = 10
        cards = pile.create_pile(testcardlist, ncards)
        self.assertEqual(len(cards), ncards)
        
    def test_build_player_pile(self):
        pile = Pile()
        testhuman = Data().load_data('res/cards.json')['player']
        pile.build_player_pile(testhuman)
        self.assertEqual(pile.cards[0]['cost'], 0)

    def test_merge_piles(self):
        adding_pile = Pile()
        pile_to_add_to = Pile()
        testpile = Data().load_data('res/cards.json')['central']
        adding_pile.create_pile(testpile, 5)
        pile_to_add_to.create_pile(testpile, 5)
        pile_lens = len(adding_pile) + len(pile_to_add_to)
        adding_pile.merge_piles(pile_to_add_to)
        self.assertEqual(len(pile_to_add_to), pile_lens)

    @unittest.skip("The function prints. Nothing more")
    def test_display_cards(self):
        pass
