"""
Class to specify card values
"""
import random
from card import Card

class Player:

    def __init__(self):
        self.money = 0
        self.attack = 0
        self.health = 30
        self.hand = Pile()
        self.active = Pile()
        self.discard = Pile()
        self.drawpile = Pile()
        self.handsize = 5

    def make_hand(self, card):
        while len(self.hand) < self.handsize:
            self.hand.add(card)

    def play_card(self, card):
        played = self.hand.pop(card)
        self.money += played.money
        self.attack += played.attack

        return self.money, self.attack

    def play_all(self):
        while len(hand) > 0:
            play_card()
