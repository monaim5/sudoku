import pygame

from board import Board
from menu import Menu
from paths import Dir


class Sudoku:
    margin = 10

    def __init__(self):
        self.window_color = (255, 255, 255)
        self.title = 'sudoku'
        self.icon = (Dir.static.value / 'sudoku.png').__str__()
        self.running = True
        self.mouse_pos = None
        pygame.init()
        pygame.display.set_caption(self.title)
        icon = pygame.image.load(self.icon)
        pygame.display.set_icon(icon)

        self.board_pos = (Sudoku.margin, Sudoku.margin)
        self.board = Board(self, self.board_pos)

        self.menu_pos = (Sudoku.margin, Sudoku.margin * 2 + self.board.height)
        self.menu = Menu(self, self.menu_pos, self.board.width, 100)

        self.width = self.board.width + Sudoku.margin * 2
        self.height = self.board.height + Sudoku.margin * 3 + self.menu.height
        self.window = pygame.display.set_mode((self.width, self.height))

    def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked_on_board = self.clicked_on_board()
                clicked_on_menu = self.clicked_on_menu()

                if clicked_on_board:
                    self.board.click_events(clicked_on_board)
                elif clicked_on_menu:
                    self.menu.click_events(clicked_on_menu)

            if event.type == pygame.KEYDOWN:
                if event.unicode.isdigit():
                    self.board.keydown_events(event.unicode)

    def update(self):
        self.mouse_pos = pygame.mouse.get_pos()
        self.menu.update((self.mouse_pos[0] - self.menu_pos[0], self.mouse_pos[1] - self.menu_pos[1]))

    def draw(self):
        self.window.fill(self.window_color)
        self.board.draw(self.window, self.board_pos)
        self.menu.draw(self.window)

        pygame.display.update()

    @staticmethod
    def get_relative_pos(pos, relative_to):
        if (relative_to.pos[0] < pos[0] < relative_to.pos[0] + relative_to.width) and \
                (relative_to.pos[1] < pos[1] < relative_to.pos[1] + relative_to.height):
            return pos[0] - relative_to.pos[0], pos[1] - relative_to.pos[1]

    def clicked_on_board(self):
        return self.get_relative_pos(self.mouse_pos, self.board)

    def clicked_on_menu(self):
        return self.get_relative_pos(self.mouse_pos, self.menu)

    def start_game(self):
        self.board.init_board()

    def check_game(self):
        if self.board.game_over:
            print('congratulations you have solved the puzzle')
        else:
            print('there are some errors there')

    def solve_game(self):
        self.board.solve_board()
