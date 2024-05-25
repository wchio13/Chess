"""
Author: William Chio
Created: 26/05/24

Contains all small helper functions
"""


def get_opponent(player: str):
    """
    Helper function that gives the opposite colour of the player given.
    :param player: Player colour as "W" or "B"
    :return: The opposite colour of the player "W" or "B"
    """
    if player == "W":
        return "B"
    else:
        return "W"


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


def get_colour(piece: str):
    """
    Determine the player who this piece belongs to
    :param piece: Piece to determine ownership
    :return: "W" if white or "B" if black
    """
    return piece[0]
