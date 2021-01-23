import numpy as np
import pygame

from shared_models import animate_color


class Cell:
    size = 40
    padding = 2
    color = (23, 234, 2)
    fill_normal_color = (240, 240, 240)
    fill_error_color = (255, 123, 0)
    fill_solved_color = (36, 255, 43)
    fill_lock_color = (200, 200, 200)
    fill_selection_color = (47, 232, 245)

    text_normal_color = (0, 0, 0)
    text_error_color = (255, 0, 0)
    text_selection_color = (255, 255, 0)

    selected = None

    def __init__(self, pos, text, is_locked=False, is_error=False):
        self.pos = pos
        self.width = Cell.size
        self.height = Cell.size

        self.rect = (0, 0, self.width, self.height)

        self.text = text
        self.is_locked = is_locked
        self.is_error = is_error
        self.is_selected = False
        self.is_solved = False
        self.is_blank = False

        self.fill_color = Cell.fill_normal_color
        self.text_color = Cell.text_normal_color
        self.surface = pygame.Surface((Cell.size, Cell.size))
        self.text_render = pygame.font.SysFont('arial', Cell.size // 2)

    @property
    def is_empty(self):
        return self.text == 0

    def click(self):
        self.is_selected = not self.is_selected

    def draw(self, surface):
        self.draw_fill()
        self.draw_text()
        surface.blit(self.surface, (self.pos[0] * Cell.size, self.pos[1] * Cell.size))

    def draw_text(self):
        if self.text != 0:
            self.text_color = Cell.text_normal_color if not self.is_error else Cell.text_error_color
            txt = self.text_render.render(str(self.text), False, self.text_color)
            self.surface.blit(txt, (Cell.size / 2 - txt.get_width() / 2, (Cell.size - txt.get_height()) / 2))

    def draw_fill(self):
        if self.is_locked:
            self.fill_color = Cell.fill_lock_color
        elif self.is_blank:
            self.fill_color = Cell.fill_normal_color
        elif self.is_selected:
            self.fill_color = Cell.fill_selection_color
        elif self.is_error:
            self.fill_color = Cell.fill_error_color
        elif self.is_solved:
            self.fill_color = animate_color(self.fill_color, Cell.fill_solved_color)
        else:
            self.fill_color = Cell.fill_normal_color

        pygame.draw.rect(self.surface, self.fill_color, self.rect)

    @classmethod
    def init_cells(cls, matrix=None):
        if type(matrix) == np.ndarray:
            return [Cell((x, y), num) if num == 0 else Cell((x, y), num, True)
                    for y, row in enumerate(matrix) for x, num in enumerate(row)]