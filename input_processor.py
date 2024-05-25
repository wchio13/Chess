"""
Author: William Chio
Created: 24/05/24

Handles and verifies input from the player, this includes the square with the piece the player selects, and the move
that they make
"""
from piece_moves import determine_valid_moves
from visuals_and_txt import message_piece_selection


def input_select_piece(player: str, board_state: dict):
    """
    Takes user input to determine the piece and square that they want to move. This piece returned is a valid square
    that has a piece belonging to the player
    :param player: The player's turn
    :param board_state:  The state of the board
    :return: The square as it is in board_state and a list of the pieces valid moves
    """

    piece = None
    square = None
    # Keep asking for input until valid square is received
    while piece is None:

        raw_square = input(player + ": Choose a piece to move (Enter the square coordinates e.g. G7)\n").capitalize()
        square = validate_input_square(raw_square)

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
                else:
                    # Now determine the moves the piece can make, reject input if piece has no valid moves
                    valid_moves = determine_valid_moves(square, board_state)
                    if not valid_moves:
                        print("Invalid Piece: That Piece has no possible moves")
                        piece = None

    message_piece_selection(player, piece, raw_square)
    return square, valid_moves


def input_move_to(player: str, board_state: dict, from_square: (int, int)):
    """
    Takes user input to determine where to move their selected piece towards.
    :param from_square: The square where the piece to be moved in
    :param player: The player's turn
    :param board_state:  The state of the board
    :return: Coordinates the player wants to move to
    """


def validate_input_square(square: str):
    """
    Takes a string input from user and validates it is a valid square, then translates into coordinates for a board_state
    :param square: the input string from user ("A6")
    :return: square translated into 2-int tuple for a board_state. Return None if input is not valid or not a square on the board
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


