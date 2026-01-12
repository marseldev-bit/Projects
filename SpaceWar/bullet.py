import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, aiGame):
        super().__init__()
        self.screen = aiGame.screen
        self.set = aiGame.set
        self.color = self.set.bullet_color

        self.rect = pygame.Rect(0, 0, self.set.bullet_width, self.set.bullet_height)
        self.rect.midtop = aiGame.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.set.bullet_speed
        self.rect.y = self.y
    
    def showBullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)