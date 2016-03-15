"""
Class to specify card values
"""
import random
from card import Card

class Pile:
    """
    Gives the properties of card piles
    """

    def __init__(self):
        self.cards = []


    def __len__(self):
        return len(self.cards)


    def create_pile(self, cardlist, ncards):
        """
        Create a deck of size ncards from the
        card list
        """
        for i in range(ncards):
            self.cards.append(random.choice(cardlist))

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

    def remove(self, card):
        """
        Remove a card from the pile
        """
        self.cards.pop(card)

    def merge_piles(self, main_pile):
        """
        Take the pile and shuffle it into the main deck
        """
        main_pile.cards.extend(self.cards)
        main_pile.shuffle()
        self.cards = []

