import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect

cor_fundo = (228, 187, 151)
cor_fonte = (183, 93, 105)
azul = (161, 252, 223)
roxo = (55, 37, 73)
branco = (234, 205, 194)
fonte = "Roboto"

run = True


def create_text(text, font_size, text_color, bg_color):
    font = pygame.freetype.SysFont(fonte, font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_color, bgcolor=bg_color)
    return surface.convert_alpha()


class UIElement(Sprite):
    def __init__(self, center_position, text, font_size, bg_color, text_color):
        self.mouse_over = False

        default_image = create_text(
            text=text, font_size=font_size, text_color=text_color, bg_color=bg_color
        )

        highlighted_image = create_text(
            text=text,
            font_size=font_size * 1.2,
            text_color=text_color,
            bg_color=bg_color,
        )

        self.images = [default_image, highlighted_image]
        self.rects = [
            default_image.get_rect(center=center_position),
            highlighted_image.get_rect(center=center_position),
        ]

        super().__init__()

    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
        else:
            self.mouse_over = False

    def draw(self, surface):
        surface.blit(self.image, self.rect)


while run:
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("<Hello Word!/>")

    uielement = UIElement(
        center_position=(400, 400),
        font_size=30,
        bg_color=cor_fundo,
        text_color=cor_fonte,
        text="Hello World",
    )

    # main loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(cor_fundo)

    uielement.update(pygame.mouse.get_pos())
    uielement.draw(screen)
    pygame.display.flip()

pygame.quit()
