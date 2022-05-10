import pygame

class Paddle:
    def __init__(self,x,y,wide,tall):
        self.x = x
        self.y = y
        self.wide = wide
        self.tall = tall
        self.vely = 0

    def moveUp(self):
        self.vely = - 10


    def moveDown(self):
        self.vely = 10

    def update(self):
        self.y += self.vely


    def draw(self,screen,colour):
        pygame.draw.rect(screen,colour,(self.x,self.y,self.wide,self.tall))