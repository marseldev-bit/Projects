import pygame
from pygame.sprite import Sprite

class alienBullet(Sprite):
    def __init__(self, aiGame):
        super().__init__()
        self.game = aiGame
        self.screen = self.game.screen
        self.set = self.game.set
        self.color = self.set.alienBullet_color

        self.rect = pygame.Rect(0, 0, self.set.bullet_width, self.set.bullet_height)

    def update(self):
        self.rect.y += self.set.bullet_speed 
    
    def showAlienBullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def setPos(self, bottom, centerx):
        self.rect.bottom = bottom
        self.rect.centerx = centerx