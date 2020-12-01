import random
from math import sqrt

import numpy as np

test_matrix = [
    [0, 0, 0, 0, 0, 0, 0, 8, 9],
    [1, 2, 0, 4, 0, 6, 7, 0, 9],
    [0, 0, 0, 0, 0, 6, 0, 8, 9],
    [0, 0, 3, 0, 0, 0, 0, 0, 9],
    [0, 2, 4, 0, 0, 6, 7, 8, 9],
    [0, 0, 1, 4, 5, 0, 0, 8, 9],
    [0, 2, 3, 4, 5, 6, 0, 8, 9],
    [0, 2, 0, 4, 5, 0, 0, 8, 9],
    [0, 0, 3, 0, 5, 6, 7, 8, 9],
]

test_matrix2 = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [0, 0, 3, 0, 0, 0, 0, 0, 9],
    [0, 2, 4, 0, 0, 6, 7, 8, 9],
    [0, 2, 1, 4, 5, 0, 0, 8, 9],
    [0, 2, 3, 4, 5, 6, 0, 8, 9],
    [0, 2, 0, 4, 5, 0, 0, 8, 9],
    [0, 2, 3, 0, 5, 6, 7, 8, 9],
]




    # def generate_solved_matrix(self, base) -> np.ndarray:
    #     dim = base * base
    #     matrix: np.array
    #     depth: int
    #     solved_matrix = None
    #     xs: list
    #     ys: list
    #
    #     def fill_matrix():
    #         # nonlocal matrix, solved_matrix, depth
    #         depth += 1
    #         for y in ys:
    #             for x in xs:
    #                 if matrix[y][x] == 0:
    #                     for num in range(1, dim + 1):
    #                         if is_valid(x, y, num):
    #                             matrix[y][x] = num
    #                             fill_matrix()
    #                             if solved_matrix is not None or depth > 10000:
    #                                 return
    #                             matrix[y][x] = 0
    #                     return
    #         solved_matrix = matrix
    #
    #     while solved_matrix is None:
    #         matrix = np.array([[0 for _ in range(dim)] for _ in range(dim)])
    #         xs = [x for x in range(dim)]
    #         ys = [y for y in range(dim)]
    #         random.shuffle(xs)
    #         random.shuffle(ys)
    #         depth = 0
    #         fill_matrix()
    #
    #     cls.solved_matrix = solved_matrix
    #     return cls.solved_matrix
    #
