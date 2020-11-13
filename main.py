import pygame

pygame.init()
pygame.mixer.init()

larg, alt = 800, 400
run = True
tela = 0
pygame.mixer.music.load("song.mp3")
pygame.mixer.music.play()


bg = pygame.image.load("blackhole.png")
fonte_ttl = pygame.font.SysFont("roboto", 40)
fonte_txt = pygame.font.SysFont("roboto", 20)
cor_btn = (69, 72, 81)
cor_fonte = (0, 0, 0)
cor_fundo = (228, 187, 151)

win = pygame.display.set_mode((larg, alt))
pygame.display.set_caption("Hello World")


def texto(text, pos, ft=fonte_txt, cor=cor_fonte):
    txt = ft.render(text, 1, cor)
    win.blit(txt, pos)
    pygame.display.update()


def botao(text, pos):
    pygame.draw.rect(win, cor_btn, ((pos[0] - 50, pos[1] - 15), (200, 50)))
    txt = fonte_txt.render(text, 1, cor_fonte)
    win.blit(txt, pos)
    pygame.display.update()


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if tela == 0:
            win.blit(bg, (0, 0))
            texto("<Hello World/>", (50, 20), fonte_ttl, (255, 255, 255))
            botao("PLAY", (600, 65))
            botao("HOW TO PLAY", (600, 140))
            botao("SETTINGS", (600, 215))
            botao("QUIT", (600, 300))
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 550 <= mouse_pos[0] <= 750 and 50 <= mouse_pos[1] <= 100:
                    tela = 1
                if 550 <= mouse_pos[0] <= 750 and 125 <= mouse_pos[1] <= 175:
                    tela = 2
                if 550 <= mouse_pos[0] <= 750 and 200 <= mouse_pos[1] <= 250:
                    tela = 3
                if 550 <= mouse_pos[0] <= 750 and 275 <= mouse_pos[1] <= 325:
                    tela = 4
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
            botao("VOLTAR", (100, 320))
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 50 <= mouse_pos[0] <= 250 and 300 <= mouse_pos[1] <= 350:
                    tela = 0
        if tela == 3:
            win.fill(cor_fundo)
            texto("CONFIGURAÇÕES", (50, 20), fonte_ttl)
            botao("Desligar Música", (575, 65))
            botao("Ligar Música", (575, 140))
            botao("VOLTAR", (120, 340))
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 50 <= mouse_pos[0] <= 250 and 325 <= mouse_pos[1] <= 375:
                    tela = 0
                if 550 <= mouse_pos[0] <= 750 and 125 <= mouse_pos[1] <= 175:
                    pygame.mixer.music.play()
                if 550 <= mouse_pos[0] <= 750 and 50 <= mouse_pos[1] <= 100:
                    pygame.mixer.music.stop()

            # SETTINGS
        if tela == 4:
            pygame.time.delay(500)
            run = False
            # QUIT

    pygame.display.update()


pygame.quit()