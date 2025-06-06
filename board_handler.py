"""
Author: William Chio
Created: 22/05/24

Handles all operations that relate to board operations. Responsible for all manipulations and creation of board states
as dicts.

Board states are dictionaries where each item has a key that is the position on the board as a 2-int tuple and the
value as a string denoting the chess piece:
e.g. (0, 1): "BR" --> Black Rook at B8
The square A8 is the origin (0, 0)

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
    pieces = list("RNBKQBNRPPPPPPPPPPPPPPPPRNBKQBNR")  # Order of piece creation from left to right going downwards
    colours = list("WWBB")  # colours, 2sets of black and white
    rows = [0, 1, 6, 7]  # rows occupied by pieces
    for row in rows:
        colour = colours.pop()
        for col in range(8):
            board_state[(row, col)] = colour + pieces.pop()
    return board_state


def perform_move(board_state: dict, from_move: (int, int), to_move: (int, int)):
    """
    Given a board state, this will move whatever piece is on the square 'from_move' to the square 'to_move'.
    If there is an existing piece on the square 'to_move', the piece is 'captured'. It is assumed both squares are
    validated beforehand.
    :param board_state: The state of the board
    :param from_move: The square where the selected piece is originally located
    :param to_move: The square where the selected piece is moved to
    :return: New board_state with the move performed
    """
    piece = board_state[from_move]
    board_state.pop(from_move)
    board_state[to_move] = piece

    return board_state


def simulate_move(board_state: dict, square: (int, int), move: (int,int)):
    """
    Create a copy of board state and perform a move on it
    :param board_state: The state of the board
    :param square: The square where the piece is on
    :param move: The square to move the piece to
    :return: a board state that is a copy of the current with the move performed
    """
    simulated_board_state = board_state.copy()  # make a copy of board
    simulated_board_state = perform_move(simulated_board_state, square, move)

    return simulated_board_state
