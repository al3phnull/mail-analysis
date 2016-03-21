"""
Testing the program.
"""

import unittest


from dbc.data import *
from dbc.game import *


class TestData(unittest.TestCase):

    def test_load_data(self):
        arc = Data().load_data('res/cards.json')['central'][0]
        self.assertEqual(str(arc['name']), 'Archer')
