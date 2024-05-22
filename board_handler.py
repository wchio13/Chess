# Author: William Chio
# Created: 22/05/24
#
# Handles all operations that relate to board operations

# Creates the initial starting board dictionary. Starting board is always the same, so create pieces at locations via
# looping through each row (0, 1, 6, 7) and popping the chars for pieces paired with coords on board
# 8 |BR|Bk|BB|BK|BQ|BB|Bk|BR|
# 7 |BP|BP|BP|BP|BP|BP|BP|BP|
# 6 |  |  |  |  |  |  |  |  |
# 5 |  |  |  |  |  |  |  |  |
# 4 |  |  |  |  |  |  |  |  |
# 3 |  |  |  |  |  |  |  |  |
# 2 |WP|WP|WP|WP|WP|WP|WP|WP|
# 1 |WR|Wk|WB|WK|WQ|WB|Wk|WR|
#    A  B  C  D  E  F  G  H


def initialise_board():
    board = {}
    pieces = list("RkBQKBkRPPPPPPPPPPPPPPPPRkBQKBkR")    # Order of piece creation from left to right going downwards
    colours = list("WWBB")    # colours, 2sets of black and white
    rows = [0, 1, 6, 7]    # rows occupied by pieces
    for row in rows:
        colour = colours.pop()
        for col in range(8):
            board[(row, col)] = colour + pieces.pop()
    return board
