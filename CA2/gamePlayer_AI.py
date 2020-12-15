'''
   I have created a build for both Humanplayer class and the AI class. for the humanplayer everytime they play it take
   in their input and turn it into an int value and return it. for the AI thing are a little different, if it's an
   empty board it randomly chooses where to go otherwise it uses the minimax algorithm to assess the best choice
   that would produce a win or end up in a draw.
   The minimax function, i'm passing in a state that is the current
   state of the game and a player which represent the player that is playing next. max_payer would be self because
   the game assume all players are playing optimally and  opponent is the other player. first we check if the
   previous move is a winner if true return the heuristic value. if the opponent win i return the position none,
   which would change when it's passed back using recursion. the state.num is +1 for me and if other player -1 plus
   the number of empty square. otherwise if they are no more square left then we want to return a score of 0.
   then if the current player is = to the max player i want best score to be negative.infinity, each score should
   maximize else infinity each score should minimize.

   For every possible move in the next move, i would make a move and score the move by calling minimax. which would
   simulate every combination and get the best value depending on if we are minimizing or maximizing.
   After which all simulated steps are removed by making the board space again and if there was a winner on the
   simulation it's set to none and the position that was return as the best move would be set as the next possible move.
   If the player is the max-player and the return simulation score is the best score then it's return it has the best
    score else if not max-player and the score is less then the best score then score is the now best and return best.

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


class AI(gamePlayer):
    def __init__(self, let):
        super().__init__(let)

    def get_move(self, game):
        if len(game.a_moves()) == 9:
            square = random.choice(game.a_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter
        opponent = 'O' if player == 'X' else 'X'

        # first we want to check if the previous move is a winner
        if state.current_winner == opponent:
            return {'position': None,
                    'score': 1 * (state.n_e_squares() + 1) if opponent == max_player else -1 * (
                            state.n_e_squares() + 1)}
        elif not state.e_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  
        else:
            best = {'position': None, 'score': math.inf}  
        for possible_move in state.a_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, opponent)  

            # undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  

            if player == max_player:  # X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best
