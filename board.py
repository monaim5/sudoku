import threading
import pygame

from sudoku_logic import SudokuLogic
from cell import Cell


class Board:
    def __init__(self, parent, pos):
        self.parent = parent
        self.pos = pos
        self.selected_cell = None

        self.grid_color = (50, 0, 0)

        self.sudoku_logic = SudokuLogic(self, 3)
        self.cells = Cell.init_cells(self.sudoku_logic.matrix)
        self.solve_thread = None
        self.text_render = pygame.font.SysFont('arial', Cell.size // 2)
        self.height = Cell.size * self.sudoku_logic.dim + 2
        self.width = Cell.size * self.sudoku_logic.dim + 2
        self.surface = pygame.Surface((self.width, self.height))

    def update(self):
        pass

    # events ----------------------------------------------------------
    def click_events(self, mouse_pos):
        x = mouse_pos[0] // Cell.size
        y = mouse_pos[1] // Cell.size
        self.toggle_cell(x, y)

    def keydown_events(self, key):
        if self.selected_cell:
            # self.selected_cell.text = int(key)
            is_valid = self.sudoku_logic.is_valid(self.selected_cell.pos[0], self.selected_cell.pos[1], int(key))
            self.sudoku_logic.set_value(self.selected_cell, int(key), is_valid)
    # -----------------------------------------------------------------

    # board state -----------------------------------------------------
    @property
    def game_over(self):
        return not self.has_error and not self.has_empty

    @property
    def has_error(self):
        return any(map(lambda x: x.is_error, self.cells))

    @property
    def has_empty(self):
        return any(map(lambda x: x.is_empty, self.cells))

    def init_board(self):
        self.solve_thread = None
        self.sudoku_logic.init_matrix(40)
        self.cells = Cell.init_cells(matrix=self.sudoku_logic.matrix)
        self.selected_cell = None

    def solve_board(self):
        self.solve_thread = threading.Thread(target=self.sudoku_logic.solve_matrix_2,
                                             kwargs={'cells': self.cells, 'delay': .02,
                                                     'random_range': self.parent.menu.random_range_checkbox.checked,
                                                     'random_numbers': self.parent.menu.random_numbers_checkbox.checked})
        self.solve_thread.start()

    def toggle_cell(self, x, y):
        cell = self.cells[y * self.sudoku_logic.dim + x]
        if not cell.is_locked:
            if not self.selected_cell:
                cell.click()
                self.selected_cell = cell
            else:
                if cell == self.selected_cell:
                    cell.click()
                    self.selected_cell = None
                else:
                    self.selected_cell.click()
                    cell.click()
                    self.selected_cell = cell
    # -----------------------------------------------------------------

    # drawing ---------------------------------------------------------
    def draw(self, window, pos):

        self.draw_cells()
        self.draw_grid()
        window.blit(self.surface, pos)

    def draw_cells(self):
        for cell in self.cells:
            cell.draw(self.surface)

    def draw_grid(self):
        for x in range(self.sudoku_logic.dim + 1):
            thickness = 1 if x % self.sudoku_logic.base != 0 else 2
            pygame.draw.line(self.surface, self.grid_color,
                             (0, x * Cell.size),
                             (self.width, x * Cell.size), thickness)
            pygame.draw.line(self.surface, self.grid_color,
                             (x * Cell.size, 0),
                             (x * Cell.size, self.height), thickness)
