from pygame.sprite import Sprite
import pygame

class Snake(Sprite):
    def __init__(self, game):
        super().__init__()
        self.head = pygame.image.load('image\head.bmp')
        self.tale = pygame.image.load('image\\tale.bmp')
        self.bodyType = pygame.Rect(0, 0, 60, 60)
        self.headRect = self.head.get_rect()
        self.taleRect = self.tale.get_rect()
        # self.body = pygame.sprite.Group()
        # self.body.add(self.bodyType)

        self.screen = game.screen
        self.screenRect = game.screen.get_rect()
        self.headRect.right = 540
        self.bodyType.right = 540
        self.taleRect.right = 540
        self.headRect.top = 300
        self.bodyType.top = 360
        self.taleRect.top = 420

        self.speed = 6
        self.angle = 0


    def runHead(self, symb):
        if symb == 'r':
            self.headRect.x += self.speed
        elif symb == 'l':
            self.headRect.x -= self.speed
        elif symb == 'u':
            self.headRect.y -= self.speed
        elif symb == 'd':
            self.headRect.y += self.speed

    def runTale(self, symb):
        if symb == 'r':
            self.taleRect.x += self.speed
        elif symb == 'l':
             self.taleRect.x -= self.speed
        elif symb == 'u':
             self.taleRect.y -= self.speed
        elif symb == 'd':
             self.taleRect.y += self.speed

    def rotateHead(self, symb):
        if symb == 'r':
            if self.angle < 270:
                self.head = pygame.transform.rotate(self.head, 270 - self.angle)
                self.angle = 270
        elif symb == 'l':
            if self.angle < 90:
                self.head = pygame.transform.rotate(self.head, 90 - self.angle)
                self.angle = 90
            elif self.angle > 90:
                self.head = pygame.transform.rotate(self.head, 90 - self.angle)
                self.angle = 90
        elif symb == 'u':
            if self.angle > 0:
                self.head = pygame.transform.rotate(self.head, self.angle*(-1))
                self.angle = 0
        elif symb == 'd':
            if self.angle < 180:
                self.head = pygame.transform.rotate(self.head, 180 - self.angle)
                self.angle = 180
            elif self.angle > 180:
                self.head = pygame.transform.rotate(self.head, 180 - self.angle)
                self.angle = 180
        
    def rotateTale(self, symb):
        if symb == 'r':
            if self.angle < 270:
                self.tale = pygame.transform.rotate(self.tale, 270 - self.angle)
                self.angle = 270
        elif symb == 'l':
            if self.angle < 90:
                self.tale = pygame.transform.rotate(self.tale, 90 - self.angle)
                self.angle = 90
            elif self.angle > 90:
                self.tale = pygame.transform.rotate(self.tale, 90 - self.angle)
                self.angle = 90
        elif symb == 'u':
            if self.angle > 0:
                self.tale = pygame.transform.rotate(self.tale, self.angle*(-1))
                self.angle = 0
        elif symb == 'd':
            if self.angle < 180:
                self.tale = pygame.transform.rotate(self.tale, 180 - self.angle)
                self.angle = 180
            elif self.angle > 180:
                self.tale = pygame.transform.rotate(self.tale, 180 - self.angle)
                self.angle = 180

    
    def draw(self):
        self.screen.blit(self.head, self.headRect)
        # pygame.draw.rect(self.screen, (35, 206, 107), self.bodyType)
        # self.screen.blit(self.tale, self.taleRect)