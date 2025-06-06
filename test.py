import copy

X = "X"
O = "O"

board = [["X", "X", "O"],
         ["O", None, "X"],
         ["X", "X", "O"]]


def player(board):
    counter_x = 0
    counter_o = 0
    for row in board:
        for col in row:
            if col == "X":
                counter_x += 1
            elif col == "O":
                counter_o += 1
            
    if counter_x > counter_o:
        return "O", counter_o, counter_x
    else:
        return "X", counter_o, counter_x
print(player(board))

def result(board, action):
    copy_board = copy.deepcopy(board)

    try:
        result_board = copy_board[action[0]][action[1]]
        print(result_board)
    except Exception as E:
        print("Action not valid")
action = [0,3]
print(action[0], action[1])
result(board, action)

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
        # Checking vertical board
    if board[0][0] == board[1][0] == board[2][0] :
        return board[0][0]
    elif board[0][1] == board[1][1] == board[2][1] :
        return board[0][1]
    elif board[0][2] == board[1][2] == board[2][2] :
        return board[0][2]

    # Checking horizontal board
    elif board[0][0] == board[0][1] == board[0][2]:
        return board[0][0]
    elif board[1][0] == board[1][1] == board[1][2]:
        return board[0][0]
    elif board[2][0] == board[2][1] == board[2][2]:
        return board[0][0]
    
    # Checking Diagonal 
    elif board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0]:
        return board[0][0]
    else:
        return None

print(winner(board))

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


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    possible_actions = actions(board)
    empty_set = set()

    if winner(board) != None:
        return True
    elif winner(board) == None and (possible_actions == empty_set):
        return True
    else:
        return False

def utility(board):

    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0

print(actions(board))
print(terminal(board))
print(utility(board))