import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    cnt_X = sum(row.count(X) for row in board)
    cnt_O = sum(row.count(O) for row in board)
    return X if cnt_X <= cnt_O else O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action       
    new_board = deepcopy(board)
    new_board[i][j] = player(new_board)
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check horizontal
    for i in range(3):
        if len(board[i]) == 3 and board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
    
    # Check vertical
    for j in range(3):
        if all(len(row) > j for row in board) and board[0][j] == board[1][j] == board[2][j] != EMPTY:
            return board[0][j]
        
    # Check primary diagonal
    if len(board) == 3 and board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    
    # Check secondary diagonal
    if len(board) == 3 and board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[1][1]
    
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or not any(EMPTY in row for row in board)

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    verdict = winner(board)
    return 1 if verdict == X else -1 if verdict == O else 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    return max_value(board)[1] if player(board) == X else min_value(board)[1]

def max_value(board):
    if terminal(board):
        return utility(board), None
    
    value, best_move = -math.inf, None
    for action in actions(board):
        min_val = min_value(result(board, action))[0]
        if min_val > value:
            value, best_move = min_val, action
    return value, best_move

def min_value(board):
    if terminal(board):
        return utility(board), None
    
    value, best_move = math.inf, None
    for action in actions(board):
        max_val = max_value(result(board, action))[0]
        if max_val < value:
            value, best_move = max_val, action
    return value, best_move

