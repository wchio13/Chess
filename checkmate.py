"""
Author: William Chio
Created: 09/06/24

Handles the checking of the King to determine if they are in check
"""
from board_handler import simulate_move
from piece_moves import generate_rook_moves, generate_bishop_moves, generate_knight_moves, determine_valid_moves
from util import get_distance, is_opponent_piece, has_piece, player_from_square


def is_check(player: str, board_state: dict):
    """
    Determine whether the current player is in check (i.e. The current player's King is in danger of being captured)
    This will be accomplished by determining the square where the King is, and then generating different types of
    piece moves as if the King where that piece. Then for each of the generated moves, we determine if there is an
    opponent piece that is of the correct piece type that can capture the King from that square. This has two
    components, straight (up, down, left, right) and diagonal (up-left, up-right, down-left, down-right)

    Example:
    Say we have the King at G3, we want to determine if it is in check. So we generate the moves of a Rook from that
    square, as if the King itself was a Rook. Now we check each of these generated moves and see if on these squares
    there is a piece that belongs to the opponent that is either
    1. A Rook (Any no. of squares away)
    2. A Queen (Any no. of squares away)
    3. A king (One square away)
    Since these pieces are what would be able to capture the King on these squares

    :param player: Player to determine if their King is in check
    :param board_state: The state of the board
    :return:
    """

    king_square = find_king(player, board_state)

    return check_via_straight(king_square, board_state) or check_via_diagonal(king_square, board_state) or check_via_knight(king_square, board_state)


def find_king(player: str, board_state: dict):
    """
    Find the square where the player's king is
    :param player: Player for whom to find the King for (e.g 'W')
    :param board_state: The state of the board
    :return: The square where the player's King is
    """

    # King piece to look for
    king = player[0] + "K"

    for square in board_state.keys():
        if board_state[square] == king:
            return square

    print("UH You have no King")


def check_via_straight(king_square: (int, int), board_state: dict):
    """
    Determine whether the King at the given square is in check via a straight direction (up, down, left, right)
    :param king_square: The square where the King is on
    :param board_state: The state of the board
    :return: return True if King is in check via a straight direction, otherwise return False
    """

    potential_checks = generate_rook_moves(king_square, board_state)
    player = player_from_square(king_square, board_state)

    for check_square in potential_checks:
        pieces_that_can_check = ["R", "Q"] # Rook & Queen can check on straight direction, also King if distance is 1
        if get_distance(king_square, check_square, "S") == 1:
            pieces_that_can_check.append("K")

        if has_piece(check_square, board_state):
            piece = board_state[check_square]
            piece_type = piece[1]

            # Piece is a Rook or Queen (or King if distance is 1)
            if is_opponent_piece(player, piece) and piece_type in pieces_that_can_check:
                return True
    return False


def check_via_diagonal(king_square: (int, int), board_state: dict):
    """
    Determine whether the King at the given square is in check via a diagonal direction (up-left, up-right,
    down-left, down-right)
    :param king_square: The square where the King is on
    :param board_state: The state of the board
    :return: return True if King is in check via a straight direction, otherwise return False
    """

    potential_checks = generate_bishop_moves(king_square, board_state)
    player = player_from_square(king_square, board_state)

    for check_square in potential_checks:
        pieces_that_can_check = ["B", "Q"] # Bishop & Queen can check on straight direction, also King if distance is 1
        if get_distance(king_square, check_square, "D") == 1:
            pieces_that_can_check.append("K")

            # See if pawn can check from this square
            # if white, see if check square has row +1 of the king square
            # if black see if check square has row -1 of the king square
            if (player == "W" and king_square[0] > check_square[0]) or \
               (player == "B" and king_square[0] < check_square[0]):
                pieces_that_can_check.append("P")

        if has_piece(check_square, board_state):
            piece = board_state[check_square]
            piece_type = piece[1]

            # Piece is a Bishop or Queen (or King if distance is 1 or Pawn if correct direction)
            if is_opponent_piece(player, piece) and piece_type in pieces_that_can_check:
                return True

    return False


def check_via_knight(king_square: (int, int), board_state: dict):
    """
    Determine whether King is in check via a Knight
    :param king_square: The square where the King is on
    :param board_state: The state of the board
    :return: return True if King is in check via a knight, otherwise return False
    """

    potential_checks = generate_knight_moves(king_square, board_state)
    player = player_from_square(king_square, board_state)

    for check_square in potential_checks:

        if has_piece(check_square, board_state):
            piece = board_state[check_square]
            piece_type = piece[1]

            if is_opponent_piece(player, piece) and piece_type == "N":
                return True

    return False


def player_has_no_moves(king_square: (int, int), board_state: dict):
    """
    Determine whether the player has any possible, non-checking, valid moves by simulating every single possible move
    they can make. Used to determine if player is checkmate (if this returns False and player is currently check)
    or if stalemate has occurred (if this returns False and player IS NOT in check).

    :param king_square: square where the King is on
    :param board_state: The state of the board
    :return: Returns False if there is at least one move the player can make that will remove check
    """

    player = player_from_square(king_square, board_state)
    for square in board_state.keys():
        # scan board and get all pieces which belong to player
        if player_from_square(square, board_state) == player:
            possible_moves = determine_valid_moves(square, board_state)
            for move in possible_moves:
                # want to perform each move and see if we are still in check
                if not move_causes_check(player, board_state, square, move):
                    return False

    return True


def move_causes_check(player: str, board_state: dict, from_square: (int, int), to_square: (int,int)):
    """
    Given a particular move, determine whether performing it will result in the player's own king being put into check
    :param player: Player who performed move
    :param board_state: The state of the board
    :param to_square: The square where the piece to move is on
    :param from_square: The square to move the piece to
    :return: True if performing the move results in the player's king being placed in check
    """

    simulated_board_state = simulate_move(board_state, from_square, to_square)
    return is_check(player, simulated_board_state)

