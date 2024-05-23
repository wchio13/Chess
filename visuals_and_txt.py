"""
Author: William Chio
Created: 23/05/24

Handles all prints of the visual board and regular print prompts to the user
- Visual board refers to the visual representation of the board state printed to terminal
"""

# Board will look like this on start
# 8 |BR|Bk|BB|BK|BQ|BB|Bk|BR|
# 7 |BP|BP|BP|BP|BP|BP|BP|BP|
# 6 |  |  |  |  |  |  |  |  |
# 5 |  |  |  |  |  |  |  |  |
# 4 |  |  |  |  |  |  |  |  |
# 3 |  |  |  |  |  |  |  |  |
# 2 |WP|WP|WP|WP|WP|WP|WP|WP|
# 1 |WR|Wk|WB|WK|WQ|WB|Wk|WR|
#    A  B  C  D  E  F  G  H
#

import os

def display_board(board_state: dict):
    """Displays the visual state of the board given a board dictionary"""

    dynamic = create_dynamic_board_parts(board_state)

    # Now create formatting of the board along with dynamic portion where piece position is display

    # Add row of letters at the top
    print("   A  B  C  D  E  F  G  H  ")

    # Add row number bit to the left and right
    for i in range(8):
        print(str(8 - i) + " " + dynamic[i] + " " + str(8 - i))

    # Add row of letters at the bottom
    print("   A  B  C  D  E  F  G  H  ")


def to_pos(x: int):
    """Helper function that turns the column of the coordinate into the row_rep char index location in the string"""

    return x*3+1


def create_dynamic_board_parts(board: dict):
    """
    Generates the part of the board that houses the pieces

    :param board: A board state (dict)
    :return: The 8 rows of the visual board with pieces present
    """

    # Blank board parts of the overall board display
    board_rep = []
    for i in range(8):
        board_rep.append("|  |  |  |  |  |  |  |  |") # Empty rows

    # populate each row representation with the pieces
    for key in board.keys():
        piece = list(board[key])
        row, col = key[0], key[1]

        # replace the two EMPTY chars with the 'piece' char - "xx" -> "BR" where x = empty/blank char
        new_row_rep = list(board_rep[row])
        new_row_rep[to_pos(col)] = piece[0]
        new_row_rep[to_pos(col)+1] = piece[1]
        new_row_rep = "".join(new_row_rep)

        board_rep[row] = new_row_rep
    return board_rep


def message_ask_input(player: str):
    """
    Print out text prompting the user to input a square on the board in order to select a piece to move
    :param player: The player who's turn it is
    """
    print(player + ": Choose a piece to move (Enter the square coordinates e.g. G7)")


def clear_screen():
    """
    Clears the screen of text/visual
    """
    os.system('cls' if os.name == 'nt' else 'clear')



