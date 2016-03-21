"""
Class to specify card values
"""

import sys
import os
import json
import random
import time

from pile import *
from data import *

class Player(object):

    def __init__(self):
        self.data = Data().load_data('res/cards.json')['player']
        self.money = 0
        self.attack = 0
        self.health = 30
        self.hand = Pile()
        self.active = Pile()
        self.discard = Pile()
        self.drawpile = Pile()
        self.handsize = 5

    def show_stats(self):
        print "Money: %s, Attack: %s" % (self.money, self.attack)

    def make_deck(self):
        self.drawpile.build_player_pile(self.data)

    def make_hand(self):
        while len(self.hand) < self.handsize:
            if len(self.drawpile) == 0:
                self.discard.shuffle()
                self.deck = self.discard
                self.discard = Pile()
            card = self.drawpile.draw()
            self.hand.put(card)

    def play_card(self, index):
        card = self.hand.draw(index)
        self.active.put(card)
        self.money += card.money
        self.attack += card.attack

    def play_all(self):
        for index in range(len(self.hand)):
            self.play_card(0)

    def buy_card(self, card):
        self.money -= card.cost
        self.discard.put(card)

    def move_to_discard(self, pile):
        for x in range(len(pile)):
            card = pile.draw()
            self.discard.put(card)

    def endturn(self):
        if len(self.active) > 0:
            self.move_to_discard(self.active)

        if len(self.hand) > 0:
            self.move_to_discard(self.active)

        self.discard.merge_piles(self.drawpile)
        self.money = 0
        self.attack = 0
