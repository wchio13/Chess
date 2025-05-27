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

    # generate list of valid moves based on piece
    if piece_type == "P":
        return generate_pawn_moves(square, board_state)
    elif piece_type == "K":
        return generate_king_moves(square, board_state)
    elif piece_type == "B":
        return generate_bishop_moves(square, board_state)
    elif piece_type == "R":
        return generate_rook_moves(square, board_state)
    elif piece_type == "Q":
        return generate_queen_moves(square, board_state)
    elif piece_type == "N":
        return generate_knight_moves(square, board_state)

    print("This Piece is not even a chess piece what????????")
    return []


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
    :param square: Square where the King is located
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


def generate_bishop_moves(square: (int, int), board_state: dict):
    """
    Create a list of moves that are valid for a Bishop at a given square given a certain board state.
    Bishop movement consist of infinite tiles in all four diagonal directions (up-left, up-right, down-left, down-right)
    until the end of the board, unless:
    1. In the given direction there is a tile with a piece on it that belongs to the same player, all possible moves
    AFTER AND INCLUDING the tile with the piece are not valid moves
    2. In the given direction there is a tile with a piece on it that belongs to the opponent player, all possible moves
    AFTER the tile with the piece are not valid moves. The tile with the opponent piece is a valid move as the bishop
    can capture the piece.
    :param square: Square where the Bishop is located
    :param board_state: State of the board
    :return: List of moves that a Bishop can make from the square given a board state
    """
    row, col = square
    moves = []
    player = board_state[square][0]

    # 4 possible directions, up-left, up-right, down-left and down-right. Premise is to keep adding moves in a
    # direction until a square is met that is off the board or has a piece on it ^^^
    directions = [1, -1]
    for i in directions:
        for j in directions:

            for step in range(1, 9):  # Add moves in direction till a piece is met
                move = (row + i * step, col + j * step)
                if is_valid_square(move):  # Check square is on the board
                    if has_piece(move, board_state):

                        # Found enemy piece so add this square to moves and stop loop
                        if is_opponent_piece(player, board_state[move]):
                            moves.append(move)
                            break

                        # Found friendly piece so don't add this square and stop loop
                        else:
                            break
                    else:
                        moves.append(move)  # Empty square so add and continue loop
                else:
                    break  # Reach end of board so stop loop

    return moves


def generate_rook_moves(square: (int, int), board_state: dict):
    """
    Create a list of moves that are valid for a Rook at a given square given a certain board state.
    Rook movement consist of infinite tiles in all four straight directions (up, left, right, down) until the end of
    the board, unless:
    1. In the given direction there is a tile with a piece on it that belongs to the same player, all possible moves
    AFTER AND INCLUDING the tile with the piece are not valid moves
    2. In the given direction there is a tile with a piece on it that belongs to the opponent player, all possible moves
    AFTER the tile with the piece are not valid moves. The tile with the opponent piece is a valid move as the rook
    can capture the piece.
    :param square: Square where the Rook is located
    :param board_state: State of the board
    :return: List of moves that a Rook can make from the square given a board state
    """
    row, col = square
    moves = []
    player = board_state[square][0]

    transforms = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for transform in transforms:
        row_change = transform[0]
        col_change = transform[1]
        for step in range(1, 9):  # Add moves in direction till a piece is met
            move = (row + row_change * step, col + col_change * step)
            if is_valid_square(move):  # Check square is on the board
                if has_piece(move, board_state):

                    # Found enemy piece so add this square to moves and stop loop
                    if is_opponent_piece(player, board_state[move]):
                        moves.append(move)
                        break

                    # Found friendly piece so don't add this square and stop loop
                    else:
                        break
                else:
                    moves.append(move)  # Empty square so add and continue loop
            else:
                break  # Reach end of board so stop loop

    return moves


def generate_queen_moves(square: (int, int), board_state: dict):
    """
    Create a list of moves that are valid for a Queen at a given square given a certain board state.
    Queen movement consist of infinite tiles in all four straight directions (up, left, right, down) and all four
    diagonal directions (up-left, up-right, down-left, down-right) until the end of the board, unless:
    1. In the given direction there is a tile with a piece on it that belongs to the same player, all possible moves
    AFTER AND INCLUDING the tile with the piece are not valid moves
    2. In the given direction there is a tile with a piece on it that belongs to the opponent player, all possible moves
    AFTER the tile with the piece are not valid moves. The tile with the opponent piece is a valid move as the queen
    can capture the piece.
    :param square: Square where the Queen is located
    :param board_state: State of the board
    :return: List of moves that a Queen can make from the square given a board state
    """

    # The queen is simply a combination of Rook and Bishop, so we will generate moves as such
    moves = generate_rook_moves(square, board_state) + generate_bishop_moves(square, board_state)

    return moves


def generate_knight_moves(square: (int, int), board_state: dict):
    """
    Create a list of moves that are valid for a Knight at a given square given a certain board state.
    Knight movement consist of 2 squares in one straight direction (up, down, left, right) followed by 1 square in the
    perpendicular straight direction (if first move up/down, next must be left/right etc)
    :param square: Square where the Knight is located
    :param board_state: State of the board
    :return: List of moves that a Knight can make from the square given a board state
    """

    row, col = square
    moves = []
    player = board_state[square][0]

    # Apply 8 transforms to square to get all possible knight moves
    transforms = [(1, 2),
                  (1, -2),
                  (-1, 2),
                  (-1, -2),
                  (2, 1),
                  (2, -1),
                  (-2, 1),
                  (-2, -1)]

    for transform in transforms:
        row_change = transform[0]
        col_change = transform[1]
        move = (row + row_change, col + col_change)

        if is_valid_square(move):
            # Add move to list of moves if square is empty or has enemy piece to capture
            if not has_piece(move, board_state) or (has_piece(move, board_state) and
                                                    is_opponent_piece(player, board_state[move])):
                moves.append(move)

    return moves


""" PLACEHOLDER FUNCTIONS """
def perform_castling():
    return None


def perform_promotion():
    return None


def perform_enpassant():
    return None
