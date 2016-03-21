"""
Class to specify card values
"""

import sys
import os
import json
import random
import time

class Card(object):
    """
    Specifies card values
    """
    def __init__(self, card):
        self.text = Data().load_data('res/strings.json')
        self.name = str(card['name'])
        self.attack = card['attack']
        self.money = card['money']
        self.cost = card['cost']

    def __getitem__(self, key):
        return self.card[key]

    def __str__(self):
        return self.text['cvals'] % \
                (self.name, self.cost, self.attack, self.money)

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
            print self.text['empty']
        else:
            for index, card in enumerate(self.cards):
                print self.text['cvals1'] % \
                    (index, card.name, card.cost, card.attack, card.money)


class Player(object):

    def __init__(self):
        self.data = Data().load_data('res/cards.json')
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

    def move_to_pile(self, card, target_pile):
        for pile in (self.drawpile, self.discard, self.hand):
            if card in pile:
                pile.take(card)
        target_pile.put(card)

    def make_deck(self):
        self.drawpile.build_player_pile(self.data['player'])

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
        self.data = Data().load_data('res/cards.json')
        self.active = Pile()
        self.maindeck = Pile()
        self.supplement = Pile()
        self.nmain = 36
        self.nsupp = 10
        self.ncen = 5
        self.strategy = 0

    def deal_decks(self):
        self.maindeck.create_pile(self.data['central'], self.nmain)
        self.supplement.create_pile(self.data['supplement'], self.nsupp)


    def draw_active(self):
        for c in range(self.ncen):
            card = self.maindeck.draw()
            self.active.put(card)

    def update_active(self):
        if len(self.active) < self.ncen:
            if len(self.maindeck) > 0:
               card = self.maindeck.draw()
               self.active.put(card)
            else:
                pass


