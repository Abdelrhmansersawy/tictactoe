"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

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
    cnt_O = 0
    cnt_X = 0
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == X:
                cnt_X += 1
            elif board[i][j] == O:
                cnt_O += 1
    if cnt_X <= cnt_O:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == EMPTY:
                moves.add((i,j))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i,j  = action       
    new_board = deepcopy(board)
    new_board[i][j] = player(new_board)
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    state = None # game still in progress
    
    # Check horzontial 
    for i in range(0 , 3):
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
    
    # Check vertical
    for j in range(0 , 3):
        if board[0][j] == board[1][j] == board[2][j]:
            return board[0][j]
        
    # Check primary diagonal
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    
    # Check secandary diagonal
    if board[0][2] == board[1][1] == board[2][0]:
        return board[1][1]   
    
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None: 
        return True
    empty_cell = 0
    for i in range(0,3):
        for j in range(0,3):
            empty_cell += board[i][j] == EMPTY
    return empty_cell == 0

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    verdict = winner(board)
    if verdict == X:
        return 1
    elif verdict == O:
        return -1
    else:
        return 0



memo = {}
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    if player(board) == O:
        move = min_value(board)[1]
    else:
        move = max_value(board)[1]
    return move

def max_value(board):
    if terminal(board):
        return [utility(board), None]
    
    if board in memo.values():
        return memo[board]

    v = -1
    best_move = None
    for action in actions(board):
        hypothetical_value = min_value(result(board, action))[0]
        if hypothetical_value > v:
            v = hypothetical_value
            best_move = action
    return [v, best_move]


def min_value(board):
    if terminal(board):
        return [utility(board), None]
    
    if board in memo.values():
        return memo[board]

    v = 1
    best_move = None
    for action in actions(board):
        hypothetical_value = max_value(result(board, action))[0]
        if hypothetical_value < v:
            v = hypothetical_value
            best_move = action
    return [v, best_move]
