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


def get_distance(square1: (int, int), square2: (int, int), direction: str):
    """
    Calculates the distance between two squares (e.g. distance of length '1' between G7 and G8, distance of length
    '2' between B1 and D3)
    :param square1: First square
    :param square2: Second square
    :param direction: Either 'S' for straight direction or 'D' for diagonal direction
    :return: distance between the two squares as an int
    """

    r1, c1 = square1
    r2, c2 = square2

    # Calculate length between two squares in a straight direction, one coordinate will stay the same, whilst the
    # other will change, that changing coord difference is the distance
    if direction == "S":
        return abs((r1 - r2) + (c1 - c2))
    # For diagonal direction, both coordinates will change by the same magnitude, and that magnitude change is the
    # distance
    elif direction == "D":
        return (abs(r1 - r2) + abs(c1 - c2)) / 2


def player_from_square(square: (int, int), board_state: dict):
    """
    Based on the square with a piece given, determine what player it belongs to (Only use when square has a piece)
    :param square: The square where the piece is on
    :param board_state: The state of the board
    :return: The player for whom the piece on the input square belongs to
    """
    piece = board_state[square]
    player = piece[0]

    return player

