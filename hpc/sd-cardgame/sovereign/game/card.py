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
        if len(self.cards) == 0:
            print(self.text['empty'])
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
        for index in range(len(self.hand)):
            self.play_card(0)

    def buy_card(self, card):
        self.money -= card.cost
        self.discard.put(card)

    def move_to_discard(self, pile):
        for x in range(len(pile)):
            card = pile.draw()
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
        self.active = Pile()
        self.maindeck = Pile()
        self.supplement = Pile()
        self.nmain = 36
        self.nsupp = 10
        self.ncen = 5

    def deal_decks(self):
        self.maindeck.create_pile(self.data['central'], self.nmain)
        self.supplement.create_pile(self.data['supplement'], self.nsupp)


    def draw_active(self):
        for c in range(self.ncen):
            card = self.maindeck.draw()
            self.active.put(card)

    def update_active(self):
        if len(self.active) < self.ncen:
            card = self.maindeck.draw()
            self.active.put(card)
        else:
            pass

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
        self.board.draw_active()

    def newturn(self):
        self.human.discard.merge_piles(self.human.drawpile)
        self.human.drawpile.shuffle()
        self.human.make_hand()

    def buyphase(self):
        while self.human.money > 0:
            self.show_buy()
            option = raw_input(self.text['action'])
            if (option == 'S' or option == 's'):
                if (len(self.board.supplement) > 0):
                    card = self.board.supplement[0]
                    if (self.human.money >= card.cost):
                        self.board.supplement.draw(card)
                        self.human.discard.put(card)
                        self.human.money -= card.cost
                        print(self.text['bought'] % (card))
    
                    else:
                        print(self.text['broke'])
                else:
                    print(self.text['nosupp'])

                raw_input(self.text['continue'])
                self.board.update_active()

                        
            elif (option == 'E' or option == 'e'):
                raw_input(self.text['continue'])
                break

            elif (option.isdigit()):
                index = int(option)
                if index < len(self.board.active):
                    card = self.board.active[index]
                    if self.human.money >= card.cost:
                        self.board.active.draw(index)
                        self.human.discard.put(card)
                        self.human.money -= card.cost
                        print(self.text['bought'] % (card))
                        if (len(self.board.maindeck) > 0):
                            newcard = self.board.maindeck.draw()
                            self.board.active.put(newcard)
                    else:
                        print(self.text['broke'])
                else:
                    print(self.text['toohigh'])
                raw_input(self.text['continue'])
                self.board.update_active()
            else:
                print(self.text['badopt'])


    def attack(self):
        self.bot.health -= self.human.attack
        self.human.attack = 0

    def endturn(self):
        if (len(self.human.active) > 0):
            self.human.move_to_discard(self.human.active)

        if (len(self.human.hand) > 0):
            self.human.move_to_discard(self.human.hand)

        for x in range(0, self.human.handsize):
            if (len(self.human.drawpile) == 0):
                self.human.discard.merge_piles(self.human.drawpile)

    def play(self):
        self.newturn()
        while True:
            self.show_move()
            action = raw_input(self.text['action'])
            if (action == 'P' or action == 'p'):
                if (len(self.human.hand) > 0):
                    self.human.play_all()
                self.show_move()
    
            if (action.isdigit()):
                index = int(action)
                if (index < len(self.human.hand)):
                    self.human.play_card(index)
                    self.show_move()
                else:
                    print(self.text['toohigh']) 
                    raw_input(self.text['continue'])

            if (action == 'B' or action == 'b'):
                self.buyphase()
    
            if (action == 'A' or action == 'a'):
                self.attack()
                self.show_move()

            if (action == 'E' or action == 'e'):
                self.endturn()
                break

            if (action == 'Q' or action == 'q'):
                sys.exit(self.text['giveup'])

            else:
                print(self.text['badopt'])
            pass

    def botturn(self):
        pass

    def show_buy(self):
        os.system('clear')
        print(self.text['avail'])
        self.board.active.display_cards()

        print(self.text['wonga'] % self.human.money)
        
        print(self.text['buyopts'])

    def show_move(self):
        os.system('clear')
        print(self.text['health'] % (self.human.health, self.bot.health))

        print(self.text['active'])
        self.human.active.display_cards()

        print(self.text['hand'])
        self.human.hand.display_cards()

        print(self.text['stats'])
        self.human.show_stats()

        print(self.text['gopts'])



def main():
    g = Game()
    g.intro_message()
    g.initialise()
    while True:
        g.play()

if __name__ == '__main__':
    main()
