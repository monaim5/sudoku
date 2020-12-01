import pygame

from shared_models import Button, CheckBox, Label


class Menu:
    padding = 2
    top_margin = 20

    def __init__(self, parent, pos, width, height):
        self.parent = parent
        self.pos = pos
        self.width = width
        self.height = height
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill((255, 255, 255))
        self.new_game_button = Button('New game', self.get_button_pos(Button, 0, 0),
                                      color=(0, 184, 49),
                                      function=self.parent.start_game)
        self.check_button = Button('Check', self.get_button_pos(Button, 1, 0),
                                   color=(237, 138, 0),
                                   function=self.parent.check_game)
        self.solve_button = Button('Solve', self.get_button_pos(Button, 2, 0),
                                   color=(0, 212, 227),
                                   function=self.parent.solve_game)
        self.random_range_label = Label('Random range', self.get_button_pos(Label, 1, 1))
        self.random_numbers_label = Label('Random number', self.get_button_pos(Label, 1, 2))
        self.random_range_checkbox = CheckBox(self.get_button_pos(CheckBox, 2, 1),
                                              checked_color=(0, 212, 227))
        self.random_numbers_checkbox = CheckBox(self.get_button_pos(CheckBox, 2, 2),
                                                checked_color=(0, 212, 227))

        self.buttons = {self.check_button, self.new_game_button, self.solve_button,
                        self.random_range_checkbox, self.random_numbers_checkbox,
                        self.random_range_label, self.random_numbers_label}

    def draw(self, window):
        for button in self.buttons:
            button.draw(self.surface)
        window.blit(self.surface, self.pos)

    def update(self, mouse):
        for button in self.buttons:
            button.update(mouse)

    def click_events(self, mouse_pos):
        self.click_button()

    def click_button(self):
        for button in self.buttons:
            if button.highlighted:
                button.click()

    def get_button_pos(self, button, x, y):
        button_container_width = self.width / 3
        button_container_height = self.height / 3
        return button_container_width * x + button_container_width / 2 - button.width / 2 + Menu.padding, \
               button_container_height * y + button_container_height / 2 - button.height / 2 + Menu.padding
