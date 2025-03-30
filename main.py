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
from checkmate import find_king, is_check

# Main run
if __name__ == '__main__':
    player_turn = "White"
    checkmate = False

    board_state = initialise_board()
    clear_screen()
    display_board(board_state)

    while not checkmate:
        #if is_check(player_turn, board_state):
            #get all pieces that can get out of check
            # while piece selected and piece moved to, do not remove the check
            # ask for input piece (dont allow for to_square input if selected piece has no move that can remove check
            # ask for input to move piece to (dont allow if the move does not remove check)
        from_square, selected_piece, valid_moves = input_select_piece(player_turn, board_state)
        to_square = input_move_to(player_turn, selected_piece, valid_moves)
        board_state = perform_move(board_state, from_square, to_square)
        display_board(board_state)
        player_turn = next_player_turn(player_turn)

        """ 
        1. When we identify we are in check, force player to only make move that gets out of check, even if legal
        also if player selects a piece which has no valid moves to stop the check, give a notice and not allow move
        2. If we identify that no possible moves can get the player out of check, set checkmate to true and declare
        other player winner
        """







