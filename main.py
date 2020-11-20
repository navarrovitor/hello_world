import pygame, time
import random as rd

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

larg, alt = 800, 400
run = True
tela = -1
level = 0
play = True
times_bh_appear = rd.randint(1, 4)


pygame.mixer.music.load("resources/song.mp3")
bg = pygame.image.load("resources/blackhole.png")
logo = pygame.image.load("resources/logo_transparent.png")
logo = pygame.transform.scale(logo, (300, 300))

apple = pygame.image.load("resources/apple.png")
apple = pygame.transform.scale(apple, (64, 64))
door = pygame.image.load("resources/door.png")
door = pygame.transform.scale(door, (64, 64))
banana = pygame.image.load("resources/banana.png")
banana = pygame.transform.scale(banana, (64, 64))
leaf = pygame.image.load("resources/leaf.png")
leaf = pygame.transform.scale(leaf, (64, 64))
rose = pygame.image.load("resources/rose.png")
rose = pygame.transform.scale(rose, (64, 64))
star = pygame.image.load("resources/star.png")
star = pygame.transform.scale(star, (64, 64))
tree = pygame.image.load("resources/tree.png")
tree = pygame.transform.scale(tree, (64, 64))
bh = pygame.image.load("resources/blackhole_prop.png")
bh = pygame.transform.scale(bh, (64, 64))


# SPRITES
walkLeft_hero = [
    pygame.image.load("resources/character/L1.png"),
    pygame.image.load("resources/character/L2.png"),
    pygame.image.load("resources/character/L3.png"),
    pygame.image.load("resources/character/L4.png"),
    pygame.image.load("resources/character/L5.png"),
    pygame.image.load("resources/character/L6.png"),
    pygame.image.load("resources/character/L7.png"),
    pygame.image.load("resources/character/L8.png"),
    pygame.image.load("resources/character/L9.png"),
]
walkRight_hero = [
    pygame.image.load("resources/character/R1.png"),
    pygame.image.load("resources/character/R2.png"),
    pygame.image.load("resources/character/R3.png"),
    pygame.image.load("resources/character/R4.png"),
    pygame.image.load("resources/character/R5.png"),
    pygame.image.load("resources/character/R6.png"),
    pygame.image.load("resources/character/R7.png"),
    pygame.image.load("resources/character/R8.png"),
    pygame.image.load("resources/character/R9.png"),
]
walkLeft_not_hero = [
    pygame.image.load("resources/character/L1E.png"),
    pygame.image.load("resources/character/L2E.png"),
    pygame.image.load("resources/character/L3E.png"),
    pygame.image.load("resources/character/L4E.png"),
    pygame.image.load("resources/character/L5E.png"),
    pygame.image.load("resources/character/L6E.png"),
    pygame.image.load("resources/character/L7E.png"),
    pygame.image.load("resources/character/L8E.png"),
    pygame.image.load("resources/character/L9E.png"),
]
walkRight_not_hero = [
    pygame.image.load("resources/character/R1E.png"),
    pygame.image.load("resources/character/R2E.png"),
    pygame.image.load("resources/character/R3E.png"),
    pygame.image.load("resources/character/R4E.png"),
    pygame.image.load("resources/character/R5E.png"),
    pygame.image.load("resources/character/R6E.png"),
    pygame.image.load("resources/character/R7E.png"),
    pygame.image.load("resources/character/R8E.png"),
    pygame.image.load("resources/character/R9E.png"),
]

# FONTES
fonte_ttl = pygame.font.SysFont("roboto", 40)
fonte_txt = pygame.font.SysFont("roboto", 20)

# logo do início do jogo
ret_logo = logo.get_rect()
vel_logo = [1, 1]

# cores
cor_btn = (47, 47, 47)
cor_btn_clicked = (20, 20, 20)
cor_fundo = (228, 187, 151)
black = (0, 0, 0)
white = (214, 214, 177)

# setup do display
win = pygame.display.set_mode((larg, alt))
pygame.display.set_caption("Hello World")

