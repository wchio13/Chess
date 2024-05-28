"""
Author: William Chio
Created: 22/05/24

Intent of this program is for a working 2 player chess game.
    8 |BR|Bk|BB|BK|BQ|BB|Bk|BR|
    7 |BP|BP|BP|BP|BP|BP|BP|BP|
    6 |  |  |  |  |  |  |  |  |
    5 |  |  |  |  |  |  |  |  |
    4 |  |  |  |  |  |  |  |  |
    3 |  |  |  |  |  |  |  |  |
    2 |WP|WP|WP|WP|WP|WP|WP|WP|
    1 |WR|Wk|WB|WK|WQ|WB|Wk|WR|
       A  B  C  D  E  F  G  H
"""

from board_handler import initialise_board, perform_move
from input_processor import input_select_piece, input_move_to
from visuals_and_txt import clear_screen, display_board
from util import next_player_turn

# Main run
if __name__ == '__main__':
    player_turn = "White"
    checkmate = False
    # Intialise Pieces
    # Print layout
    # While (no_winner)
    # Get Move
    # Determine Pieces
    # Print Layout
    # --Repeat while loop--
    board_state = initialise_board()
    clear_screen()
    display_board(board_state)
    while not checkmate:
        from_square, selected_piece, valid_moves = input_select_piece(player_turn, board_state)
        to_square = input_move_to(player_turn, selected_piece, valid_moves)
        board_state = perform_move(board_state, from_square, to_square)
        display_board(board_state)
        player_turn = next_player_turn(player_turn)





