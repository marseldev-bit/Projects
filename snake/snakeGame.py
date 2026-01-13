# Импорт библиотек
import sys
import random
import pygame
from pygame.sprite import Sprite

# Классы
class Head:
    def __init__(self, screen):
        self.screen = screen
        self.head = pygame.image.load('image\head.bmp')
        self.headRect = self.head.get_rect()
        self.headRect.top = 300
        self.headRect.left = 480

    def showHead(self):
        self.screen.blit(self.head, self.headRect)
    
class Body(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.body = pygame.image.load('image\\body.bmp')
        self.bodyRect = self.body.get_rect()
        self.bodyRect.top = 360
        self.bodyRect.left = 480

    def update(self):
        self.screen.blit(self.body, self.bodyRect)

class Berry:
    def __init__(self, screen):
        self.screen = screen
        self.berry = pygame.image.load('image\\berry.bmp')
        self.berryRect = self.berry.get_rect()
        self.isBerry = False
    
    def createBerry(self):
        self.berryRect.left = random.randrange(0, 1200, 60)
        self.berryRect.top = random.randrange(0, 840, 60)

    def showBerry(self):
        self.screen.blit(self.berry, self.berryRect)

# Функции
def key(symb, temp):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q: sys.exit()
            elif event.key == pygame.K_RIGHT and temp != 'l':
                return 'r'
            elif event.key == pygame.K_LEFT and temp != 'r':
                return 'l'
            elif event.key == pygame.K_UP and temp != 'd':
                return 'u'
            elif event.key == pygame.K_DOWN and temp != 'u':
                return 'd'
    return symb

def rotate(image, symb, temp):
    if temp == 'r':
        if symb == 'u':
            return pygame.transform.rotate(image, -270)
        elif symb == 'd':
            return pygame.transform.rotate(image, -90)
    elif temp == 'l':
        if symb == 'u':
            return pygame.transform.rotate(image, -90)
        elif symb == 'd':
            return pygame.transform.rotate(image, 90)
    elif temp == 'u':
        if symb == 'r':
            return pygame.transform.rotate(image, 270)
        elif symb == 'l':
            return pygame.transform.rotate(image, 90)
    elif temp == 'd':
        if symb == 'r':
            return pygame.transform.rotate(image, 90)
        elif symb == 'l':
            return pygame.transform.rotate(image, -90)
    return image

def move(object, symb):
    if symb == 'r': object.left += 60
    elif symb == 'l': object.left -= 60
    elif symb == 'u': object.top -= 60
    elif symb == 'd': object.top += 60

def moveBody(object, top, left):
    object.top = top
    object.left = left

def show(screen, map, mapRect, head, body, berry, isberry):
    screen.blit(map, mapRect)
    head.showHead()
    body.update()
    if isberry: berry.showBerry()
    pygame.display.flip()


# Игра
time = pygame.time.Clock()
screen = pygame.display.set_mode((1200, 840))
head = Head(screen)
body = pygame.sprite.Group()
body.add(Body(screen))
berry = Berry(screen)
map = pygame.image.load('image\map.bmp')
mapRect = map.get_rect()
symbol = ''

while True:
    if berry.isBerry == False:
        berry.createBerry()
        berry.isBerry = True

    if symbol == '':
        temp = 'u'
        headTop = 360
        headLeft = 480
    else: 
        temp = symbol
        headTop = head.headRect.top
        headLeft = head.headRect.left

    symbol = key(symbol, temp)

    if symbol != temp:
        head.head = rotate(head.head, symbol, temp)

    move(head.headRect, symbol)

    if head.headRect.left < 0: head.headRect.left = 1140
    elif head.headRect.right > 1200: head.headRect.right = 60
    elif head.headRect.top < 0: head.headRect.top = 780
    elif head.headRect.bottom > 840: head.headRect.bottom = 60

    if head.headRect.left == berry.berryRect.left and head.headRect.top == berry.berryRect.top:
        body.add(Body(screen))
        berry.isBerry = False
    
    currentTop = 0
    currentLeft = 0
    countSprite = 0
    for sprite in body:
        if head.headRect.left == sprite.bodyRect.left and head.headRect.top == sprite.bodyRect.top: sys.exit()
        top = currentTop
        left = currentLeft
        currentTop = sprite.bodyRect.top
        currentLeft = sprite.bodyRect.left

        if countSprite == 0:
            moveBody(sprite.bodyRect, headTop, headLeft)
        else:
            moveBody(sprite.bodyRect, top, left)
        countSprite += 1

    show(screen, map, mapRect, head, body, berry, berry.isBerry)
    time.tick(3)
            
        