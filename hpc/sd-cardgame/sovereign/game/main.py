"""
Class to specify card values
"""
from game import *
import logging

def main():
    g = Game()
    g.deal_decks()
    g.play()

if __name__ == '__main__':
    main()
