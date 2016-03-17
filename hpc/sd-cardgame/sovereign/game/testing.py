from card import *


g = Game()
cen, sup, pla, bot = g.deal_decks()
print("central deck size: %s" % len(cen))
print("supplement deck size: %s" % len(sup))
print("player deck size: %s" % len(pla))
print("bot deck size: %s" % len(bot))

drawn = pla.draw()
print drawn.name
