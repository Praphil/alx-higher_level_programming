#!/usr/bin/python3
"""
Module containing functions to search for solutions to N-queens problem.
"""


def all_possible(n=4):
    """Find all possible solutions by placing the first queen on
    the first row, with different column positions starting from
    the 2nd column to 2nd to last column.

    Args:
        n (int): The size of the chessboard and the number of queens.
    """

    for i in range(n):
        matrix = [[0, i]]
        col = [z for z in range(n) if z != i]
        recur_bt(matrix, 1, col, n)


def recur_bt(matrix, row, col, n):
    """
    Recursive backtracking function to test remaining possible positions
    for placing queens on the board.

    Args:
        matrix (list): A matrix representing queen positions.
        row (int): The current row being processed.
        col (list): Possible column positions for the remaining queens.
        n (int): The size of the board and the number of queens.

    Returns:
        A solution matrix or None if no solution is found.
    """
    if len(matrix) == n:
        return matrix

    if row:
        i = row
        for j in col:
            if (
                not bot_right(matrix, i + 1, j + 1, n)
                or not bot_left(matrix, i + 1, j - 1, n)
                or not top_left(matrix, i - 1, j - 1, n)
                or not top_right(matrix, i - 1, j + 1, n)
            ):
                continue
            matrix.append([i, j])
            new_col = [z for z in col if z != j]
            new_matrix = recur_bt(matrix, row + 1, new_col, n)
            if new_matrix is not None:
                print(matrix)
            matrix.remove([i, j])
    return None


def bot_right(matrix, y, x, n):
    """Test if there are any queens on the bottom right diagonal."""
    while y < n and x < n:
        if [y, x] in matrix:
            return False
        else:
            y += 1
            x += 1
    return True


def bot_left(matrix, y, x, n):
    """Test if there are any queens on the bottom left diagonal."""
    while y < n and x >= 0:
        if [y, x] in matrix:
            return False
        else:
            y += 1
            x -= 1
    return True


def top_left(matrix, y, x, n):
    """Test if there are any queens on the top left diagonal."""
    while y >= 0 and x >= 0:
        if [y, x] in matrix:
            return False
        else:
            y -= 1
            x -= 1
    return True


def top_right(matrix, y, x, n):
    """Test if there are any queens on the top right diagonal."""
    while y >= 0 and x < n:
        if [y, x] in matrix:
            return False
        else:
            y -= 1
            x += 1
    return True


if __name__ == "__main__":
    from sys import argv

    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        n = int(argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    all_possible(n)
