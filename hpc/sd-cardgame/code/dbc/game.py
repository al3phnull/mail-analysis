"""
Class to specify game functionality
"""

import sys
import os
import time

from data import *
from player import *
from board import *
from bot import *
from card import *
from pile import *


class Game(object):

    def __init__(self):
        self.text = Data().load_data('res/strings.json')
        self.data = Data().load_data('res/cards.json')
        self.human = Player()
        self.bot = Bot()
        self.board = Board()

    def intro_message(self):
        """
        Prints introductory message and allows the player
        to choose AI strategy
        """
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
        """
        Reinitialise options for a rematch
        """
        self.human = Player()
        self.bot = Bot()
        self.board = Board()
        self.board.deal_decks()
        self.human.make_deck()
        self.bot.make_deck()
        self.board.draw_active()

    def newturn(self):
        """
        Human assembles a new hand at the start of aturn
        """
        self.human.make_hand()

    def buyphase(self):
        """
        Buying phase. The player has three options to choose from:
        1. Buy a card by specifying its index
        2. Buy a Levy from the supplement pile
        3. Leave the shop
        """
        while self.human.money > 0:
            self.show_buy()
            option = raw_input(self.text['action'])
            if option == 'S' or option == 's':
                if len(self.board.supplement) > 0:
                    card = self.board.supplement[0]
                    if self.human.money >= card.cost:
                        card = self.board.supplement.draw()
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
                            continue
                    else:
                        print self.text['broke']
                else:
                    print self.text['toohigh']
                raw_input(self.text['continue'])
            else:
                print self.text['badopt']


    def attack(self, target, assailant):
        """
        Use attack values to inflict damage to
        the other player
        """
        target.health -= assailant.attack
        assailant.attack = 0

    def play(self):
        """
        Player chooses what to do during a turn:
        1. Play all cards
        2. Play a card specifying its index
        3. Buy cards from central active line
        4. Inflict damage to opponent's health
        5. End turn
        6. Leave the game
        """
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
                self.human.endturn()
                if self.bot.health > 0:
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
        """
        Bot AI functionality. Long. Needs cleaning in future
        """
        os.system('clear')
        print self.text['botgo']
        aggressive = self.strategy

        self.bot.make_hand()
        self.bot.play_all()

        self.text['botact']
        self.bot.active.display_cards()
        
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

            cardinds = range(len(self.board.active))
            for index in cardinds:
                cardinds.pop()
                
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
                    pass

                if len(self.board.supplement) > 0:
                    if self.bot.money >= self.board.supplement[0].cost:
                        self.bot.money -= self.board.supplement[0].cost
                        card = self.board.supplement.draw()
                        self.bot.hand.put(card)
                        print self.text['bought'] % (card)
            else:
                botbuy = False
            if self.bot.money == 0:
                botbuy = False


        raw_input(self.text['continue'])
        self.bot.endturn()


    def show_buy(self):
        """
        Displays the buying screen text
        """
        os.system('clear')
        print self.text['shopstr']
        print self.text['avail']
        self.board.active.display_cards()

        print self.text['wonga'] % self.human.money

        supps = len(self.board.supplement)
        print self.text['supprem'] % supps

        print self.text['buyopts']


    def show_move(self):
        """
        Displays the turn screen text
        """
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
        """
        Prompts the player for a rematch
        at the end of a game
        """
        re = raw_input(self.text['rematch'])
        if re == 'Y' or re == 'y':
            return True
        
        elif re == 'N' or re == 'n':
            return False

        else:
            self.text['badopt']

    

    def endgame(self):
        """
        Conditions for the end of a game
        """
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

