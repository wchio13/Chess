
"""
Author: William Chio
Created: 22/05/24

Intent of this program is for a working 2 player chess game.
    8 |BR|BN|BB|BK|BQ|BB|BN|BR|
    7 |BP|BP|BP|BP|BP|BP|BP|BP|
    6 |  |  |  |  |  |  |  |  |
    5 |  |  |  |  |  |  |  |  |
    4 |  |  |  |  |  |  |  |  |
    3 |  |  |  |  |  |  |  |  |
    2 |WP|WP|WP|WP|WP|WP|WP|WP|
    1 |WR|WN|WB|WK|WQ|WB|WN|WR|
       A  B  C  D  E  F  G  H
"""
import util
from board_handler import initialise_board, perform_move
from input_processor import input_select_piece, input_move_to
from visuals_and_txt import clear_screen, display_board
from util import next_player_turn
from checkmate import find_king, is_check, player_has_no_moves, move_causes_check

# Main run
if __name__ == '__main__':
    player_turn = "White"
    checkmate = False
    stalemate = False
    in_check = False

    board_state = initialise_board()
    clear_screen()
    display_board(board_state)

    while not checkmate and not stalemate:
        king = find_king(player_turn, board_state)
        player_cant_move = player_has_no_moves(king, board_state)
        in_check = is_check(player_turn, board_state)
        # NO MOVE -> Check -> Checkmate
        # No Move -> not check -> stalemate
        # can move -> check -> have to play move that removes check

        if player_cant_move:
            if in_check: # Check + cant move = checkmate
                checkmate = True

            else: # no check + cant move = stalemate
                stalemate = True

        # Piece selection
        if not stalemate and not checkmate:
            if in_check:
                print(f"{player_turn} is in Check!\n")
            from_square, selected_piece, valid_moves = input_select_piece(player_turn, board_state, in_check)

            # Piece movement
            to_square = input_move_to(player_turn, selected_piece, valid_moves, in_check)

            board_state = perform_move(board_state, from_square, to_square)
            display_board(board_state)
            player_turn = next_player_turn(player_turn)
            if in_check:
                in_check = False

    print(f"Checkmate! {next_player_turn(player_turn)} is victorious!\n")







