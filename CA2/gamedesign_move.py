import math
import time
from CA2.gamePlayer_AI import HumanPlayer, AI

'''
Created a class AI_Tic which is then initialise with a board and current winner that is set to none.
On m_board i'm returning a board in length of 9 including space. In p_board i'm going through the row and i'm 
 printing the row, on every turn of each players. 
'''
class AI_Tic():
    def __init__(self):
        self.board = self.m_board()
        self.current_winner = None

    @staticmethod
    def m_board():
        return [' ' for _ in range(9)]

    def p_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
            print('-------------')
    '''
    In make_move is making a move on the board. taking in a square, representing the space the player 
    want to play which should be a number from 0-8 and the let value is could be X or 0. I check if the space is empty
    and if true, i assign a let to that square. Then i check if it's the winner, if it's i return winner 
    to current player.
'''

    # @staticmethod
    # def pd_nums():
    #     # 0 | 1 | 2
    #     number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
    #     for row in number_board:
    #         print('| ' + ' | '.join(row) + ' |')
    #         print('-------------')

    def make_move(self, square, let):
        if self.board[square] == ' ':
            self.board[square] = let
            if self.winner(square, let):
                self.current_winner = let
            return True
        return False
    '''
    In the winner function i check if the previous move was a win or not, i take in the square and 
    the let and i'm getting the row in the board, and if every let is the same let on the board then i return true.
    Then i check the column is the let in every column is same i return true. becouse the check is done along the square
    the diagonal only applies if it's a diagonal and the square is even. if the square is even then the diagonal applies. 
    so i check the diagonal to see if the let is the same and return true. 
    '''

    def winner(self, square, letter):
        # check the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind * 3:(row_ind + 1) * 3]
        # print('row', row)
        if all([s == letter for s in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        # print('col', column)
        if all([s == letter for s in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                return True
        return False

    '''
    The e_squares let me know the number of empty square on the board, n_e_squares count the number of 
    empty square on the board and a_move get the actual number of the empty space.
    
    '''

    def e_squares(self):
        return ' ' in self.board

    def n_e_squares(self):
        return self.board.count(' ')

    def a_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]

    '''
   The play function has an X and O player, with print game. The X player start the game if the game is empty. 
   if the player is O, we get the player next move else we get the X player next move. We make a move and check to see 
   if there is a current winner, if there is a current winner we print the lett win else we print it's a draw game.
   
   '''


def play(game, x_player, o_player, print_game=True):
    # if print_game:
    #     game.pd_nums()

    lett = 'X'
    while game.e_squares():
        if lett == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, lett):

            if print_game:
                print(lett + ' makes a move to square {}'.format(square))
                game.p_board()
                print('')

            if game.current_winner:
                if print_game:
                    print("Congratulation" + lett + ' wins!')
                return lett
            lett = 'O' if lett == 'X' else 'X'  # switches player

        time.sleep(.5)

    if print_game:
        print('Draw Game!')