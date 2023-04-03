import numpy as np
from itertools import cycle

def spiral_matrix(size):
    row, column = 0, 0
    array = [[None]*4 for _ in range(4)]
    movement = cycle([[0, 1], [1, 0], [0, -1], [-1, 0]])
    drow, dcolumn = next(movement)
    for num in range(1, size**2 + 1):
        array[row][column] = num
        if row + drow == size or column + dcolumn == size or array[row + drow][column + dcolumn] is not None:
            drow, dcolumn = next(movement)
        row += drow
        column += dcolumn

    return np.array(array)


print(spiral_matrix(4))
