import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, aiGame):
        super().__init__()
        self.screen = aiGame.screen
        self.screenRect = self.screen.get_rect()
        self.set = aiGame.set

        self.image = pygame.image.load('images\\alien.bmp')
        self.rect = self.image.get_rect()
        self.x = 40
        self.y = 50
        self.isShooter = False

        self.rect.left = self.x
        self.rect.top =  self.y

    def check_edges(self):
        return (self.rect.left <= 0) or (self.rect.right >= self.screenRect.right)
    
    def update(self):
        self.rect.x += (self.set.alien_speed * self.set.fleet_direction)

