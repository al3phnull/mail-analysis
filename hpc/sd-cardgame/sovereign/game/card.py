"""
Class to specify card values
"""

import json
import random

from data import Data

class Card(object):
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

    def __str__(self):
        return "Name %s, cost %s, attack %s, money %s" % \
                (self.name, self.cost, self.attack, self.money)

class Pile(object):
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

    def add(self, card):
        """
        Place a card on top of the pile
        """
        self.cards.append(card)

    def take(self, card):
        """
        Removes a specific card from the pile
        """
        self.cards.remove(card)

    def draw(self):
        """
        Remove a card from the top of pile
        """
        return self.cards.pop()

    def merge_piles(self, main_pile):
        """
        Take the pile and shuffle it into another pile
        """
        main_pile.cards.extend(self.cards)
        main_pile.shuffle()
        self.cards = []

    def display_cards(self):
        for card in self.cards:
            print "Name %s, cost %s, attack %s, money %s" % \
                (card.name, card.cost, card.attack, card.money)

class Player(object):

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

    def print_stats(self):
        print("Money: %s, Attack: %s" % (self.money, self.attack))

    def move_to_pile(self, card, target_pile):
        for pile in (self.drawpile, self.discard, self.hand):
            if card in pile:
                pile.take(card)
        target_pile.add(card)

    def make_deck(self):
        self.drawpile.build_player_pile(self.data['player'])

    def make_hand(self):
        while len(self.hand) < self.handsize:
            card = self.drawpile.draw()
            self.hand.add(card)

    def play_card(self, card):
        self.hand.take(card)
        self.money += card.money
        self.attack += card.attack
        self.discard.add(card)

    def play_all(self):
        for card in self.hand:
            self.play_card(card)

    def buy_card(self, card):
        self.money -= card.cost
        self.discard.add(card)

class Bot(Player):

    def __init__(self):
        Player.__init__(self)
        self.strategy = 'aggressive'

    def set_strat(self, strategy):
        if strategy == 'aggressive':
            bot_aggressive()

        elif strategy == 'acquisitive':
            bot_acquisitive()
                
    def bot_aggressive(self):
        pass


    def bot_acquisitive(self):
        pass
        

class Data(object):
    def __init__(self):
        self.data = []

    def load_cards(self, cardfile='../res/cards.json'):
        with open(cardfile) as card_file:
            self.data = json.load(card_file)

        return self.data

class Board(object):

    def __init__(self):
        self.data = Data().load_cards()
        self.central = Pile()
        self.active = Pile()
        self.maindeck = Pile()
        self.supplement = Pile()
        self.nmain = 36
        self.nsupp = 10
        self.ncen = 5

    def deal_decks(self):
        self.maindeck.create_pile(self.data['central'], self.ncen)
        self.supplement.create_pile(self.data['supplement'], self.nsupp)


    def draw_central(self):
        for c in range(self.ncen):
            card = self.maindeck.draw()
            self.central.add(card)


class Game(object):

    def __init__(self):
        self.data = Data().load_cards()
        self.human = Player()
        self.bot = Bot()
        self.board = Board()

    def initialise(self):
        self.board.deal_decks()
        self.human.make_deck()
        self.bot.make_deck()

    def newturn(self):
        self.human.make_hand()
        self.board.central.display_cards()
        self.human.hand.display_cards()

    def buyphase(self):
        pass

    def attack(self):
        pass

    def endturn(self):
        pass

    def botturn(self):
        pass

    def play(self):
        pass

def main():
    g = Game()
    g.initialise()
    while g.human.health > 0:
        g.newturn()
        print("\nPlayer Health: %s, Computer Health: %s \n" % (g.human.health, g.bot.health))
        print("\nChoose action: \nP = play all\n[0-n] = play card\nB = buy card\nA = attack\nE = end turn\n")
        action = raw_input("Enter action: ")
        if action == "P" or "p":
            g.human.play_all()
            pass

        if action.isdigit():
            pass

        if action == "B" or "b":
            pass

        if action == "A" or "a":
            pass

        if action == "E" or "e":
            pass

if __name__ == '__main__':
    main()
