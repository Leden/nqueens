# coding: utf-8
"""
This module solves N queens problem.
Works well under both Python 3 and 2.
You can run the program by calling the following command in your terminal:

    python3 nqueens.py 50

where 50 is the size of a chessboard you want the problem to be solved on.
"""


import sys


def make_board(dimension):
    """Create and return new empty board"""
    return [
        [0] * dimension
        for _ in range(dimension)
    ]


def print_board(board):
    """Print the given board to stdout"""
    border = '+%s+' % ('-' * (len(board) * 2 - 1))

    print(border)
    for row in board:
        print('|%s|' % '|'.join('Q' if cell else '_' for cell in row))
    print(border)
    print('')


def can_place(board, row, col):
    """Take a board and a point and return True if it is possible to place
       a new queen into that point, False otherwise.

       Note that we don't check the board cells to the right
       and on the current column, because we are moving from top-left corner
       in outer cycle and there can not be any queens to the right
       from current position"""
    dimension = len(board)

    # Can't place a queen in a row that already has one
    if any(board[row][:col]): return False

    # Can't place a queen if any diagonal already has one: check upper-left branch...
    if any(board[r][c] for r, c
           in zip(range(row-1, -1, -1), range(col-1, -1, -1))):
        return False

    # ... and lower-left branch
    if any(board[r][c] for r, c
           in zip(range(row+1, dimension), range(col-1, -1, -1))):
        return False

    # If no attacking queens found so far, consider it safe to place a new one
    # in the given cell
    return True


def solve_recursively(board, col, acc):
    """Solve the N queens puzzle for a given board
       by recursively traversing the possible solutions tree"""
    dimension = len(board)

    # If all the board is filled, than we've found a solution.
    # Print it and increment the counter
    if col == dimension:
        print_board(board)
        return acc + 1

    for r in range(dimension):
        if can_place(board, r, col):

            # Place a queen here, 'coz we can
            board[r][col] = 1

            # Dive into subtree
            acc = solve_recursively(board, col+1, acc)

            # Remove a queen, moving backwards in the possible solutions tree
            board[r][col] = 0

    return acc


def print_argument_error(argument):
    """Utility function that prints an error message"""
    print('Sorry, can\'t create a chess board of size %s. '
          'Please, give a positive integer instead.' % argument)


def main():
    """Entry point"""
    dimension_arg = sys.argv[1]

    try:
        dimension = int(dimension_arg)
    except ValueError:
        print_argument_error(dimension_arg)
        return

    if dimension < 1:
        print_argument_error(dimension_arg)
        return

    board = make_board(dimension)
    total = solve_recursively(board, 0, 0)

    print('Total: %s' % total)


if __name__ == '__main__':
    main()
