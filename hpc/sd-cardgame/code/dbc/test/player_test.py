"""
Testing the program.
"""

import unittest

from dbc.player import *
from dbc.card import *


class TestPlayer(unittest.TestCase):
    
    @unittest.skip("The function prints.")
    def test_show_stats(self):
        player = Player()
        player.show_stats()
        pass

    def test_make_deck(self):
        player = Player()
        player.make_deck()
        self.assertEquals(random.choice(player.drawpile)['cost'], 0)
        self.assertEquals(len(player.drawpile), 10)

    def test_make_hand(self):
        player = Player()
        player.make_deck()
        player.make_hand()
        self.assertEquals(len(player.hand), player.handsize)

    def test_play_card(self):
        player = Player()
        player.make_deck()
        player.make_hand()
        atk, mon = player.hand[0]['attack'], player.hand[0]['money']
        player.play_card(0)
        self.assertEquals(player.attack, atk)
        self.assertEquals(player.money, mon)
    
    def test_play_all(self):
        player = Player()
        player.make_deck()
        player.make_hand()
        player.play_all()
        self.assertEquals(len(player.active), player.handsize)
    
    def test_buy_card(self):
        player = Player()
        card = Card(random.choice(player.data))
        player.buy_card(card)
        self.assertEquals(player.money, card.cost)
    
    def test_move_to_discard(self):
        player = Player()
        player.make_deck()
        player.make_hand()
        player.move_to_discard(player.hand)
        self.assertEquals(len(player.discard), player.handsize)

    def test_endturn(self):
        player = Player()
        player.make_deck()
        pile = len(player.drawpile)
        player.make_hand()
        player.play_all()
        player.endturn()
        self.assertEquals(player.money, 0)
        self.assertEquals(player.attack, 0)
        self.assertEquals(len(player.drawpile), pile)
