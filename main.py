import pygame

pygame.init()
pygame.mixer.init()

larg, alt = 800, 400
run = True
tela = 0
pygame.mixer.music.load("resources/song.mp3")
play = True


bg = pygame.image.load("resources/blackhole.png")
fonte_ttl = pygame.font.SysFont("roboto", 40)
fonte_txt = pygame.font.SysFont("roboto", 20)
cor_btn = (69, 72, 81)
cor_btn_clicked = (47, 49, 55)
cor_fonte = (0, 0, 0)
cor_fundo = (228, 187, 151)

win = pygame.display.set_mode((larg, alt))
pygame.display.set_caption("Hello World")


def texto(text, pos, ft=fonte_txt, cor=cor_fonte):
    txt = ft.render(text, 1, cor)
    win.blit(txt, pos)
    # pygame.display.update()


class button:
    def __init__(self, cor, x, y, width, height, txt, clicked=False):
        self.cor = cor
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.txt = txt
        self.clicked = clicked

    def draw(self, win=win):
        if self.clicked:
            pygame.draw.rect(
                win, cor_btn_clicked, (self.x, self.y, self.width, self.height), 0
            )
        else:
            pygame.draw.rect(
                win, self.cor, (self.x, self.y, self.width, self.height), 0
            )
        texto = fonte_txt.render(self.txt, 1, cor_fonte)
        win.blit(
            texto,
            (
                self.x + (self.width / 2 - texto.get_width() / 2),
                self.y + (self.height / 2 - texto.get_height() / 2),
            ),
        )

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False


# BOTÕES
play_button = button(cor_btn, 550, 50, 200, 50, "JOGAR")
how_to_play_button = button(cor_btn, 550, 125, 200, 50, "COMO JOGAR")
settings_button = button(cor_btn, 550, 200, 200, 50, "CONFIGURAÇÕES")
quit_button = button(cor_btn, 550, 275, 200, 50, "SAIR")
volume_button = button(cor_btn, 525, 50, 200, 50, "MÚSICA")
back_button = button(cor_btn, 50, 300, 200, 50, "VOLTAR")

while run:
    # MÚSICA
    if play:
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.stop()

    # EVENTOS
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            run = False
        if tela == 0:
            win.blit(bg, (0, 0))
            texto("<Hello World/>", (50, 20), fonte_ttl, (255, 255, 255))
            play_button.draw()
            how_to_play_button.draw()
            settings_button.draw()
            quit_button.draw()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.isOver(pos):
                    tela = 1
                if how_to_play_button.isOver(pos):
                    tela = 2
                if settings_button.isOver(pos):
                    tela = 3
                if quit_button.isOver(pos):
                    pygame.time.delay(500)
                    run = False
        if tela == 1:
            win.fill(cor_fundo)
            # PLAY
        if tela == 2:
            # como jogar
            if event.type == pygame.QUIT:
                pygame.quit()
            win.fill(cor_fundo)
            texto("Como Jogar?", (50, 50), fonte_ttl, (255, 255, 255))
            texto(
                "Você poderá controlar o jogador de sua escolha com os botões do teclado.",
                ((50, 100), (100, 70)),
            )
            texto(
                "O objetivo do jogo é passar pelos desafios referentes a programação.",
                ((50, 115), (115, 75)),
            )
            back_button.draw()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.isOver(pos):
                    tela = 0
        if tela == 3:
            # SETTINGS
            win.fill(cor_fundo)
            texto("CONFIGURAÇÕES", (50, 20), fonte_ttl)
            back_button.draw()
            volume_button.draw()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if volume_button.isOver(pos):
                    volume_button.clicked = not volume_button.clicked
                    play = not play
                if back_button.isOver(pos):
                    tela = 0

    pygame.display.update()


pygame.quit()