"""
Class to initialise and execute the game
"""

from game import Game

def main():
    """
    Launches the main game procedure
    """
    g = Game()
    g.intro_message()
    g.initialise()
    g.endgame()

if __name__ == '__main__':
    main()
