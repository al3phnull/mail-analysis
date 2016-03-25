"""
Class to specify computer player functions
WIP: Would be used for cleaning up bot AI
"""

from player import Player


class Bot(Player):
    """
    Specifies AI attributes and methods
    """
    def __init__(self):
        Player.__init__(self)
        self.strategy = 'aggressive'

    def set_strat(self, strategy):
        """
        Sets the AI's strategy
        """
        if strategy == 'aggressive':
            self.bot_aggressive()

        elif strategy == 'covetous':
            self.bot_covetous()

    def bot_aggressive(self):
        """
        Utilise an aggressive strategy
        """
        pass

    def bot_covetous(self):
        """
        Utilise a covetous strategy
        """
        pass


