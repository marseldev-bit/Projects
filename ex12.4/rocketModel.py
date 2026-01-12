import pygame

class Rocket:
    def __init__(self, game):
        pygame.init()
        self.model = pygame.image.load("C:\\Users\\marse\\OneDrive\\Рабочий стол\\Projects\\SpaceWar\\images\\ship.bmp")
        self.rect = self.model.get_rect()
        self.screenRect = game.screen.get_rect()
        self.speed = 3
        self.game = game
        self.screen = game.screen
        self.rect.midleft = self.screenRect.midleft

    def moveRocket(self):
        if self.game.moveUp and self.screenRect.top < self.rect.top:
            self.rect.y -= self.speed
        elif self.game.moveDown and self.screenRect.bottom > self.rect.bottom:
            self.rect.y += self.speed

    def showModel(self):
        self.screen.blit(self.model, self.rect)
