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
        """
        Displays player's money and attack
        """
        print "Money: %s, Attack: %s" % (self.money, self.attack)

    def make_deck(self):
        """
        Builds a deck from Serfs and Squires
        """
        self.drawpile.build_player_pile(self.data)

    def make_hand(self):
        """
        Assemble a hand by picking up cards from the
        top of the drawpile
        """
        while len(self.hand) < self.handsize:
            if len(self.drawpile) == 0:
                self.discard.shuffle()
                self.deck = self.discard
                self.discard = Pile()
            card = self.drawpile.draw()
            self.hand.put(card)

    def play_card(self, index):
        """
        Takes a card from the player's hand and adds
        its stats to the player's. 
        :param index: the index of the card in the hand
        """
        card = self.hand.draw(index)
        self.active.put(card)
        self.money += card.money
        self.attack += card.attack

    def play_all(self):
        """
        Play all cards at once
        """
        for index in range(len(self.hand)):
            self.play_card(0)

    def move_to_discard(self, pile):
        """
        Moves all cards from a target pile to
        a discard pile
        :param pile: The pile from which cards are removed
        """
        for x in range(len(pile)):
            card = pile.draw()
            self.discard.put(card)

    def endturn(self):
        """
        Steps taken at the end of the turn.
        The active and hand piles are 
        merged with the discard pile then the
        discard pile is shuffled into the drawpile
        money and attack are reinitialised
        """
        if len(self.active) > 0:
            self.move_to_discard(self.active)

        if len(self.hand) > 0:
            self.move_to_discard(self.hand)

        self.discard.merge_piles(self.drawpile)
        self.money = 0
        self.attack = 0
