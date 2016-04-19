import numpy as np


def determinant(matrix):
    if len(matrix) == 0:
        return 1
    if len(matrix) == 1:
        return matrix[0]

    x = np.array(matrix)
    return round(np.linalg.det(x))





