import pygame


class Button:
    text_size = 12
    width = 80
    height = 30

    def __init__(self, text, pos, dim=(width, height), color=(73, 73, 73), function=None,
                 params=None):
        self.pos = pos
        self.dim = dim
        self.image = pygame.Surface(dim)
        self.rect = pygame.Rect(*self.pos, *self.dim)
        self.text_render = pygame.font.SysFont('arial', Button.text_size, 1.5)
        self.text = text
        self.color = color
        # self.highlighted_color = highlighted_color
        self.function = function
        self.params = params
        self.highlighted = False

    def update(self, mouse):
        self.highlighted = True if self.rect.collidepoint(mouse) else False

    def draw(self, window):
        self.draw_button()
        self.draw_text(self.text)
        window.blit(self.image, self.pos)

    def click(self):
        if self.params:
            self.function(self.params)
        else:
            self.function()

    def draw_text(self, text, color=(0, 0, 0)):
        button_text = self.text_render.render(text, False, color)
        width, height = button_text.get_size()
        x = (self.dim[0] - width) / 2
        y = (self.dim[1] - height) / 2
        self.image.blit(button_text, (x, y))

    def draw_button(self):
        if self.highlighted:
            self.image.fill(self.color, special_flags=pygame.BLEND_RGB_ADD)
        else:
            self.image.fill(self.color)


class CheckBox(Button):
    width = 20
    height = 20

    def __init__(self, pos, color=(73, 73, 73), checked_color=(225, 17, 48)):
        super().__init__('', pos, (CheckBox.width, CheckBox.height), color=color)
        self.checked_color = checked_color
        self.checked = False

    def draw_text(self, text, color=(255, 0, 0)):
        pass

    def click(self):
        self.checked = not self.checked
        print(self.checked)

    def draw_button(self):
        if self.highlighted:
            self.image.fill(self.checked_color, special_flags=pygame.BLEND_RGB_ADD) if self.checked else self.image.fill(self.color, special_flags=pygame.BLEND_RGB_ADD)
        else:
            self.image.fill(self.checked_color) if self.checked else self.image.fill(self.color)

    def draw(self, window):
        self.draw_button()
        window.blit(self.image, self.pos)


class Label(Button):
    width = 80
    height = 30

    def __init__(self, text, pos):
        super().__init__(text, pos)

    def click(self):
        pass

    def draw_button(self):
        self.image.set_alpha(128)
        self.image.fill((255, 255, 255))
