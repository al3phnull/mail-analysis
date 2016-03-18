"""
Class to specify player attributes and functions
"""
import sys
import random

from data import Data
from pile import Pile



class Player:

    def __init__(self):
        self.data = Data().load_cards()
        self.money = 0
        self.attack = 0
        self.health = 30
        self.hand = Pile()
        self.active = Pile()
        self.discard = Pile()
        self.drawpile = Pile()
        self.handsize = 5

    def move_to_pile(self, card, target_pile):
        for p in (self.drawpile, self.discard, self.hand):
            if card in p:
                p.take(card)
        target_pile.add(card)

    def make_deck(self):
        return self.drawpile.build_player_pile(self.data['player'])

    def make_hand(self, card):
        while len(self.hand) < self.handsize:
            self.hand.add(card)

    def play_card(self, card):
        self.hand.take(card)
        self.money += card.money
        self.attack += card.attack
        self.discard.add(card)

    def play_all(self):
        while len(hand) > 0:
            play_card()

