"""
Class to specify card values
"""

import random

from card import *
from data import *

class Pile(object):
    """
    Gives the properties of card piles
    """
    def __init__(self):
        self.cards = []
        self.text = Data().load_data('res/strings.json')

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
        """
        Gets card indexes and creates a drawpile
        using the player card dictionary list
        :param squire_index: Index of 'Squire' card dict
        :param serf_index: Index of 'Serf' card dict
        """
        squire_index = next(ix for (ix, d) in enumerate(cardlist) if d['name'] == 'Squire')
        serf_index = next(ix for (ix, d) in enumerate(cardlist) if d['name'] == 'Serf')

        [self.cards.append(Card(cardlist[serf_index])) for i in range(8)]
        [self.cards.append(Card(cardlist[squire_index])) for i in range(2)]

        return self.cards

    def shuffle(self):
        """
        Shuffles the pile
        """
        random.shuffle(self.cards)

    def put(self, card):
        """
        Place a card on top of the pile
        """
        self.cards.append(card)

    def draw(self, card=0):
        """
        Remove a card from the top of pile
        """
        return self.cards.pop(card)

    def merge_piles(self, main_pile):
        """
        Take the pile and shuffle it into another pile
        """
        main_pile.cards.extend(self.cards)
        main_pile.shuffle()
        self.cards = []

    def display_cards(self):
        """
        Goes through a pile and prints the card strings
        one by one
        """
        if len(self.cards) == 0:
            print self.text['empty']
        else:
            for index, card in enumerate(self.cards):
                print self.text['cvals1'] % \
                    (index, card.name, card.cost, card.attack, card.money)


