# Импорт библиотек
import sys
import pygame
from pygame.sprite import Sprite
from time import sleep


# Создание классов
class Field(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.screenRect = self.screen.get_rect()
        self.rect = pygame.Rect(0, 0, 300, 300)
        self.color1 = (0, 126, 167)
        self.color2 = (0, 50, 73)
        self.value = ''
        self.number = 0
    
    def setValue(self, symbol):
        self.value = symbol

    def update(self):
        if self.number % 2 == 0:
            pygame.draw.rect(self.screen, self.color1, self.rect)
        else:
            pygame.draw.rect(self.screen, self.color2, self.rect)

class X(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen 
        self.image = pygame.image.load('image\\x.bmp')
        self.rect = self.image.get_rect()
    
    def setPos(self, field):
        self.rect.center = field.center
    
    def update(self):
        self.screen.blit(self.image, self.rect)

class O(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen 
        self.image = pygame.image.load('image\\o.bmp')
        self.rect = self.image.get_rect()

    def setPos(self, field):
        self.rect.center = field.center

    def update(self):
        self.screen.blit(self.image, self.rect)

class Symb:
    def __init__(self):
        self.symb = 1
    
    def changeSymb(self):
        self.symb *= -1

# Функции
def checkEvent(symb, xGroup, oGroup, screen, fields):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q: sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            addSymbol(symb.symb, xGroup, oGroup, screen, pygame.mouse.get_pos(), fields)
            symb.changeSymb()

def updateScreen(screen, fields, xGroup, oGroup):
    fields.update()
    xGroup.update()
    oGroup.update()
    pygame.display.flip()

def setMap(fields):
    left = 0
    top = 0
    num = 1
    for field in fields.sprites():
        if num == 4:
            top = 300
            left = 0
        elif num == 7:
            top = 600
            left = 0
        field.number += num
        field.rect.left = left
        field.rect.top = top
        num += 1
        left += 300


def createMap(fields, screen):
    for i in range(9):
        fields.add(Field(screen))
    setMap(fields)

def addSymbol(symb, xGroup, oGroup, screen, pos, fields):
    if symb > 0:
        newX = X(screen)
        newX.rect.center = setCursorPos(pos, fields, 'x')
        if newX.rect.centerx:
            xGroup.add(newX)
    else:
        newO = O(screen)
        newO.rect.center = setCursorPos(pos, fields, 'o')
        if newO.rect.centerx:
            oGroup.add(newO)


def setCursorPos(mouse, fields, symb):
    x, y = mouse
    for field in fields:
        if field.rect.top <= y and field.rect.bottom >= y and field.rect.left <= x and field.rect.right >= x:
            if not field.value:
                field.value = symb
                return field.rect.center
            else: return (0, 0)

def checkWin(fields):
    triple = []
    num = 0
    for field in fields.sprites():
        triple.append(field)
    if triple:
        while num < 9:
            if triple[num].value == triple[num+1].value and triple[num].value == triple[num+2].value and triple[num+1].value == triple[num+2].value and triple[num].value:
                return True
            num += 3
        num = 0

        while num < 3:
            if triple[num].value == triple[num+3].value and triple[num].value == triple[num+6].value and triple[num+3].value == triple[num+6].value and triple[num].value:
                return True
            num += 1
        num = 0
        temp = 4

        while num < 3:
            if triple[num].value == triple[num+temp].value and triple[num].value == triple[num+temp*2].value and triple[num+temp].value == triple[num+temp*2].value and triple[num].value:
                return True
            num += 2
            temp -= 2
    
def checkDraw(fields):
    for field in fields.sprites():
        if not field.value: return False
    else: return True

def emptyMap(oGroup, xGroup, isDraw):
    if isDraw:
        xGroup.empty()
        oGroup.empty()


# Игра
screen = pygame.display.set_mode((900, 900))
fields = pygame.sprite.Group()
xGroup = pygame.sprite.Group()
oGroup = pygame.sprite.Group()
currentSymb = Symb()

while True:
    if not fields:
        createMap(fields, screen)
    checkEvent(currentSymb, xGroup, oGroup, screen, fields)
    if checkWin(fields):
        sys.exit()
    emptyMap(oGroup, xGroup, checkDraw(fields))
    updateScreen(screen, fields, xGroup, oGroup)
