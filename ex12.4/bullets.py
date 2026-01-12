import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, game):
        super().__init__()
        self.speed = 5
        self.width = 15
        self.height = 3
        self.color = (242, 221, 110)
        self.screen = game.screen
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midright = game.model.rect.midright

    def shoot(self):
        self.rect.x += self.speed
    
    def drawBullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
