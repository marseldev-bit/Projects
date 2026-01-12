import pygame
import sys
from snakeModel import Snake

class gameWindow:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 840))
        self.screenRect = self.screen.get_rect()
        self.snake = Snake(self)
        self.clock = pygame.time.Clock()
        self.symb = ''
        self.map = pygame.image.load('image\map.bmp')
        
    def runGame(self): 
        while True:
            temp = self.symb
            self.move()
            self.moveOnField(temp)
            self.snake.rotateHead(self.symb)
            self.snake.runHead(self.symb)
            self.showDisplay()
            # self.snake.rotateTale(self.symb)
            # self.snake.runTale(self.symb)
            self.clock.tick(60)
      
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q: sys.exit()
                elif event.key == pygame.K_RIGHT:
                    self.symb = 'r'
                elif event.key == pygame.K_LEFT:
                    self.symb = 'l'
                elif event.key == pygame.K_UP:
                    self.symb = 'u'
                elif event.key == pygame.K_DOWN:
                    self.symb = 'd'
    
    def moveOnField(self, temp):
        if temp != self.symb:
            if temp == 'r':
                t = self.snake.headRect.right
                while t % 60 != 0: t += 1
                self.snake.headRect.right = t
            elif temp == 'l':
                t = self.snake.headRect.left
                while t % 60 != 0: t -= 1
                self.snake.headRect.left = t
            elif temp == 'u':
                t = self.snake.headRect.top
                while t % 60 != 0: t -= 1
                self.snake.headRect.top = t
            elif temp == 'd':
                t = self.snake.headRect.bottom
                while t % 60 != 0: t += 1
                self.snake.headRect.bottom = t

    def showDisplay(self):
        self.screen.blit(self.map, self.map.get_rect())
        self.snake.draw()
        pygame.display.flip()


if __name__ == "__main__":
    snake = gameWindow()
    snake.runGame()