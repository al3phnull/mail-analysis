from card import *


g = Game()
g.board.deal_decks()
g.board.draw_central()
g.board.central.display_cards()

g.human.make_deck()
g.human.drawpile.shuffle()
g.human.make_hand()
