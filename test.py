board = [["X", None, None],
         ["O", "X", None],
         [None, "O", None]]

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

# for row in range(0, len(board)):
#     print(board[row])
#     for col in range(0, len(board)):
#         #print(board[row][col])
#         pass