"""
Testing the program.
"""

import unittest
from sovereign.game import Card

class TestCards(unittest.TestCase):

    def test_load_cards:
        test_data = []
        test_data["name"] = "Archer"
        test_data["cost"] = 2
        test_data["attack"] = 3
        test_data["money"] = 0

