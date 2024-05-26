"""
Author: William Chio
Created: 26/05/24

Handles the generation of moves that each chess piece can perform
"""

from util import get_direction, is_valid_square, is_opponent_piece, has_piece


def determine_valid_moves(square: (int, int), board_state: dict):
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
    elif piece_type == "K":
        moves = generate_king_moves(square, board_state)
    return moves


def generate_pawn_moves(square: (int, int), board_state: dict):
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

    row, col = square

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

            if is_opponent_piece(player, piece_on_square):  # Check piece on square belongs to the opponent
                valid_moves.append(move)

    return valid_moves


def generate_king_moves(square: (int, int), board_state: dict):
    """
    Create a list of moves that are valid for a King at a given square given a certain board state.
    King movement simply consists of one tile in all directions, being able to capture on each of these squares
    :param square: Square where the pawn is located
    :param board_state: State of the board
    :return: List of moves that a King can make from the square given a board state
    """
    row, col = square
    moves = []
    player = board_state[square][0]

    # Generate all 8 possible moves
    for i in range(-1, 2):
        for j in range(-1, 2):
            move = (row + i, col + j)
            valid = True
            if not is_valid_square(move):  # Check square is valid
                valid = False
            # Move not valid if square has a piece of same colour as player
            elif has_piece(move, board_state) and not is_opponent_piece(player, board_state[move]):
                valid = False

            if valid:
                moves.append(move)
    return moves