### FUNÇÕES E CLASSES
def texto(text, pos, ft=fonte_txt, cor=black):
    txt = ft.render(text, 1, cor)
    win.blit(txt, pos)


class prop:
    def __init__(self, img, x, y):
        self.img, self.x, self.y = img, x, y
        self.rect = img.get_rect(topleft=(self.x, self.y))
        self.count = 0

    def draw(self, win=win):
        win.blit(self.img, (self.x, self.y))
        ###
        # pygame.draw.rect(win, black, self.rect, 0)
        ###

    def collision(self, x):
        if x > self.x and x < self.x + self.rect[2]:
            return True
        return False


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
        texto = fonte_txt.render(self.txt, 1, white)
        win.blit(
            texto,
            (
                self.x + (self.width / 2 - texto.get_width() / 2),
                self.y + (self.height / 2 - texto.get_height() / 2),
            ),
        )

    def isClicked(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False


class boneco:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.walkCount = 0
        self.left = False
        self.right = False
        self.standing = True
        self.sprite = True

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.sprite:
            if not self.standing:
                if self.left:
                    win.blit(walkLeft_hero[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    win.blit(walkRight_hero[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
            else:
                if self.right:
                    win.blit(walkRight_hero[0], (self.x, self.y))
                else:
                    win.blit(walkLeft_hero[0], (self.x, self.y))
        else:
            if not self.standing:
                if self.left:
                    win.blit(walkLeft_not_hero[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    win.blit(walkRight_not_hero[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
            else:
                if self.right:
                    win.blit(walkRight_not_hero[0], (self.x, self.y))
                else:
                    win.blit(walkLeft_not_hero[0], (self.x, self.y))


# BOTÕES
# botão para tela do jogo
play_button = button(cor_btn, 550, 50, 200, 50, "JOGAR")
# botão para tela de como jogar
how_to_play_button = button(cor_btn, 550, 125, 200, 50, "COMO JOGAR")
# botão para tela de configurações
settings_button = button(cor_btn, 550, 200, 200, 50, "CONFIGURAÇÕES")
# botão para sair do jogo
quit_button = button(cor_btn, 550, 275, 200, 50, "SAIR")
# botão para ligar ou desligar música
music_button = button(cor_btn, 525, 150, 200, 50, "MÚSICA")
# botão para mudar sprite
sprite_button = button(cor_btn, 525, 225, 200, 50, "HERÓI")
# botão para voltar para a tela inicial
back_button = button(cor_btn, larg / 10, 300, 200, 50, "VOLTAR")

figuras = []
bh = prop(bh, 700, 300)
leaf = prop(leaf, 700, 300)
apple = prop(apple, 700, 300)
banana = prop(banana, 700, 300)
rose = prop(rose, 700, 300)
star = prop(star, 700, 300)
tree = prop(tree, 700, 300)
figuras.append(leaf)
figuras.append(apple)
figuras.append(banana)
figuras.append(rose)
figuras.append(star)
figuras.append(tree)
hero = boneco(50, 300, 64, 64)

start_ticks = pygame.time.get_ticks()
ticks_elapsed = pygame.time.get_ticks()

initial_points = 10
pontuações = []
# pygame.mixer.music.play()
while run:
    clock.tick(60)
    # telas
    if tela == -1:
        win.fill(black)
        win.blit(logo, ret_logo)
        ret_logo = ret_logo.move(vel_logo)
        if ret_logo.left < 0 or ret_logo.right > larg:
            vel_logo[0] = -vel_logo[0]
        if ret_logo.top < 0 or ret_logo.bottom > alt:
            vel_logo[1] = -vel_logo[1]
        texto(
            "pressione qualquer tecla para continuar",
            (larg / 4, 350),
            fonte_txt,
            (47, 47, 47),
        )

    if tela == 0:
        win.blit(bg, (0, 0))
        texto("Hello World", (larg / 10, alt / 8), fonte_ttl, (white))
        play_button.draw()
        how_to_play_button.draw()
        settings_button.draw()
        quit_button.draw()

    if tela == 1:
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000
        time_elapsed = (pygame.time.get_ticks() - ticks_elapsed) / 1000
        win.fill(cor_fundo)
        texto(str(time_elapsed), (larg - 150, alt / 8), fonte_ttl, (black))
        ##
        texto(str(initial_points), (larg - 150, alt / 4), fonte_ttl, (black))
        ##
        if seconds > 2:
            initial_points -= 2
            start_ticks = pygame.time.get_ticks()
        if level == 0:
            texto("O QUE É RECURSIVIDADE?", (larg / 10, alt / 8), fonte_ttl, (black))
            texto("Vá até o buraco negro", (larg / 10, alt / 4), fonte_txt, (black))
            bh.draw()
            if bh.count < times_bh_appear:
                if bh.collision(hero.x):
                    hero.x = 50
                    bh.count += 1
            else:
                bh.img = door
                texto(
                    "para aprender recursividade você precisa primeiro aprender sobre recursividade",
                    (larg / 12, alt / 2),
                    fonte_txt,
                    (black),
                )
                if bh.collision(hero.x):
                    level = 1
                    pontuações.append(initial_points)
                    initial_points = 10
        if level == 1:
            texto("OS ALGORITMOS DE BUSCA", (larg / 10, alt / 8), fonte_ttl, (black))
            texto(
                "busca sequencial (note a velocidade)",
                (larg / 10, alt / 4),
                fonte_txt,
                (black),
            )
            hero.vel = 5
            for i in range(len(figuras)):
                figuras[i].x = larg / (i + 1)
                figuras[i].draw()

        hero.draw(win)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and hero.x > hero.vel:
            hero.x -= hero.vel
            hero.right = False
            hero.left = True
            hero.standing = False
        elif keys[pygame.K_RIGHT] and hero.x + hero.width < larg - hero.vel:
            hero.x += hero.vel
            hero.right = True
            hero.left = False
            hero.standing = False
        else:
            hero.walkCount = 0
            hero.standing = True

    if tela == 2:
        win.fill(cor_fundo)
        texto("COMO JOGAR", (larg / 10, alt / 8), fonte_ttl)
        texto(
            "Faça o boneco andar usando as setas do teclado. Selecione com a tecla de ESPAÇO",
            (larg / 32, alt / 3),
        )
        texto(
            "O objetivo do jogo é passar pelos desafios referentes a programação.",
            (larg / 32, alt / 2),
        )
        back_button.draw()

    if tela == 3:
        win.fill(cor_fundo)
        texto("CONFIGURAÇÕES", (larg / 10, alt / 8), fonte_ttl)
        back_button.draw()
        music_button.draw()
        sprite_button.draw()

    # EVENTOS
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            run = False

        if tela == -1:
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                tela = 0

        elif tela == 0:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.isClicked(pos):
                    tela = 1
                if how_to_play_button.isClicked(pos):
                    tela = 2
                if settings_button.isClicked(pos):
                    tela = 3
                if quit_button.isClicked(pos):
                    pygame.time.delay(500)
                    run = False

        elif tela == 1:
            pass
            # PLAY

        elif tela == 2:
            # como jogar
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.isClicked(pos):
                    tela = 0

        elif tela == 3:
            # SETTINGS
            if event.type == pygame.MOUSEBUTTONDOWN:
                # MÚSICA LIGADA
                if music_button.isClicked(pos):
                    music_button.clicked = not music_button.clicked
                    play = not play
                    if play:
                        pygame.mixer.music.play()
                    else:
                        pygame.mixer.music.stop()
                if sprite_button.isClicked(pos):
                    sprite_button.clicked = not sprite_button.clicked
                    if sprite_button.clicked:
                        sprite_button.txt = "GOBLIN"
                    else:
                        sprite_button.txt = "HERÓI"
                    hero.sprite = not hero.sprite
                if back_button.isClicked(pos):
                    tela = 0

    pygame.display.update()

print(pontuações)
pygame.quit()