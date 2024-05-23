"""
Author: William Chio
Created: 22/05/24

Handles all operations that relate to board operations. Responsible for all manipulations and creation of board states
as dicts.

Board states are dictionaries where each item has a key that is the position on the board as a 2-int tuple and the
value as a string denoting the chess piece:
e.g. (0, 1): "BR" --> Black Rook at B8

Board states contain all pieces which are 'alive' from both white and black
"""


def initialise_board():
    """
    Creates an initial starting board state dictionary. Starting board is always the same, so create pieces at locations
    via looping through each row (0, 1, 6, 7) and popping the chars for pieces paired with coords on board
    8 |BR|Bk|BB|BK|BQ|BB|Bk|BR|
    7 |BP|BP|BP|BP|BP|BP|BP|BP|
    6 |  |  |  |  |  |  |  |  |
    5 |  |  |  |  |  |  |  |  |
    4 |  |  |  |  |  |  |  |  |
    3 |  |  |  |  |  |  |  |  |
    2 |WP|WP|WP|WP|WP|WP|WP|WP|
    1 |WR|Wk|WB|WK|WQ|WB|Wk|WR|
       A  B  C  D  E  F  G  H
    :return: Board state with starting piece positions
    """
    board_state = {}
    pieces = list("RkBQKBkRPPPPPPPPPPPPPPPPRkBQKBkR")  # Order of piece creation from left to right going downwards
    colours = list("WWBB")  # colours, 2sets of black and white
    rows = [0, 1, 6, 7]  # rows occupied by pieces
    for row in rows:
        colour = colours.pop()
        for col in range(8):
            board_state[(row, col)] = colour + pieces.pop()
    return board_state
