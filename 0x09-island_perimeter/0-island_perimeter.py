#!/usr/bin/python3
"""island perimeter"""


def island_perimeter(grid):
    """gets the perimeter of an island described in grid
    Args:
        grid: a 2d list of integers
    Return:
        the perimeter of the island
    """
    if not grid or not grid[0]:
        return 0

    # [up(-y), down(y), left(-x), right(x)]
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    rows = len(grid)  # length of rows in the grid
    columns = len(grid[0])  # length of a column in the grid

    perimeter = 0  # total number of perimeter

    for ro in range(rows):
        for col in range(columns):
            if grid[ro][col] >= 1:
                zeros = 0

                # d_ro = row direction, d_co = column direction
                for d_ro, d_co in direction:
                    off_ro = ro + d_ro  # offset row
                    off_co = col + d_co  # offset column

                    # check if offset is within bounds
                    if 0 <= off_ro < rows and 0 <= off_co < columns:
                        # increment zero if offset of 1 island cell is zero
                        if grid[off_ro][off_co] == 0:
                            zeros += 1

                perimeter += zeros

    # return total perimeter
    return perimeter
