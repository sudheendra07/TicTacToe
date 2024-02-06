import numpy as np
import tkinter as tk

NUM_ROWS = 3
NUM_COLS = 3

class states:
    # initialize state
    def __init__(self):
        self.board = np.zeros((NUM_ROWS, NUM_COLS))
        self.sym_dic = {0: ' ', 1: 'X', -1: 'O'}
        self.play = True
        self.is_over = False
        self.is_X = True
        self.consent = True

    # helper function to print the board state
    def print_board(self):
        print('-------------')
        for i in range(NUM_ROWS):
            out = '| '
            for j in range(NUM_COLS):
                out += self.sym_dic[self.board[i, j]] + ' | '
            print(out)
            print('-------------')

    # to reset once the game is over
    def board_clear(self):
        self.board = np.zeros((NUM_ROWS, NUM_COLS))
        self.is_over = False

    # main function to play game
    def play_game(self):
        if self.is_X:
            print('Input row and column for player X')
        else:
            print('Input row and column for player O')

        while True:
            row = int(input('Enter row: ')) - 1
            col = int(input('Enter col: ')) - 1
            
            if ((0<=row<=2) and (0<=col<=2)):
                if self.board[row, col] == 0:
                    break
            
        if self.is_X:
            self.board[row, col] = 1
        else:
            self.board[row, col] = -1

        self.is_X = not self.is_X
        
        self.print_board()
        self.isWinner()

        if self.is_over:
            self.get_consent()

        if game.play:
            self.play_game()

    def isWinner(self):
        if (np.trace(self.board) == 3) or (np.trace(np.flipud(self.board)) == 3):
            print('X wins!')
            self.is_over = True

        if (np.trace(self.board) == -3) or (np.trace(np.flipud(self.board)) == -3):
            print('O wins!')
            self.is_over = True

        for i in range(NUM_ROWS):
            if (sum(self.board[i, :]) == 3) or (sum(self.board[:, i]) == 3):
                print('X wins!')
                self.is_over = True
                break
            elif (sum(self.board[i, :]) == -3) or (sum(self.board[:, i]) == -3):
                print('O wins!')
                self.is_over = True
                break

        if not self.is_over:
            if 0 not in self.board:
                print('Game tied!')
                self.is_over = True

    def get_consent(self):
        cons = input('Continue (y/n)?: ').lower()
        if cons not in ['y', 'yes']:
            self.play = False
        else:
            self.board_clear()


if __name__ == "__main__":
    game = states()
    game.play_game()