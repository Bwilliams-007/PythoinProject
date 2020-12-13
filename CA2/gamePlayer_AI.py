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
