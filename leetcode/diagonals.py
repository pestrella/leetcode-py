def diagonals(m):
    """
    Given a matrix, return a list of the diagonals e.g.
    Input: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Output: [[1], [2, 4], [3, 5, 7], [6, 8], [9]]
    """

    diags = []
    height = len(m)
    width = len(m[0])
    col = 0

    for row in range(height):
        for col in range(col, width):
            diags.append(get_diagonal(m, row, col))

        col = width - 1

    return diags


def get_diagonal(m, row, col):
    diags = []
    while is_inbounds(m, row, col):
        diags.append(m[row][col])
        row += 1
        col -= 1

    return diags


def is_inbounds(m, row, col):
    return row > -1 and row < len(m) and col > -1 and col < len(m[0])


def print_diagonals(m):
    for d in diagonals(m):
        print(*d)