class Game(object):

    def __init__(self):
        self.text = Data().load_data('res/strings.json')
        self.data = Data().load_data('res/cards.json')
        self.human = Player()
        self.bot = Bot()
        self.board = Board()

    def intro_message(self):
        os.system('clear')
        print self.text['intro']
        while True:
            self.strategy = raw_input(self.text['strat'])
            if self.strategy == 'a' or self.strategy == 'A':
                print self.text['aggro']
                break
            
            if self.strategy == 'c' or self.strategy == 'C':
                print self.text['shekel']
                break

            else:
                print self.text['badopt']

        raw_input(self.text['continue'])

    def initialise(self):
        self.human = Player()
        self.bot = Bot()
        self.board = Board()
        self.board.deal_decks()
        self.human.make_deck()
        self.bot.make_deck()
        self.board.draw_active()

    def newturn(self):
        self.human.make_hand()

    def buyphase(self):
        while self.human.money > 0:
            self.show_buy()
            option = raw_input(self.text['action'])
            if option == 'S' or option == 's':
                if len(self.board.supplement) > 0:
                    card = self.board.supplement.draw(0)
                    if self.human.money >= card.cost:
                        self.human.discard.put(card)
                        self.human.money -= card.cost
                        print self.text['bought'] % (card)

                    else:
                        print self.text['broke']
                else:
                    print self.text['nosupp']

                raw_input(self.text['continue'])
                self.board.update_active()

            elif option == 'E' or option == 'e':
                raw_input(self.text['continue'])
                break

            elif option.isdigit():
                index = int(option)
                if index < len(self.board.active):
                    card = self.board.active[index]
                    if self.human.money >= card.cost:
                        self.board.active.draw(index)
                        self.human.discard.put(card)
                        self.human.money -= card.cost
                        print self.text['bought'] % (card)
                        if len(self.board.maindeck) > 0:
                            newcard = self.board.maindeck.draw()
                            self.board.active.put(newcard)
                        else:
                            print self.text['nocards']
                            contine
                    else:
                        print self.text['broke']
                else:
                    print self.text['toohigh']
                raw_input(self.text['continue'])
            else:
                print self.text['badopt']


    def attack(self, target, assailant):
        target.health -= assailant.attack
        assailant.attack = 0

    def endturn(self, player):
        if len(player.active) > 0:
            player.move_to_discard(player.active)

        if len(player.hand) > 0:
            player.move_to_discard(player.hand)

        player.discard.merge_piles(player.drawpile)

    def play(self):
        self.newturn()
        while True:
            self.show_move()
            action = raw_input(self.text['action'])
            if action == 'P' or action == 'p':
                if len(self.human.hand) > 0:
                    self.human.play_all()
                else:
                    print self.text['nocards']
                self.show_move()

            elif action.isdigit():
                index = int(action)
                if index < len(self.human.hand):
                    self.human.play_card(index)
                    self.show_move()
                else:
                    print self.text['toohigh']
                    raw_input(self.text['continue'])

            elif action == 'B' or action == 'b':
                self.buyphase()

            elif action == 'A' or action == 'a':
                self.attack(self.bot, self.human)
                self.show_move()

            elif action == 'E' or action == 'e':
                self.endturn(self.human)
                self.botturn()
                break

            elif action == 'Q' or action == 'q':
                quit = raw_input(self.text['confirm'])
                if quit == 'Y' or quit == 'y':
                    sys.exit(self.text['giveup'])
                elif quit == 'N' or quit == 'n':
                    continue

            else:
                print self.text['badopt']

    def botturn(self):
        os.system('clear')
        print self.text['botgo']
        aggressive = self.strategy

        self.bot.make_hand()
        self.bot.play_all()
        
        print self.text['botst'] % (self.bot.money, self.bot.attack)
        time.sleep(2)

        if self.bot.attack > 0:
            print self.text['botatk'] % (self.bot.attack)
            self.attack(self.human, self.bot)
        
        print self.text['botbuy']
        
        time.sleep(2)
        botbuy = True
        while botbuy:
            templist = []

            if len(self.board.supplement) > 0:
                if self.board.supplement[0].cost <= self.bot.money:
                    templist.append(("s", self.board.supplement[0]))

            for index in range(self.board.ncen):
                if self.board.active[index].cost <= self.bot.money:
                    templist.append((index, self.board.active[index]))
                
                if len(templist) > 0:
                    maxindex = 0
                    for index in range(len(templist)):
                        if templist[index][1].cost > templist[maxindex][1].cost:
                            maxindex = index

                        if templist[index][1].cost == templist[maxindex][1].cost:
                            if aggressive:
                                if templist[index][1].attack > templist[maxindex][1].attack:
                                    maxindex = index
                            else:
                                if templist[index][1].attack > templist[maxindex][1].money:
                                    maxindex = index

                    source = templist[maxindex][0]
                    if source in range(self.board.ncen):
                        if self.bot.money >= self.board.active[int(source)].cost:
                            self.bot.money -= self.board.active[int(source)].cost
                            card = self.board.active.draw(int(source))
                            print self.text['bought'] % (card)
                            self.bot.hand.put(card)
                            self.board.update_active()
                    else:
                        pass
                else:
                    if money >= self.board.supplement[0].cost:
                        money -= self.board.supplement[0].cost
                        card = self.board.supplement.draw()
                        self.bot.hand.put(card)
                        print self.text['bought'] % (card)
            else:
                botbuy = False
            if self.bot.money == 0:
                botbuy = False


        raw_input(self.text['continue'])
        self.endturn(self.bot)


    def show_buy(self):
        os.system('clear')
        print self.text['avail']
        self.board.active.display_cards()

        print self.text['wonga'] % self.human.money

        print self.text['buyopts']


    def show_move(self):
        os.system('clear')
        print self.text['health'] % (self.human.health, self.bot.health)

        print self.text['active']
        self.human.active.display_cards()

        print self.text['hand']
        self.human.hand.display_cards()

        print self.text['stats']
        self.human.show_stats()

        print self.text['gopts']


    def rematch_prompt(self):
        re = raw_input(self.text['rematch'])
        if re == 'Y' or re == 'y':
            return True
        
        elif re == 'N' or re == 'n':
            return False

        else:
            self.text['badopt']

    

    def endgame(self):
        game = True
        while game:
            self.play()
            if self.human.health <= 0:
                print self.text['botwin']
                game = self.rematch_prompt()
                self.initialise()

            elif self.bot.health <= 0:
                print self.text['win']
                game = self.rematch_prompt()
                self.initialise()

            elif len(self.board.active) == 0:
                print self.text['nocend']

                if self.human.health > self.bot.health:
                    print self.text['win']
                    game = self.rematch_prompt()
                    self.initialise()

                elif self.bot.health > self.human.health:
                    print self.text['botwin']
                    game = self.rematch_prompt()
                    self.initialise()



def main():
    g = Game()
    g.intro_message()
    g.initialise()
    g.endgame()

if __name__ == '__main__':
    main()
