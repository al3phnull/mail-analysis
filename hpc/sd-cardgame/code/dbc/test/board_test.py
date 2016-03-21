"""
Testing the program.
"""

import unittest
from dbc.board import *


class TestBoard(unittest.TestCase):

    def test_deal_decks(self):
        board = Board()
        board.deal_decks()
        self.assertEqual(len(board.maindeck), board.nmain)
        self.assertEqual(len(board.supplement), board.nsupp)

    def test_draw_active(self):
        board = Board()
        board.deal_decks()
        test_card = board.maindeck[0]
        board.draw_active()
        self.assertEqual(board.active[0], test_card)
        

    def test_update_active(self):
        board = Board()
        board.deal_decks()
        board.draw_active()
        board.active.draw()
        self.assertEqual(len(board.active), board.ncen - 1)
        board.update_active()
        self.assertEqual(len(board.active), board.ncen)
        self.assertEqual(len(board.maindeck), board.nmain - board.ncen - 1)
