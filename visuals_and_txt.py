# Author: William Chio
# Created: 23/05/24
#
# Handles all visual "UI" prints and normal prints to user to the terminal

# Displays the visual state of the board given a dictionary
def display_board(board: dict):
    dynamic = create_dynamic_board_parts(board)


# Helper function that turns the column of the coordinate into the row_rep char index location in the string
def to_pos(x: int):
    return x*3


def create_dynamic_board_parts(board: dict):
    # Blank board parts of the overall board display
    board_rep = []
    for i in range(8):
        board_rep.append("  |  |  |  |  |  |  |  ") # Empty rows

    # populate each row representation with the piece at the location
    for key in board.keys():
        piece = list(board[key])
        row, col = key[0], key[1]

        # replace the two EMPTY chars with the 'piece' char - "xx" -> "BR" where x = empty/blank char
        new_row_rep = list(board_rep[row])
        new_row_rep[to_pos(col)] = piece[0]
        new_row_rep[to_pos(col)+1] = piece[1]
        new_row_rep = "".join(new_row_rep)

        board_rep[row] = new_row_rep

