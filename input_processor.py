"""
Author: William Chio
Created: 24/05/24

Handles and verifies input from the player, this includes the square with the piece the player selects, and the move
that they make
"""

import visuals_and_txt as vis


def input_select_piece(player: str, board_state: dict):
    """
    Takes user input to determine the piece and square that they want to move. This piece returned is a valid square
    that has a piece belonging to the player
    :param player: The player's turn
    :param board_state:  The state of the board
    :return: The piece and coordinates they want to move
    """

    piece = None
    square = None
    # Keep asking for input until valid square is received
    while piece is None:

        raw_square = input(player + ": Choose a piece to move (Enter the square coordinates e.g. G7)\n").capitalize()
        square = validate_square(raw_square)

        if square:
            # Check there is a piece at the square
            try:
                piece = board_state[square]
            except KeyError:
                print("Invalid Piece: There is no Piece on that Square")
                piece = None
            else:
                # Check the piece belongs to the player
                if piece[0] != player[0]:
                    print("Invalid Piece: That Piece belongs to the other Player")
                    piece = None

    return piece, raw_square, square


def validate_square(square: str):
    """
    Takes a string and validates it is a valid square, then translates into coordinates for a board_state
    :param square: the input string from user
    :return: square translated into 2-int typle for a board_state. Return None if input is not valid or not a square on the board
    """

    # Check length is 2
    if len(square) != 2:
        print("Invalid Square: Input was not 2 characters")
        return None

    # check input is a letter followed by number (e.g. A7)
    if square[0].isalpha() and square[1].isnumeric():
        letter = str(square[0]).capitalize()
        number = int(square[1])
    else:
        print("Invalid Square: Was not a letter followed by a number")
        return None

    valid_letters = "ABCDEFGH"

    # Check input is composed first of a valid letter (A-H) followed by a number from (1-8)
    if letter not in valid_letters or not (0 < number < 9):
        print("Invalid Square: Square was not on the board")
        return None

    # Translate into coordinates for board_state to read
    letter = valid_letters.index(letter)
    number = 8 - number

    return number, letter
