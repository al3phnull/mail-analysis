"""
Class to specify card values
"""

import sys
import json
import random

CARDFILE = '../res/cards.json'

class Card:
    """
    Specifies card values
    """

    def __init__(self, card):
        self.name = str(card['name'])
        self.attack = card['attack']
        self.money = card['money']
        self.cost = card['cost']


    def __getitem__(self, key):
        return self.card[key]
        

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


class Game:

    def __init__(self):
        self.data = []
        self.cardlist = []
        self.human = Player()
        self.bot = Player()
        self.humandeck = Pile()
        self.botdeck = Pile()
        self.central = Pile()
        self.supplement = Pile()
        self.ncentral = 36
        self.ndeck = 10
        self.nsupp = 10

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
        self.humandeck.build_player_pile(self.data['player'])
        self.botdeck.build_player_pile(self.data['player'])
                
        return self.central, self.supplement, self.humandeck, self.botdeck




def main():
    g = Game()
    g.deal_decks()
    g.play()

if __name__ == '__main__':
    main()
