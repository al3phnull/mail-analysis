"""
Class to specify central line attributes
"""
from data import Data
from pile import Pile

class Board(object):
    """
    Initialises sentral line attributes and methods
    """
    def __init__(self):
        self.data = Data().load_data('res/cards.json')
        self.active = Pile()
        self.maindeck = Pile()
        self.supplement = Pile()
        self.nmain = 36
        self.nsupp = 10
        self.ncen = 5

    def deal_decks(self):
        """
        Calls create_pile from the Pile class
        to randomly distribute sets of cards
        from a list
        """
        self.maindeck.create_pile(self.data['central'], self.nmain)
        self.supplement.create_pile(self.data['supplement'], self.nsupp)


    def draw_active(self):
        """
        Populates the active area of the board
        from the top cards in the main deck
        """
        for index in range(self.ncen):
            card = self.maindeck.draw(index)
            self.active.put(card)

    def update_active(self):
        """
        Moves a card from the top of the
        main deck if the active area is
        not entirely populated and the
        main pile is non-empty. Otherwise
        it depletes
        """
        if len(self.active) < self.ncen:
            if len(self.maindeck) > 0:
                card = self.maindeck.draw()
                self.active.put(card)
            else:
                pass
