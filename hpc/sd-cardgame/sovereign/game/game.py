"""
Class to specify card values
"""

import sys
import json
import random

from data import Data
from card import Card
from pile import Pile
from player import Player
#from bot import Bot


class Game:

    def __init__(self):
        self.data = Data().load_cards()
        self.cardlist = []
        self.human = Player()
        self.bot = Player()
        self.central = Pile()
        self.supplement = Pile()
        self.ncentral = 36
        self.ndeck = 10
        self.nsupp = 10


    def get_cards(self, data, pile):
        for card in data[pile]:
            self.cardlist.append(card)

        return self.cardlist

    def deal_decks(self):
        self.central.create_pile(self.data['central'], self.ncentral)

        self.supplement.create_pile(self.data['supplement'], self.nsupp)
                
        return self.central, self.supplement
    
    def play(self):
        pass
