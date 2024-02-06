import numpy as np

NUM_ROWS = 3
NUM_COLS = 3

class state:
    # initialize state
    def __init__(self):
        self.board = np.zeros((NUM_ROWS, NUM_COLS))
        self.sym_dic = {0: ' ', 1: 'X', -1: 'O'}
        self.play = True
        self.is_over = False

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

def play_game(game, is_X):
    # row, col = -1, -1
    if is_X:
        print('Input row and column for player X')
    else:
        print('Input row and column for player O')

    while True:
        row = int(input('Enter row: ')) - 1
        col = int(input('Enter col: ')) - 1
        
        if ((0<=row<=2) and (0<=col<=2)):
            if game.board[row, col] == 0:
                break
        
    if is_X:
        game.board[row, col] = 1
    else:
        game.board[row, col] = -1

    game.print_board()

    if (np.trace(game.board) == 3) or (np.trace(np.flipud(game.board)) == 3):
        print('X wins!')
        game.is_over = True

    if (np.trace(game.board) == -3) or (np.trace(np.flipud(game.board)) == -3):
        print('O wins!')
        game.is_over = True

    for i in range(NUM_ROWS):
        if (sum(game.board[i, :]) == 3) or (sum(game.board[:, i]) == 3):
            print('X wins!')
            game.is_over = True
            break
        elif (sum(game.board[i, :]) == -3) or (sum(game.board[:, i]) == -3):
            print('O wins!')
            game.is_over = True
            break

    if not game.is_over:
        if 0 not in game.board:
            print('Game tied!')
            game.is_over = True


game = state()

consent = 'y'
is_X = True

while game.play:
    play_game(game, is_X)
    is_X = not is_X
    if game.is_over:
        consent = input('Continue (y/n)?: ').lower()
        if consent not in ['y', 'yes']:
            game.play = False
        else:
            game.board_clear()
# game.print_board()