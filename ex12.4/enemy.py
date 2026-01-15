import pygame


class Enemy:
    def __init__(self, game):
        self.screen = game.screen
        self.screenRect = self.screen.get_rect()
        self.enemy = pygame.image.load('C:\\Users\\marse\\OneDrive\\Рабочий стол\\Projects\\SpaceWar\\images\\alien.bmp')
        self.rect = self.enemy.get_rect()
        self.rect.midright = self.screenRect.midright
        self.direction = 'up'
        self.speed = 20

    def run(self):
        if self.direction == 'up':
            if self.rect.top <= 0:
                self.direction = 'down'
                self.rect.y += self.speed
            else:
                self.rect.y -= self.speed
        elif self.direction == 'down':
            if self.rect.bottom >= self.screenRect.bottom:
                self.direction = 'up'
                self.rect.y -= self.speed
            else: 
                self.rect.y += self.speed
    
    def showEnemy(self):
        self.screen.blit(self.enemy, self.rect)