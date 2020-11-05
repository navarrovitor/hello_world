# import pygame
# import pygame.freetype
# from pygame.sprite import Sprite
# from pygame.rect import Rect

# cor_fundo = (228, 187, 151)
# cor_fonte = (183, 93, 105)
# azul = (161, 252, 223)
# roxo = (55, 37, 73)
# branco = (234, 205, 194)
# fonte = "Roboto"


# def text_in_surface(text, font_size, text_color, bg_color):
#     font = pygame.freetype.SysFont(fonte, font_size, bold=True)
#     surface, _ = font.render(text=text, fgcolor=text_color, bgcolor=bg_color)
#     return surface.convert_alpha()


# class UIElement(Sprite):
#     def __init__(self, center_position, text, font_size, bg_color, text_color):
#         super().__init__()

#         self.mouse_over = False

#         default_image = text_in_surface(text, font_size, text_color, bg_color)

#         highlighted_image = text_in_surface(text, font_size * 1.2, text_color, bg_color)

#         self.images = [default_image, highlighted_image]
#         self.rects = [
#             default_image.get_rect(center=center_position),
#             highlighted_image.get_rect(center=center_position),
#         ]

#     @property
#     def image(self):
#         return self.images[1] if self.mouse_over else self.image[0]

#     @property
#     def rect(self):
#         return self.rects[1] if self.mouse_over else self.rects[0]

#     def update(self, mouse_pos):
#         if self.rect.collidepoint(mouse_pos):
#             self.mouse_over = True
#         else:
#             self.mouse_over = False

#     def draw(self, surface):
#         surface.blit(self.image, self.rect)


# def main():
#     pygame.init()

#     screen = pygame.display.set_mode((800, 600))
#     pygame.display.set_caption("<Hello Word!/>")

#     uielement = UIElement(
#         center_position=(400, 400),
#         text="Teste",
#         font_size=30,
#         bg_color=cor_fundo,
#         text_color=cor_fonte,
#     )

#     while True:
#         for event in pygame.event.get():
#             pass
#         screen.fill(cor_fundo)

#         uielement.update(pygame.mouse.get_pos())
#         uielement.draw(screen)
#         pygame.display.flip()


# if __name__ == "__main__":
#     main()

import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect

cor_fundo = (228, 187, 151)
cor_fonte = (183, 93, 105)


def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
    # """ Returns surface with text written on """
    font = pygame.freetype.SysFont("Courier", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()


class UIElement(Sprite):
    # """ An user interface element that can be added to a surface """

    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb):
        # """
        # Args:
        #     center_position - tuple (x, y)
        #     text - string of text to write
        #     font_size - int
        #     bg_rgb (background colour) - tuple (r, g, b)
        #     text_rgb (text colour) - tuple (r, g, b)
        # """
        self.mouse_over = False  # indicates if the mouse is over the element

        # create the default image
        default_image = create_surface_with_text(
            text=text, font_size=font_size, text_rgb=text_rgb, bg_rgb=bg_rgb
        )

        # create the image that shows when mouse is over the element
        highlighted_image = create_surface_with_text(
            text=text, font_size=font_size * 1.2, text_rgb=text_rgb, bg_rgb=bg_rgb
        )

        # add both images and their rects to lists
        self.images = [default_image, highlighted_image]
        self.rects = [
            default_image.get_rect(center=center_position),
            highlighted_image.get_rect(center=center_position),
        ]

        # calls the init method of the parent sprite class
        super().__init__()

    # properties that vary the image and its rect when the mouse is over the element
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
        # """ Draws element onto a surface """
        surface.blit(self.image, self.rect)


def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))

    # create a ui element
    uielement = UIElement(
        center_position=(400, 400),
        font_size=30,
        bg_rgb=cor_fundo,
        text_rgb=cor_fonte,
        text="Hello World",
    )

    # main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                False

        screen.fill(cor_fundo)

        uielement.update(pygame.mouse.get_pos())
        uielement.draw(screen)
        pygame.display.flip()


# call main when the script is run
if __name__ == "__main__":
    main()