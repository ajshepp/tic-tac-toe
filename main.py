print("program started")

# This function makes a board and returns it
def create_board():
    board = []
    for x in range(0, 3):
        board.append(["?"] * 3)
    return board

# This function prints a board
def print_board(board): 
    print("=====")
    for row in board:
        print(" ".join(row))

# def place_x(board, row, col):
#     board[row][col] = "X"
# def place_o(board, row, col):
#     board[row][col] = "O"
def place_mark(board, row, col, mark):
    board[row][col] = mark


board1 = create_board()
print_board(board1)
place_mark(board1, 1, 2, "X")
place_mark(board1, 0, 2, "O")
print_board(board1)



