# Author: William Chio
# Created: 22/05/24

# Board will look like this on start
# 8 |BR|Bk|BB|BK|BQ|BB|Bk|BR|
# 7 |BP|BP|BP|BP|BP|BP|BP|BP|
# 6 |  |  |  |  |  |  |  |  |
# 5 |  |  |  |  |  |  |  |  |
# 4 |  |  |  |  |  |  |  |  |
# 3 |  |  |  |  |  |  |  |  |
# 2 |WP|WP|WP|WP|WP|WP|WP|WP|
# 1 |WR|Wk|WB|WK|WQ|WB|Wk|WR|
#    A  B  C  D  E  F  G  H
#
import board_handler as bh
import visuals_and_txt as vis

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Intialise Pieces
    # Print layout
    # While (no_winner)
    # Get Move
    # Determine Pieces
    # Print Layout
    # --Repeat while loop--
    board = bh.initialise_board()
    vis.display_board(board)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
