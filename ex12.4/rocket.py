import pygame
from rocketModel import Rocket
from bullets import Bullet
import sys

class RocketGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.screenRect = self.screen.get_rect()
        self.screenTitle = pygame.display.set_caption("Rocket")
        self.bg = (42, 50, 75)
        self.clock = pygame.time.Clock()

        self.model = Rocket(self)
        self.bullets = pygame.sprite.Group()
        self.maxBullets = 5

        self.moveRight = False
        self.moveLeft = False
        self.moveUp = False
        self.moveDown = False

    def runGame(self):
        while True:
            self.check_event()
            self.updateBullet()
            self.model.moveRocket()
            self.updateScreen()
            self.clock.tick(60)


    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q: sys.exit()
                elif event.key == pygame.K_UP:
                    self.moveUp = True
                elif event.key == pygame.K_DOWN:
                    self.moveDown = True
                elif event.key == pygame.K_SPACE:
                    self.goBullets()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.moveUp = False
                elif event.key == pygame.K_DOWN:
                    self.moveDown = False
    
    def goBullets(self):
        if len(self.bullets) <= self.maxBullets:
            newBullet = Bullet(self)
            self.bullets.add(newBullet)
        
    def updateScreen(self):
        self.screen.fill(self.bg)
        for bullet in self.bullets:
            bullet.drawBullet()
        self.model.showModel()
        pygame.display.flip()

    def updateBullet(self):
        for bullet in self.bullets: 
            bullet.shoot()
        for bullet in self.bullets.copy():
            if bullet.rect.right >= self.screenRect.right:
                self.bullets.remove(bullet)

if __name__ == "__main__":
    rock = RocketGame()
    rock.runGame()

