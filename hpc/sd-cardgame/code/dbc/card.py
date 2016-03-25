"""
Class to specify card values
"""
from data import Data

class Card(object):
    """
    Specifies card values
    """
    def __init__(self, card):
        self.text = Data().load_data('res/strings.json')
        self.card = card
        self.name = str(card['name'])
        self.attack = card['attack']
        self.money = card['money']
        self.cost = card['cost']

    def __getitem__(self, key):
        return self.card[key]

    def __str__(self):
        return self.text['cvals'] % \
                (self.name, self.cost, self.attack, self.money)
