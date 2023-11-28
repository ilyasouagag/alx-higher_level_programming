#!/usr/bin/python3
"""Solves the N-queens puzzle."""
import sys


def init_chessboard(size):
    """Initialize an `size`x`size` chessboard with 0's."""
    chessboard = [[' '] * size for _ in range(size)]
    return chessboard


def chessboard_copy(chessboard):
    """Return a deepcopy of a chessboard."""
    if isinstance(chessboard, list):
        return [chessboard_copy(row) for row in chessboard]
    return chessboard


def get_solution(chessboard):
    """Return the list of lists representation of a solved chessboard."""
    solution = [[r, c] for r, row in enumerate(
        chessboard) for c, val in enumerate(row) if val == 'Q']
    return solution


def mark_attacked(chessboard, row, col):
    """Mark spots on a chessboard as attacked."""
    size = len(chessboard)

    for c in range(col + 1, size):
        chessboard[row][c] = "x"

    for c in range(col - 1, -1, -1):
        chessboard[row][c] = "x"

    for r in range(row + 1, size):
        chessboard[r][col] = "x"

    for r in range(row - 1, -1, -1):
        chessboard[r][col] = "x"

    c = col + 1
    for r in range(row + 1, size):
        if c >= size:
            break
        chessboard[r][c] = "x"
        c += 1

    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        chessboard[r][c] = "x"
        c -= 1

    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= size:
            break
        chessboard[r][c] = "x"
        c += 1

    c = col - 1
    for r in range(row + 1, size):
        if c < 0:
            break
        chessboard[r][c] = "x"
        c -= 1


def recursive_solve(chessboard, row, queens, solutions):
    """Recursively solve an N-queens puzzle."""
    size = len(chessboard)
    if queens == size:
        solutions.append(get_solution(chessboard))
        return solutions

    for col in range(size):
        if chessboard[row][col] == " ":
            tmp_chessboard = chessboard_copy(chessboard)
            tmp_chessboard[row][col] = "Q"
            mark_attacked(tmp_chessboard, row, col)
            solutions = recursive_solve(
                tmp_chessboard, row + 1, queens + 1, solutions)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    chessboard = init_chessboard(int(sys.argv[1]))
    solutions = recursive_solve(chessboard, 0, 0, [])
    for solution in solutions:
        print(solution)
