"""
Author: William Chio
Created: 22/05/24

Intent of this program is for a working 2 player chess game.
"""

import board_handler as bh
import visuals_and_txt as vis

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
    vis.display_board(board_state)
    vis.message_ask_input(player_turn)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
