'''
   This is a build of different class Gameplayer class, Humanely class and the AI class.
'''

import math
import random


class gamePlayer:
    def __init__(self, let):
        self.letter = let


class HumanPlayer(gamePlayer):
    def __init__(self, let):
        super().__init__(let)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s move. Enter (0-9) to make a move: ')
            try:
                val = int(square)
                if val not in game.a_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val
