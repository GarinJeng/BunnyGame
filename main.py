import pygame
from pygame.locals import *
import os
import sys
import math
import random
from pygame.locals import (
    RLEACCEL,
    K_w,
    K_a,
    K_s,
    K_d,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_g,
    K_l,
    KEYDOWN,
    QUIT
)

global m
global pros
global TFloor
global Mup
global TFloor2
global Mup2
pros = pygame.sprite.Group()
Mup = 0
TFloor = False
Mup2 = 0
TFloor2 = False
m = 1
pygame.init()
button_list = []


class Obstacles(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super(Obstacles, self).__init__()
        self.surf = pygame.Surface((w, h))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect(x=x, y=y)

    def getTop(self):
        return self.rect.top

class lives(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(lives, self).__init__()
        self.surf = pygame.image.load("PLayer/LiveIcon.png")
        self.rect = self.surf.get_rect(x=x, y=y)
class pro(pygame.sprite.Sprite):
    def __init__(self, f, x1, y1, s):
        self.s = s
        self.f = f
        super(pro, self).__init__()
        self.surf = pygame.image.load("PLayer/pro1.png")
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(x=x1, y=y1)
        if self.f == 1:
            self.rect.move_ip(s, 0)
        else:
            self.rect.move_ip(-s, 0)

    def facing(self):
        if self.f == 1:
            self.surf = pygame.transform.flip(self.surf, True, True)

    def update(self):
        if self.f == 1:
            # self.surf = pygame.transform.flip(self.surf, True, True)
            self.rect.move_ip(self.s, 0)
        else:
            self.rect.move_ip(-self.s, 0)

    def SetS(self, s):
        self.s = s


class Player(pygame.sprite.Sprite):
    # Run = [pygame.image.load(os.path.join('PLayer/Run/', "R" + str(x) + '.png')) for x in range(1, 10)]
    # Jump = [pygame.image.load(os.path.join('PLayer/Jump/', "J" + str(x) + '.png')) for x in range(1, 19)]
    def __init__(self, n):
        self.Shoot = [pygame.image.load(os.path.join('PLayer/Shoot/', "S" + str(x) + '.png')) for x in range(1, 7)]
        self.Death = [pygame.image.load(os.path.join('PLayer/Death/', "D" + str(x) + '.png')) for x in range(1, 6)]
        self.Run = [pygame.image.load(os.path.join('PLayer/Run/', "R" + str(x) + '.png')) for x in range(1, 11)]
        self.Jump = [pygame.image.load(os.path.join('PLayer/Jump/', "J" + str(x) + '.png')) for x in range(1, 11)]
        #print(self.Shoot)
        self.num = n
        self.lives = 3
        self.f1 = 1
        self.f2 = 2
        super(Player, self).__init__()
        self.surf = pygame.image.load("PLayer/Idle.png")
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(x=300 * self.num, y=20)
        self.B = pro(self.f1, -100, -100, 10)
        pros.add(self.B)
        self.c = 100
        self.c2 = 0
        self.action = 0
        self.c3 = 0
        self.re = 0
        self.c5 = 0
        self.c8 = 0
        self.c6 = 0
        self.c7 = 0
        self.p = 1
        self.livess = []
    def showLives(self,pla):
        self.livess = []
        #print(self.livess)
        if pla == 1:
            for x in range(0,self.lives):
                t = lives(50+(39*x),50)
                self.livess.append(t)
        if pla == 2:
            for x in range(0,self.lives):
                t = lives(1450-(39*x),50)
                self.livess.append(t)
        #print(self.livess)
    def getTop(self):
        return self.rect.top

    def death(self):
        self.c8 = 15

    def death2(self):
        self.lives = self.lives - 1
        if (self.lives < 0):
            global m
            m = 1
        else:
            self.rect = self.surf.get_rect(x=300 * self.num, y=20)

    def spawn(self):
        self.rect = self.surf.get_rect(x=300 * self.num, y=20)

    def anamate(self):
        if self.c3 < 2:
            self.c3 += 1
        else:
            self.c3 = 0
            if self.action == 0:
                self.surf = pygame.image.load("PLayer/Idle.PNG")
            if self.action == 1:
                # print(self.c2)
                if self.c2 < 2:
                    self.c2 = self.c2 + 1
                else:
                    self.c2 = 2
                # print(self.c2)
                self.surf = self.Shoot[self.c2]
            if self.action == 2:
                if self.c2 < 5:
                    # print(str(self.c2) + "end")
                    self.c2 = self.c2 + 1
                    self.surf = self.Shoot[self.c2]
                else:
                    # print(str(self.c2) + "end")
                    self.c2 = 0
                    self.c3 = 0
            if self.action == 3:
                if self.c6 < 9:
                    self.c6 = self.c6 + 1
                    self.surf = self.Run[self.c6]
                else:
                    self.c6 = 0
            if self.action == 4:
                if Mup > 0:
                    if self.c7 < 5:
                        self.c7 = self.c7 + 1
                        self.surf = self.Jump[self.c7]
                    else:
                        self.c7 = 5
                        self.surf = self.Jump[self.c7]
                if Mup < 0:
                    if self.c7 < 9:
                        self.c7 = self.c7 + 1
                        self.surf = self.Jump[self.c7]
                    else:
                        self.c7 = 9
                        self.surf = self.Jump[self.c7]
            if self.action == 5:
                if self.c5 < 4:
                    self.c5 = self.c5 + 1
                    self.surf = self.Death[self.c5]
                else:
                    self.death2()
            if self.action == 6:
                if Mup2 > 0:
                    if self.c7 < 5:
                        self.c7 = self.c7 + 1
                        self.surf = self.Jump[self.c7]
                    else:
                        self.c7 = 5
                        self.surf = self.Jump[self.c7]
                if Mup2 < 0:
                    if self.c7 < 9:
                        self.c7 = self.c7 + 1
                        self.surf = self.Jump[self.c7]
                    else:
                        self.c7 = 9
                        self.surf = self.Jump[self.c7]
            if self.action == 7:
                self.surf = self.Death[3]
            if self.f1 == 1:
                self.surf = pygame.transform.flip(self.surf, True, False)

    def update(self, pressed_keys):
        global Mup
        # print(self.lives)
        self.action = 0
        keys = pygame.key.get_pressed()
        if self.c8 > 0:
            self.c8 -= 1
            self.action = 5
            self.anamate()
            board.blit(self.B.surf, self.B.rect)
            self.B.update()
            pros.add(self.B)
            self.rect = self.surf.get_rect(x=self.rect.x, y=self.rect.y)
            return
        else:
            self.c5 = 0
        if keys[pygame.K_w] and TFloor:
            self.action = 4
            self.rect.move_ip(0, -5)
            Mup = -20
        if keys[pygame.K_s] and not TFloor:
            self.rect.move_ip(0, 5)
        if keys[pygame.K_a]:
            self.action = 3
            self.f1 = 2
            self.rect.move_ip(-5, 0)
        if keys[pygame.K_d]:
            self.action = 3
            self.f1 = 1
            self.rect.move_ip(5, 0)
        if not TFloor:
            self.action = 4
        if keys[pygame.K_s] and TFloor:
            self.action = 7
        if keys[pygame.K_g]:
            self.B = pro(self.f1, self.rect.centerx - 15, self.rect.centery, 10)
            self.action = 1
            if self.c > 0:
                self.c = self.c - 1
            self.B.SetS((70 - (50 * (self.c / 100))))
        else:
            if self.c != 100:
                self.re = 12
                self.action = 2
            if self.re > 0:
                self.re -= 1
                self.action = 2
            self.c = 100
        if self.rect.left < 0:
            self.death()
        if self.rect.right > 1500:
            self.death()
        if self.rect.top <= 0:
            self.death()
        if self.rect.bottom >= 800:
            self.death()
        # self.B.SetS(20)
        self.anamate()
        self.showLives(1)
        for x in self.livess:
            board.blit(x.surf, x.rect)
        self.B.facing()
        board.blit(self.B.surf, self.B.rect)
        self.B.update()
        pros.add(self.B)
        self.rect = self.surf.get_rect(x=self.rect.x, y=self.rect.y)

    def update2(self, pressed_keys):
        global Mup2
        # print(self.lives)
        self.action = 0
        keys = pygame.key.get_pressed()
        if self.c8 > 0:
            self.c8 -= 1
            self.action = 5
            self.anamate()
            board.blit(self.B.surf, self.B.rect)
            self.B.update()
            pros.add(self.B)
            self.rect = self.surf.get_rect(x=self.rect.x, y=self.rect.y)
            return
        else:
            self.c5 = 0
        if keys[pygame.K_UP] and TFloor2:
            self.action = 6
            self.rect.move_ip(0, -5)
            Mup2 = -20
        if keys[pygame.K_DOWN] and not TFloor2:
            self.rect.move_ip(0, 5)
        if keys[pygame.K_LEFT]:
            self.action = 3
            self.f1 = 2
            self.rect.move_ip(-5, 0)
        if keys[pygame.K_RIGHT]:
            self.action = 3
            self.f1 = 1
            self.rect.move_ip(5, 0)
        if not TFloor2:
            self.action = 6
        if keys[pygame.K_DOWN] and TFloor2:
            self.action = 7
        if keys[pygame.K_l]:
            self.B = pro(self.f1, self.rect.centerx - 15, self.rect.centery, 10)
            self.action = 1
            if self.c > 0:
                self.c = self.c - 1
            self.B.SetS((70 - (50 * (self.c / 100))))
        else:
            self.p = 1
            if self.c != 100:
                self.re = 12
                self.action = 2
            if self.re > 0:
                self.re -= 1
                self.action = 2
            self.c = 100
        if self.rect.left < 0:
            self.death()
        if self.rect.right > 1500:
            self.death()
        if self.rect.top <= 0:
            self.death()
        if self.rect.bottom >= 800:
            self.death()
        # self.B.SetS(20)
        self.anamate()
        self.showLives(2)
        for x in self.livess:
            board.blit(x.surf, x.rect)
        self.B.facing()
        board.blit(self.B.surf, self.B.rect)
        self.B.update()
        pros.add(self.B)
        self.rect = self.surf.get_rect(x=self.rect.x, y=self.rect.y)


def quit():
    pygame.quit()


# button class writen by Girish Hegde
# https://stackoverflow.com/questions/63435298/how-to-create-a-button-class-in-pygame
class button:
    def __init__(self, position, size, clr=[100, 100, 100], cngclr=None, func=None, text='', font="Segoe Print",
                 font_size=16, font_clr=[0, 0, 0]):
        self.clr = clr
        self.size = size
        self.func = func
        self.surf = pygame.Surface(size)
        self.rect = self.surf.get_rect(center=position)

        if cngclr:
            self.cngclr = cngclr
        else:
            self.cngclr = clr

        if len(clr) == 4:
            self.surf.set_alpha(clr[3])

        self.font = pygame.font.SysFont(font, font_size)
        self.txt = text
        self.font_clr = font_clr
        self.txt_surf = self.font.render(self.txt, 1, self.font_clr)
        self.txt_rect = self.txt_surf.get_rect(center=[wh // 2 for wh in self.size])

    def draw(self, screen):
        self.mouseover()

        self.surf.fill(self.curclr)
        self.surf.blit(self.txt_surf, self.txt_rect)
        screen.blit(self.surf, self.rect)

    def mouseover(self):
        self.curclr = self.clr
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.curclr = self.cngclr

    def call_back(self, *args):
        if self.func:
            return self.func(*args)


def Tm():
    global m
    m = 1


def Fm():
    global m
    m = 0


def rectangle(x, y):
    pygame.draw.rect(board, (255, 255, 255), (x, y, 50, 50))


def game():
    pros = None
    button_list.clear()
    GB()
    global m
    m = 2


def GB():
    pygame.draw.rect(board, (255, 255, 255), (0, 0, 1500, 800))
    board.blit(bg, (-450, 0))


def Rules():
    Fm()
    pygame.draw.rect(board, (255, 255, 255), (450, 100, 600, 600))
    button_list.clear()
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Rules', True, pygame.Color("black"))
    textRect = text.get_rect()
    textRect.center = (750, 150)
    font = pygame.font.Font('freesansbold.ttf', 10)
    text1 = font.render('this is a 2 player game where you are both bunnys that shoot carets at eachother. player 1 uses ASWD to move and G to shoot.', True, pygame.Color("black"))
    text2 = font.render('player 2 uses arrow keys to move and L to shoot you have 5 lives and by holding the shoot button you charge your shot making it faster.',True, pygame.Color("black"))
    text3 = font.render('lives are displayed in the top corners.',True, pygame.Color("black"))
    textRect1 = text.get_rect()
    textRect1.center = (450, 200)
    textRect2 = text.get_rect()
    textRect2.center = (450, 220)
    textRect3 = text.get_rect()
    textRect3.center = (450, 240)
    board.blit(text, textRect)
    board.blit(text1, textRect1)
    board.blit(text2, textRect2)
    board.blit(text3, textRect3)
    button1 = button((750, 580), (100, 50), (220, 220, 220), (200, 200, 200), Tm, 'Back')
    button_list.append(button1)


def menu():
    button_list.clear()
    player.lives = 4
    player2.lives = 4
    player.spawn()
    player2.spawn()
    pygame.draw.rect(board, (255, 255, 255), (350, 0, 800, 800))
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('The Game', True, pygame.Color("black"))
    textRect = text.get_rect()
    textRect.center = (750, 200)
    board.blit(text, textRect)
    button1 = button((750, 300), (100, 50), (220, 220, 220), (200, 200, 200), game, 'Start')
    button2 = button((750, 360), (100, 50), (220, 220, 220), (200, 200, 200), Rules, 'Rules')
    button4 = button((750, 420), (100, 50), (220, 220, 220), (200, 200, 200), quit, 'Quit')
    button_list.append(button1)
    button_list.append(button2)
    button_list.append(button4)


bg = pygame.image.load("PLayer/bG.jpeg")
board = pygame.display.set_mode((1500, 800))
board.fill(pygame.Color("white"))
pygame.mouse.set_cursor(pygame.cursors.broken_x)
player = Player(1)
player2 = Player(4)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(player2)
Obsticls = pygame.sprite.Group()
# obsticl1 = obsticls(0,550,600,50)
all_sprites.remove(Obsticls)
Obsticls.add(Obstacles(100, 400, 400, 50))
Obsticls.add(Obstacles(1000, 400, 400, 50))
for x in range(0, random.randint(1, 11)):
    Obsticls.add(Obstacles(random.randint(50, 1450), random.randint(100, 700), random.randint(10, 800),random.randint(50, 400)))
for x in range(0, random.randint(1, 11)):
    Obsticls.add(Obstacles(random.randint(50, 1450), random.randint(100, 700), random.randint(10, 70),random.randint(50, 70)))
all_sprites.add(Obsticls)
all_sprites.add(pros)
menu()
while True:
    clock = pygame.time.Clock()
    clock.tick(30)
    if m == 1:
        menu()
    if m == 2:
        GB()
        pros = pygame.sprite.Group()
        player.update(pressed_keys)
        player2.update2(pressed_keys)
        player.rect.move_ip(0, 5)
        player2.rect.move_ip(0, 5)
        Obsticls.update()
        if not TFloor:
            Mup += 1
            # print(Mup)
            player.rect.move_ip(0, Mup)
        if TFloor and Mup > -15:
            Mup = 0
        if not TFloor2:
            Mup2 += 1
            player2.rect.move_ip(0, Mup2)
        if TFloor2 and Mup2 > 0:
            Mup2 = 0
        player.rect.scale_by(1, 1)
        board.blit(player.surf, player.rect)
        board.blit(player2.surf, player2.rect)
        for ls in all_sprites:
            board.blit(ls.surf, ls.rect)
        TFloor = False
        TFloor2 = False
        # for pr in pros:
        # print(pr.rect)
        if pygame.sprite.spritecollideany(player, pros):
            player.death()
        if pygame.sprite.spritecollideany(player2, pros):
            # print("hit")
            player2.death()
        u = 0
        while pygame.sprite.spritecollideany(player, Obsticls):
            if u > 1000:
                player.spawn()
                u=0
            u+=1
            TFloor = True
            for ob in Obsticls:
                O = pygame.sprite.Group()
                O.add(ob)
                if pygame.sprite.spritecollideany(player, O) and player.getTop() < ob.getTop():
                    player.rect.move_ip(0, -2)
                elif (pygame.sprite.spritecollideany(player, O)):
                    z = 1
                    while pygame.sprite.spritecollideany(player, O):
                        player.rect.move_ip(5 * z, 0)
                        if pygame.sprite.spritecollideany(player, O):
                            player.rect.move_ip(-10 * z, 0)
                        if pygame.sprite.spritecollideany(player, O):
                            player.rect.move_ip(5 * z, 0)
                        if pygame.sprite.spritecollideany(player, O):
                            player.rect.move_ip(0, 2*z)
                        if pygame.sprite.spritecollideany(player, O):
                            player.rect.move_ip(0, -2 * z)
                        if z > 10:
                            player.death()
                        if z >15:
                            break
                        z += 1
            player.rect.move_ip(0, 1)
        y = 0
        while pygame.sprite.spritecollideany(player2, Obsticls):
            if y > 1000:
                player2.spawn()
                y=0
            y+=1
            TFloor2 = True
            for ob in Obsticls:
                O = pygame.sprite.Group()
                O.add(ob)
                if pygame.sprite.spritecollideany(player2, O) and player2.getTop() < ob.getTop():
                    player2.rect.move_ip(0, -2)
                elif (pygame.sprite.spritecollideany(player2, O)):
                    z = 1
                    while pygame.sprite.spritecollideany(player2, O):
                        player2.rect.move_ip(5 * z, 0)
                        if pygame.sprite.spritecollideany(player2, O):
                            player2.rect.move_ip(-10 * z, 0)
                        if pygame.sprite.spritecollideany(player2, O):
                            player2.rect.move_ip(5 * z, 0)
                        if pygame.sprite.spritecollideany(player2, O):
                            player2.rect.move_ip(0, 2 * z)
                        if pygame.sprite.spritecollideany(player2, O):
                            player2.rect.move_ip(0, -2 * z)
                        if z > 15:
                            break
                        z += 1
            player2.rect.move_ip(0, 1)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                for b in button_list:
                    if b.rect.collidepoint(pos):
                        b.call_back()
        pressed_keys = pygame.key.get_pressed()
        if m == 2:
            pass
    for b in button_list:
        b.draw(board)
    pygame.display.update()
