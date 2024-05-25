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

import board_handler as bh
import visuals_and_txt as vis
import input_processor as inp

# Main run
if __name__ == '__main__':
    player_turn = "White"
    # Intialise Pieces
    # Print layout
    # While (no_winner)
    # Get Move
    # Determine Pieces
    # Print Layout
    # --Repeat while loop--
    board_state = bh.initialise_board()
    vis.clear_screen()
    vis.display_board(board_state)
    piece, raw_square, square, valid_moves = inp.input_select_piece(player_turn, board_state)
    vis.message_piece_selection(player_turn, piece, raw_square)


