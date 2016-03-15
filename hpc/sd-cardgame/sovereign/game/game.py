"""
Class to specify card values
"""

import sys
import json
import random
from card import Card

class Game:

    def __init__(self):
        self.data = []
        self.cardlist = []
        self.deck = Pile()
        self.central = Pile()
        self.supplement = Pile()
        self.ncentral = 36
        self.ndeck = 10
        self.nsupp = 10
        self.human = Player()
        self.bot = Player()

    def load_cards(self, cardfile = '../res/cards.json'):
        with open(cardfile) as card_file:
            self.data = json.load(card_file)

        return self.data

    def get_cards(self, data, pile):
        for card in data[pile]:
            self.cardlist.append(card)

        return self.cardlist

    def deal_decks(self):
        self.data = self.load_cards()
        self.central.create_pile(self.data['central'], self.ncentral)

        self.supplement.create_pile(self.data['supplement'], self.nsupp)

        [self.deck.add(filter(lambda pcards: pcards['name'] == 'Serf', \
                self.data['player']) for i in range(8))]
        [self.deck.add(filter(lambda pcards: pcards['name'] == 'Squire', \
                self.data['player']) for i in range(2))]

        return self.central, self.supplement, self.deck

