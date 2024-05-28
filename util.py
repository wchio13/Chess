"""
Author: William Chio
Created: 26/05/24

Contains all small helper functions
"""


def is_opponent_piece(player: str, piece: str):
    """
    Helper function that gives the opposite colour of the player given.
    :param piece: Piece to check
    :param player: Player colour as "W" or "B"
    :return: True or False if the piece belongs to opponent
    """

    return player != piece[0]


def get_direction(player: str):
    """
    Helper function that gives the direction a pawn should move based on if they are white or black
    :param player: Colour of player
    :return: +1 or -1 indicating going up rows or doing down depending on colour
    """
    if player == "W":
        return -1
    else:
        return 1


def is_valid_square(square: (int, int)):
    """
    Helper function that checks given square coordinates (in board_state form -> (0, 1)) are valid
    :param square: Board_state coordinates
    :return: True or False if valid
    """
    if (-1 < square[0] < 8) and (-1 < square[1] < 8):
        return True
    else:
        return False


def has_piece(square: (int, int), board_state: dict):
    """
    Determines the status of a valid square
    :param board_state: State of the board
    :param square: The square to check
    :return: "W" if White piece, "B" if Black piece or None if the square has no piece
    """
    # Check there is a piece at the square
    try:
        board_state[square]
    except KeyError:
        return False
    else:
        return True


def next_player_turn(player: str):
    """
    Helper function to cycle the current players turn between White and Black
    :param player: The current player's turn
    :return: The next player's turn
    """
    if player == "White":
        return "Black"
    else:
        return "White"
