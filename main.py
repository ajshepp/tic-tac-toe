print("program started")

# This function makes a board and returns it
def create_board():
    board = []
    for x in range(0, 3):
        board.append(["?"] * 3)
    return board

# This function prints a board
def print_board(board): 
    print()
    print("----")
    print()
    for row in board:
        print(" ".join(row))

def is_valid(board, row, col):
    if board[row][col] == "?":
        return True
    else:
        print()
        print("Invalid entry")
        print()
        return False


def place_mark(board, row, col, player):
    board[row][col] = player

    
board1 = create_board()
player = "X"

while True:
    row = int(input("P" + player + " set row: "))
    col = int(input("P" + player + " set column: "))

    if is_valid(board1, row, col) == True:
        place_mark(board1, row, col, player)
        print_board(board1)

        # Player switch
        if player == "X":
            player = "O"
        elif player == "O":
            player = "X"
