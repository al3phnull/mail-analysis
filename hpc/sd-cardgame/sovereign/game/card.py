import sys
import json
import random

CARDFILE = '../res/cards.json'

class Card:
    def __init__(self, card):
        self.name = card['name']
        self.attack = card['attack']
        self.money = card['money']
        self.cost = card['cost']


    def get_attack(self, card):
        return self.attack

    def get_money(self, card):
        return self.money


class Pile:
    def __init__(self):
        self.central = []


    def load_cards(self):
        with open(CARDFILE) as card_file:
            self.data = json.load(card_file)
        
        return data


    def read_cards(data, self):
        self.cardlist = []
        for card in data:
            self.cardlist.append(card)

        return cardlist


    def create_pile(cards, ncards, self):     
        self.pile = []
        for i in range(ncards):
            self.deck.append(random.choice(cards))
    
        return deck

    
    def shuffle(self):
        random.shuffle(self.cards)


class Player:
    def __init__(self):
        self.money = 0
        self.attack = 0
        self.health = 30
        self.hand = None
        self.deck = Pile() 
        self.active = None
        self.discard = None
        self.handsize = 5

    
    def add_card(self, card):
        self.hand.append(card)

    
    def make_hand(self):
        while len(hand) < handsize:
            add_card()


    def play_card(self, card):
        self.hand.pop(card)


    def play_all(self):
        while len(hand) > 0:
            play_card():



class Game:
    def __init__(self, game):
        self.game = game
        self.central = []
        self.discard = []
        self.deck = []
