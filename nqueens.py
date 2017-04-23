# coding: utf-8
"""
This module solves N queens problem.
Works well under both Python 3 and 2.
You can run the program by calling the following command in your terminal:

    python3 nqueens.py 50

where 50 is the size of a chessboard you want the problem to be solved on.
"""


import sys
from collections import namedtuple


Point = namedtuple('Point', ('x', 'y'))


def print_board(board):
    """Print the given board to stdout"""
    size = len(board)
    border = '+%s+' % ('-' * (size * 2 - 1))

    print(border)
    for x in range(size):
        print(
            '|%s|' % '|'.join('Q' if Point(x, y) in board else '_'
                              for y in range(size))
        )
    print(border + '\n')


def can_place(board, size, point):
    """Take a board and a point and return True if it is possible to place
       a new queen into that point, False otherwise.

       Note that we don't check the board cells to the right
       and on the current column, because we are moving from top-left corner
       in outer loop and there can not be any queens to the right
       from current position"""
    # size = len(board)
    row, col = point

    # Can't place a queen in a row that already has one
    if board & {Point(row, c) for c in range(col)}: return False

    # Can't place a queen if any diagonal already has one: upper-left...
    if board & {Point(r, c) for (r, c)
                in zip(range(row-1, -1, -1), range(col-1, -1, -1))}:
        return False

    # ... and lower-left
    if board & {Point(r, c) for (r, c)
                in zip(range(row+1, size), range(col-1, -1, -1))}:
        return False

    # If no attacking queens found so far, consider it safe to place a new one
    # in the given cell
    return True


def solve_recursively(board, size, col, acc):
    """Solve the N queens puzzle for a given board
       by recursively traversing the possible solutions tree"""

    # If all the board is filled, than we've found a solution.
    # Print it and increment the counter
    if col == size:
        print_board(board)
        return acc + 1

    for r in range(size):
        point = Point(r, col)
        if can_place(board, size, point):

            # Place a queen here, 'coz we can
            board.add(point)

            # Dive into subtree
            acc = solve_recursively(board, size, col+1, acc)

            # Remove a queen, moving backwards in the possible solutions tree
            board.remove(point)

    return acc


def print_argument_error(argument):
    """Utility function that prints an error message"""
    print('Sorry, can\'t create a chess board of size %s. '
          'Please, give a positive integer instead.' % argument)


def main():
    """Entry point"""
    size_arg = sys.argv[1]

    try:
        size = int(size_arg)
    except ValueError:
        print_argument_error(size_arg)
        return

    if size < 1:
        print_argument_error(size_arg)
        return

    total = solve_recursively(set(), size, 0, 0)

    print('Total: %s' % total)


if __name__ == '__main__':
    main()
