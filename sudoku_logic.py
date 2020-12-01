import random
import time

import numpy as np


class SudokuLogic:
    def __init__(self, parent, base):
        # self.solved_matrix = None
        self.base = base
        self.dim = self.base * self.base
        self.parent = parent
        self.matrix = np.array([[0 for _ in range(self.dim)] for _ in range(self.dim)])
        self.matrix_solved = False

        self.locked_cells = set()
        self.errors = set()
        self.gaps = set()
        self.depth = 0

    @property
    def dirty(self):
        return

    def set_value(self, cell):
        if self.is_valid(cell.pos[0], cell.pos[1], int(cell.text)):
            cell.is_error = False
        else:
            cell.is_error = True
        self.matrix[cell.pos[1]][cell.pos[0]] = cell.text

    def init_matrix(self, gaps):
        while not self.matrix_solved:
            self.matrix = np.array([[0 for _ in range(self.dim)] for _ in range(self.dim)])
            self.solve_matrix(random_range=True)
        self.generate_playing_matrix(gaps)
        self.matrix_solved = False

    def generate_playing_matrix(self, gaps):
        actual_gaps = 0
        self.locked_cells = {(x, y) for y in range(self.dim) for x in range(self.dim)}

        coordinates = [(x, y) for y in range(self.dim) for x in range(self.dim)]
        random.shuffle(coordinates)

        for x, y in coordinates:
            if actual_gaps >= gaps:
                return
            self.matrix[y][x] = 0
            self.locked_cells.remove((x, y))
            self.gaps.add((x, y))
            actual_gaps += 1

    def solve_matrix(self, *, random_range=False, delay=False):
        x_range = [x for x in range(self.dim)]
        y_range = [y for y in range(self.dim)]
        self.depth = 0
        if random_range:
            random.shuffle(x_range)
            random.shuffle(y_range)

        def backtrack_algorithm():
            self.depth += 1
            for y in y_range:
                for x in x_range:
                    if self.matrix[y][x] == 0:
                        for num in range(1, self.dim + 1):
                            is_valid = self.is_valid(x, y, num)
                            if delay:
                                self.matrix[y][x] = num
                                if not is_valid:
                                    self.errors.add((x, y))
                                time.sleep(delay)
                                if not is_valid:
                                    self.errors.remove((x, y))
                                self.matrix[y][x] = 0
                            if is_valid:
                                self.matrix[y][x] = num
                                backtrack_algorithm()
                                if self.matrix_solved or self.depth > self.dim * 500:
                                    return
                                self.matrix[y][x] = 0

                        return
            self.matrix_solved = True
            return
        backtrack_algorithm()

    def solve_matrix_2(self, *, cells, delay=False, random_range=False, random_numbers=False):
        numbers = list(range(1, self.dim + 1))
        cells_range = list(range(len(cells)))
        if random_numbers:
            random.shuffle(numbers)
        if random_range:
            random.shuffle(cells_range)
        print(random_range)

        def backtrack_algorithm():
            for i in cells_range:
                if cells[i].is_empty:
                    for num in numbers:
                        if not self.parent.solve_thread:
                            print('exit from solve process')
                            exit()
                        is_valid = self.is_valid(cells[i].pos[0], cells[i].pos[1], num)

                        if delay:
                            cells[i].text = num
                            self.set_value(cells[i])
                            time.sleep(delay)
                            cells[i].text = 0
                            self.set_value(cells[i])
                        if is_valid:
                            cells[i].text = num
                            self.set_value(cells[i])
                            backtrack_algorithm()
                            if self.matrix_solved:
                                return
                            cells[i].text = 0
                            self.set_value(cells[i])

                    return
            self.matrix_solved = True
            return
        backtrack_algorithm()

    def is_valid(self, x, y, number):
        return self.valid_for_row(y, number) and self.valid_for_column(x, number) and self.valid_for_square(x, y, number)

    def valid_for_row(self, y, number):
        return number not in [x for x in self.matrix[y, :] if x != 0]

    def valid_for_column(self, x, number):
        return number not in [x for x in self.matrix[:, x] if x != 0]

    def valid_for_square(self, x, y, number):
        box_x = (x // self.base) * self.base
        box_y = (y // self.base) * self.base
        return number not in [x for x in self.matrix[box_y:box_y + self.base, box_x:box_x + self.base].flatten()
                              if x != 0]
