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
from checkmate import find_king, is_check, generate_moves_that_remove_check

# Main run
if __name__ == '__main__':
    player_turn = "White"
    checkmate = False
    in_check = False

    board_state = initialise_board()
    clear_screen()
    display_board(board_state)

    while not checkmate:
        if is_check(player_turn, board_state):
            uncheck_moves = generate_moves_that_remove_check(find_king(player_turn, board_state), board_state)
            if uncheck_moves:
                in_check = True
                print(f"{player_turn} is in Check!")
                # There is no moves that remove check, therefore it is checkmate
            else:
                checkmate = True

        # Piece selection
        from_square, selected_piece, valid_moves = input_select_piece(player_turn, board_state)
        if in_check and not checkmate:
            while from_square not in uncheck_moves.keys():
                print("Invalid selection. That piece cannot prevent check")
                from_square, selected_piece, valid_moves = input_select_piece(player_turn, board_state)

        # Piece movement
        to_square = input_move_to(player_turn, selected_piece, valid_moves)
        if in_check and not checkmate:
            while to_square not in uncheck_moves[from_square]:
                print("Invalid move. King is still in check")
                to_square = input_move_to(player_turn, selected_piece, valid_moves)

        board_state = perform_move(board_state, from_square, to_square)
        display_board(board_state)
        player_turn = next_player_turn(player_turn)
        if in_check:
            in_check = False

    print(f"Checkmate! {next_player_turn(player_turn)} is victorious!\n")







