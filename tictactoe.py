"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    counter_x = 0
    counter_o = 0
    for row in board:
        for col in row:
            if col == X:
                counter_x += 1
            elif col == O:
                counter_o += 1
           
    if counter_x > counter_o:
            return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_actions = set()

    for rowIdx in range(0, len(board)):
        for colIdx in range(0, len(board)):
            if board[rowIdx][colIdx] == None:
                possible_actions.add((rowIdx,colIdx))

    return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    raise NotImplementedError

def max_value(board):

    raise NotImplementedError

def min_value(board):

    raise NotImplementedError