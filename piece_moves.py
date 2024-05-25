"""
Author: William Chio
Created: 26/05/24

Handles the generation of moves that each chess piece can perform
"""

from util import get_direction, is_valid_square, get_opponent, get_colour


def determine_valid_moves(square: str, board_state: dict):
    """
    Determines the valid moves a selected piece can make
    :param square: Square with the player-selected piece
    :param board_state: The state of the board
    :return: A list of valid moves the selected piece can make. Will return an empty list if there is no valid moves
    """
    piece = board_state[square]
    piece_type = piece[1]  # Grab the piece type to determine movement rules
    moves = []

    # generate list of valid moves based on piece
    if piece_type == "P":
        moves = generate_pawn_moves(square, board_state)

    return moves


def generate_pawn_moves(square: str, board_state: dict):
    """
    Create a list of moves that are valid for a pawn piece at a given square with a given board state
    Pawn movement consists of three parts:
    1. Forward one square if nothing obstructing square (move1)
    2. Forward two squares if nothing obstructing and pawn has not been moved yet (move2)
    3. Diagonal forward left/right if opposing piece can be captured on those squares (move3)
    :param square: Square where the pawn is located
    :param board_state: State of the board
    :return: List of moves that a pawn can make from the square given a board state
    """
    valid_moves = []
    player = board_state[square][0]  # Grab first char of piece to get player colour
    direction = get_direction(player)

    row = square[0]
    col = square[1]

    # Forward one square if not obstructed (move1)
    move1 = (row + direction, col)
    if is_valid_square(move1) and move1 not in board_state.keys():
        valid_moves.append(move1)

    # Forward two squares if nothing obstructing and pawn has not been moved yet (move2)
    if (row == 1 and direction == 1) or (row == 6 and direction == -1):  # Determine pawn has not moved
        move2 = (row + direction * 2, col)

        if move1 in valid_moves and move2 not in board_state.keys():  # Check both squares in front of pawn are empty
            valid_moves.append(move2)

    # Diagonal move left/right if there is opposing piece on those squares (move3)
    move3 = [(row + direction, col + 1), (row + direction, col - 1)]
    for move in move3:
        if is_valid_square(move) and move in board_state.keys():  # Check there is a piece on the valid square
            piece_on_square = board_state[move]

            if get_colour(piece_on_square) == get_opponent(player):  # Check piece on square belongs to the opponent
                valid_moves.append(move)

    return valid_moves
