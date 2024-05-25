"""
Author: William Chio
Created: 24/05/24

Handles and verifies input from the player, this includes the square with the piece the player selects, and the move
that they make
"""


def input_select_piece(player: str, board_state: dict):
    """
    Takes user input to determine the piece and square that they want to move. This piece returned is a valid square
    that has a piece belonging to the player
    :param player: The player's turn
    :param board_state:  The state of the board
    :return: The selected piece, the square as it is on the board, the square as it is in board_state and a list of the pieces valid moves
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

    return piece, raw_square, square, valid_moves


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

    # Forward one square if not obstructed
    move1 = (row + direction, col)
    if is_valid_square(move1) and move1 not in board_state.keys():
        valid_moves.append(move1)

    # Forward two squares if nothing obstructing and pawn has not been moved yet
    if (row == 1 and direction == 1) or (row == 6 and direction == -1):  # Determine pawn has not moved
        move2 = (row + direction * 2, col)

        if move1 in valid_moves and move2 not in board_state.keys():  # Check both squares in front of pawn are empty
            valid_moves.append(move2)

    # Diagonal move left/right if there is opposing piece on those squares
    move3 = [(row + direction, col + 1), (row + direction, col - 1)]
    for move in move3:
        if is_valid_square(move) and move in board_state.keys():  # Check there is a piece on the valid square
            piece_on_square = board_state[move]

            if get_colour(piece_on_square) == get_opponent(player):  # Check piece on square belongs to the opponent
                valid_moves.append(move)
    return valid_moves


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
