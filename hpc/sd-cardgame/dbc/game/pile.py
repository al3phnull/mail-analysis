"""
Class to specify card values
"""

import random

from data import Data
from card import Card


class Pile:
    """
    Gives the properties of card piles
    """
    def __init__(self):
        self.cards = []


    def __len__(self):
        return len(self.cards)

    def __getitem__(self, key):
        return self.cards[key]

    def create_pile(self, cardlist, ncards):
        """
        Create a deck of size ncards from the
        card list
        """
        for i in range(ncards):
            self.cards.append(Card(random.choice(cardlist)))

        return self.cards

    def build_player_pile(self, cardlist):
        squire_index = next(ix for (ix, d) in enumerate(cardlist) if d['name'] == 'Squire')
        serf_index = next(ix for (ix, d) in enumerate(cardlist) if d['name'] == 'Squire')
        [self.cards.append(Card(cardlist[serf_index])) for i in range(8)]
        [self.cards.append(Card(cardlist[squire_index])) for i in range(2)]
        return self.cards

    def shuffle(self):
        """
        Shuffles the pile
        """
        random.shuffle(self.cards)

    def add(self, card):
        """
        Place a card on top of the pile
        """
        self.cards.append(card)

    def take(self, card):
        """
        Place a card on top of the pile
        """
        self.cards.remove(card)

    def draw(self):
        """
        Remove a card from the pile
        """
        return self.cards.pop()

    def merge_piles(self, main_pile):
        """
        Take the pile and shuffle it into the main deck
        """
        main_pile.cards.extend(self.cards)
        main_pile.shuffle()
        self.cards = []
