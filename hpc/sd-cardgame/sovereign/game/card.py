"""
Class to specify card values
"""

import sys, os
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
        self.text = Data().load_data('../res/strings.json')

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

    def take(self, card):
        """
        Removes a specific card from the pile
        """
        return self.cards.remove(card)

    def draw(self, card=None):
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
        if len(self.cards) == 0:
            print "\nEmpty"
        else:
            for card in self.cards:
                print(self.text['cvals'] % \
                    (card.name, card.cost, card.attack, card.money))


class Player(object):

    def __init__(self):
        self.data = Data().load_data('../res/cards.json')
        self.money = 0
        self.attack = 0
        self.health = 30
        self.hand = Pile()
        self.active = Pile()
        self.discard = Pile()
        self.drawpile = Pile()
        self.handsize = 5

    def show_stats(self):
        print("Money: %s, Attack: %s" % (self.money, self.attack))

    def move_to_pile(self, card, target_pile):
        for pile in (self.drawpile, self.discard, self.hand):
            if card in pile:
                pile.take(card)
        target_pile.put(card)

    def make_deck(self):
        self.drawpile.build_player_pile(self.data['player'])

    def make_hand(self):
        while len(self.hand) < self.handsize:
            card = self.drawpile.draw()
            self.hand.put(card)

    def play_card(self, index):
        card = self.hand.draw(index)
        self.active.put(card)
        self.money += card.money
        self.attack += card.attack

    def play_all(self):
        for index in range(self.handsize):
            self.play_card(index)

    def buy_card(self, card):
        self.money -= card.cost
        self.discard.put(card)

    def move_to_discard(self):
        for card in self.active:
            self.active.take(card)
            self.discard.put(card)


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

    def load_data(self, textfile):
        with open(textfile) as in_file:
            self.data = json.load(in_file)

        return self.data

class Board(object):

    def __init__(self):
        self.data = Data().load_data('../res/cards.json')
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
            self.central.put(card)

    def update_central(self, index):
        if len(self.central) < self.ncen:
            card = self.central.draw(index)
            self.maindeck.draw()
            self.central.add

class Game(object):

    def __init__(self):
        self.text = Data().load_data('../res/strings.json')
        self.data = Data().load_data('../res/cards.json')
        self.human = Player()
        self.bot = Bot()
        self.board = Board()

    def intro_message(self):
        os.system('clear')
        print self.text['intro']
        raw_input(self.text['continue'])

    def initialise(self):
        self.board.deal_decks()
        self.human.make_deck()
        self.bot.make_deck()
        self.board.draw_central()

    def newturn(self):
        self.human.discard.merge_piles(self.human.drawpile)
        self.human.drawpile.shuffle()
        self.human.make_hand()

    def buyphase(self):
        while True:
            os.system('clear')
            print self.text['cards']
            self.board.central.display_cards()
            if (option == 'S' or option == 's'):
                pass

            elif (option == 'E' or option == 'e'):
                break

            elif (option.isdigit()):
                pass

    def attack(self):
        self.bot.health -= self.human.attack
        self.human.attack = 0

    def endturn(self):
        self.human.move_to_discard()

    def play(self):
        pass

    def botturn(self):
        pass

    def show_data(self):
        os.system('clear')
        print(self.text['line'])
        self.board.central.display_cards()

        print(self.text['hand'])
        self.human.hand.display_cards()

        print(self.text['stats'])
        self.human.show_stats()



def main():
    g = Game()
    g.intro_message()
    g.initialise()
    g.newturn()
    while True:
        g.show_data()
        print(g.text['health'] % (g.human.health, g.bot.health))
        print(g.text['gopts'])
        action = raw_input("Enter action: ")
        if (action == 'P' or action == 'p'):
            g.human.play_all()
            g.show_data()

        if (action.isdigit()):
            if (int(action) < len(g.human.hand)):
                g.human.play_card(int(action))
                g.show_data()
            else:
                print(g.text['toohigh']) 


        if (action == 'B' or action == 'b'):
            pass

        if (action == 'A' or action == 'a'):
            g.attack()
            g.show_data()

        if (action == 'E' or action == 'e'):
            g.endturn()
            g.botturn()

        if (action == 'Q' or action == 'q'):
            sys.exit(g.text['giveup'])
        else:
            print(g.text['badopt'])

if __name__ == '__main__':
    main()
