import copy
board = [["X", None, "X"],
         ["O", "X", "X"],
         [None, "O", "X"]]

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

possible_actions = set()

for rowIdx in range(0, len(board)):
    for colIdx in range(0, len(board)):
        if board[rowIdx][colIdx] == None:
            print((board[rowIdx][colIdx]))
            possible_actions.add((rowIdx,colIdx))

print(possible_actions)

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

    # Checking vertical board
    if board[0][0] == board[1][0] == board[2][0] :
        print(board[0][0])
    if board[0][1] == board[1][1] == board[2][1] :
        print(board[0][1])
    if board[0][2] == board[1][2] == board[2][2] :
        print(board[0][2])
    print("----")
    # Checking horizontal board
    if board[0][0] == board[0][1] == board[0][2]:
        print(board[0][0])
    if board[1][0] == board[1][1] == board[1][2]:
        print(board[0][0])
    if board[2][0] == board[2][1] == board[2][2]:
        print(board[0][0])
    # Checking Diagonal 
    print("--------")
    if board[0][0] == board[1][1] == board[2][2]:
        print(board[0][0])
    if board[0][2] == board[1][1] == board[2][0]:
        print(board[0][0])

winner(board)