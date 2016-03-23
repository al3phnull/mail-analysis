"""
Testing the program.
"""

import unittest

from dbc.game import *


class TestGame(unittest.TestCase):

    @unittest.skip("It prints text.")
    def test_intro_message(self):
        game = Game()
        game.intro_message()

    @unittest.skip("It prints text.")
    def test_show_buy(self):
        game = Game()
        game.show_buy()

    @unittest.skip("It prints text.")
    def test_show_move(self):
        game = Game()
        game.show_move()

    @unittest.skip("It prints text.")
    def test_rematch_prompt(self):
        game = Game()
        game.rematch_prompt()

    def test_initialise(self):
        game = Game()
        game.initialise()
        self.assertEquals(len(game.board.maindeck), game.board.nmain - game.human.handsize)
        self.assertEquals(len(game.human.drawpile), 10)
        self.assertEquals(len(game.bot.drawpile), 10)
        self.assertEquals(len(game.board.active), game.board.ncen)

    def test_newturn(self):
        game = Game()
        game.initialise()
        game.newturn()
        self.assertEquals(len(game.human.hand), game.human.handsize)

    @unittest.skip("no output, skipping")
    def test_buyphase(self):
        game = Game()
        game.buyphase()

    @unittest.skip("no output, skipping")
    def test_botturn(self):
        game = Game()
        game.botturn()

    @unittest.skip("no output, skipping")
    def test_play(self):
        game = Game()
        game.play()

    @unittest.skip("no output, skipping")
    def test_endgame(self):
        game = Game()
        game.endgame()

    def test_attack(self):
        game = Game()
        game.initialise()
        game.newturn()
        game.human.play_all()
        temp_health = game.bot.health
        atk = game.human.attack
        game.attack(game.bot, game.human)
        self.assertEquals(game.bot.health, temp_health - atk)
